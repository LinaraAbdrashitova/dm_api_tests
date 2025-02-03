import time

from dm_api_account.models.change_email import ChangeEmail
from dm_api_account.models.login_credentials import LoginCredentials
from dm_api_account.models.registration import Registration
from dm_api_account.models.reset_password import ResetPassword
from dm_api_account.models.change_password import ChangePassword
from services.dm_api_account import DMApiAccount
from services.api_mailhog import MailHogApi
from json import loads


def retrier(function):
    def wrapper(*args, **kwargs):
        token = None
        count = 0
        while token is None:
            print(f"Попытка получения токена номер {count + 1}")
            token = function(*args, **kwargs)
            count += 1
            if count == 5:
                raise AssertionError("Превышено количество попыток получения активационного токена!")
            if token:
                return token
            time.sleep(1)

    return wrapper


class AccountHelper:
    def __init__(
            self,
            dm_account_api: DMApiAccount,
            mailhog: MailHogApi
    ):
        self.dm_account_api = dm_account_api
        self.mailhog = mailhog

    def auth_client(self, login: str, password: str):
        response = self.user_login(login=login, password=password)
        token = {
            "x-dm-auth-token": response.headers["x-dm-auth-token"]
        }
        self.dm_account_api.account_api.set_headers(token)
        self.dm_account_api.login_api.set_headers(token)

    def register_new_user(self, login: str, password: str, email: str):
        registration = Registration(
            login=login,
            password=password,
            email=email
        )
        response = self.dm_account_api.account_api.post_v1_account(registration=registration)
        assert response.status_code == 201, "Пользователь не был создан"
        start_time = time.time()
        token = self.get_activation_token_by_login(login=login)
        end_time = time.time()
        assert end_time - start_time < 3, "время ожидания превышено"
        assert token is not None, f"Токен для пользователя {login} не был получен"
        response = self.activation_token(token=token)
        return response

    def reset_password(self, login: str, email: str, password: str):
        response = self.user_login(login=login, password=password)
        headers = {
            "x-dm-auth-token": response.headers["x-dm-auth-token"]
        }
        reset_password = ResetPassword(
            login=login,
            email=email
        )
        response = self.dm_account_api.account_api.post_v1_account_password(reset_password=reset_password,
                                                                            headers=headers)
        return response

    def logout_user(self):
        response = self.dm_account_api.login_api.delete_v1_account_login()
        return response

    def logout_all_users(self):
        response = self.dm_account_api.login_api.delete_v1_account_login_all()
        return response

    def get_user(self, validate_response=True):
        response = self.dm_account_api.account_api.get_v1_account(validate_response=validate_response)
        return response

    def user_login(self, login: str, password: str, remember_me: bool = True, validate_response=False):
        login_credentials = LoginCredentials(
            login=login,
            password=password,
            remember_me=remember_me
        )
        response = self.dm_account_api.login_api.post_v1_account_login(
            login_credentials=login_credentials,
            validate_response=validate_response
        )
        assert response.headers["x-dm-auth-token"], "Авторизационный токен не был получен"
        # assert response.status_code == 200, "Пользователь не был авторизован"
        return response

    def change_email(
            self,
            login: str,
            password: str,
            email: str
    ):
        change_email = ChangeEmail(
            login=login,
            password=password,
            email=email
        )
        response = self.dm_account_api.account_api.put_v1_account_email(change_email=change_email)
        return response

    def change_password(
            self,
            login: str,
            old_password: str,
            new_password: str,
            email: str
    ):
        self.reset_password(login=login, email=email, password=old_password)
        token = self.get_token_by_reset_password(login=login)
        change_password = ChangePassword(
            login=login,
            token=token,
            old_password=old_password,
            new_password=new_password
        )
        response = self.dm_account_api.account_api.put_v1_account_password(change_password=change_password)
        assert response.status_code == 200, "Пароль не был изменен"
        return response

    @retrier
    def get_activation_token_by_login(
            self,
            login
    ):
        response = self.mailhog.mailhog_api.get_api_v2_messages()
        # assert response.status_code == 200, "Письма не были получены"
        token = None
        for item in response.json()['items']:
            user_data = loads(item['Content']['Body'])
            user_login = user_data['Login']
            if user_login == login:
                token = user_data['ConfirmationLinkUrl'].split('/')[-1]
                print(token)
        return token

    @retrier
    def get_token_by_reset_password(
            self,
            login
    ):
        response = self.mailhog.mailhog_api.get_api_v2_messages()
        # assert response.status_code == 200, "Письма не были получены"
        token = None
        for item in response.json()['items']:
            user_data = loads(item['Content']['Body'])
            user_login = user_data['Login']
            if user_login == login and 'ConfirmationLinkUri' in user_data:
                token = user_data['ConfirmationLinkUri'].split('/')[-1]
                print(token)
        return token

    def activation_token(
            self,
            token
    ):
        response = self.dm_account_api.account_api.put_v1_account_token(token=token, validate_response=False)
        assert response.status_code == 200, "Пользователь не был активирован"
        return response
