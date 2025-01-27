import time

from services.dm_api_account import DMApiAccount
from services.api_mailhog import MailHogApi
from json import loads


def retrier(function):
    def wrapper(*args,**kwargs):
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
        response = self.dm_account_api.login_api.post_v1_account_login(
            json_data={"login": login, "password":password}
        )
        token = {
            "x-dm-auth-token": response.headers["x-dm-auth-token"]
        }
        self.dm_account_api.account_api.set_headers(token)
        self.dm_account_api.login_api.set_headers(token)
    def register_new_user(
            self,
            login: str,
            password: str,
            email: str
    ):

        json_data = {
            'login': login,
            'email': email,
            'password': password,
        }
        response = self.dm_account_api.account_api.post_v1_account(json_data=json_data)
        assert response.status_code == 201, "Пользователь не был создан"

        token = self.get_activation_token_by_login(login=login)
        assert token is not None, f"Токен для пользователя {login} не был получен"
        response = self.activation_token(token=token)
        return response

    def reset_password(self, login:str, email: str):
        json_data = {
            'login': login,
            'email': email
        }
        response = self.dm_account_api.account_api.post_v1_account_password(json_data=json_data)
        return response

    def logout_user(self):
        response = self.dm_account_api.login_api.delete_v1_account_login()
        return response

    def logout_all_users(self):
        response = self.dm_account_api.login_api.delete_v1_account_login_all()
        return response

    def get_user(self):
        response = self.dm_account_api.account_api.get_v1_account()
        return response

    def user_login(
            self,
            login: str,
            password: str,
            remember_me: bool = True
            ):
        json_data = {
            'login': login,
            'password': password,
            'rememberMe': remember_me,
        }
        response = self.dm_account_api.login_api.post_v1_account_login(json_data=json_data)
        assert response.status_code == 200, "Пользователь не был авторизован"
        return response

    def change_email(
            self,
            login: str,
            password: str,
            email: str
            ):
        json_data = {
            'login': login,
            'password': password,
            'email': email,
        }
        response = self.dm_account_api.account_api.put_v1_account_email(json_data=json_data)
        return response

    def change_password(
            self,
            login: str,
            oldPassword: str,
            newPassword: str,
            email: str
    ):
        self.auth_client(login=login, password=oldPassword) #дальше должен пробрасываться токен аутентификации
        response = self.reset_password(login=login, email=email)
        token = self.get_token_by_reset_password(login=login)
        json_data = {
            'login': login,
            'oldPassword': oldPassword,
            'newPassword': newPassword,
            'token': token
        }
        response = self.dm_account_api.account_api.put_v1_account_password(json_data=json_data)
        assert response.status_code == 200, "Пароль не был изменен"
        return response

    @retrier
    def get_activation_token_by_login(
            self,
            login
    ):
        response = self.mailhog.mailhog_api.get_api_v2_messages()
        #assert response.status_code == 200, "Письма не были получены"
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
        response = self.dm_account_api.account_api.put_v1_account_token(token=token)
        assert response.status_code == 200, "Пользователь не был активирован"
        return response
