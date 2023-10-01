from dm_api_account.models import Registration, ResetPassword, ChangePassword, ChangeEmail


class Account:
    def __init__(self, facade):
        from services.dm_api_account import Facade
        self.facade: Facade = facade
        # в facade приходит класс Facade, в котором будет лежать все, что у нас есть

    def set_headers(self, headers):
        """
        Set headers in class helper
        :param headers:
        :return:
        """
        self.facade.account_api.client.session.headers.update(headers)

    def register_new_user(self, login: str, email: str, password: str, status_code: int = 201):
        response = self.facade.account_api.post_v1_account(
            json=Registration(
                login=login,
                email=email,
                password=password
            ),
            status_code=status_code
        )
        return response

    def activate_registered_user(self, login: str, status_code: int = 200):
        token = self.facade.mailhog.get_token_by_login(login=login)
        response = self.facade.account_api.put_v1_account_token(
            token=token,
            status_code=status_code
        )
        return response

    def get_current_user_info(self, **kwargs):
        response = self.facade.account_api.get_v1_account(**kwargs)
        return response

    def reset_registered_user_password(self, login: str, email: str, status_code: int = 201, **kwargs):
        response = self.facade.account_api.post_v1_account_password(
            json=ResetPassword(
                login=login,
                email=email,
            ),
            status_code=status_code,
            **kwargs
        )

        return response

    def change_registered_user_password(self, login: str, old_password: str, new_password: str,status_code: int=200, **kwargs):
        token = self.facade.mailhog.get_token_by_change_password(login=login)
        print("______________________________________" + token)
        response = self.facade.account_api.put_v1_account_password(
            json=ChangePassword(
                login=login,
                token=token,
                old_password=old_password,
                new_password=new_password
            ),
            status_code=status_code,
            **kwargs)

        return response

    def change_registered_user_email(self, login: str, email: str, password: str, status_code: int = 200):
        response = self.facade.account_api.put_v1_account_email(
            json=ChangeEmail(
                login=login,
                email=email,
                password=password
            ),
            status_code=status_code
        )
        return response

    def get_reset_password_token(self, login: str, email: str, **kwargs):
        response = self.reset_registered_user_password(login=login, email=email, **kwargs)

        # token = {'X-Dm-Auth-Token': response.headers['X-Dm-Auth-Token']}
        return response
