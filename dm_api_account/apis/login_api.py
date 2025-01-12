import requests


class LoginApi:
    def __init__(
            self,
            host,
            headers=None
            ):
        self.host = host
        self.headers = headers

    def post_v1_account_login(
            self,
            json_data
            ):
        """
        Authenticate via credentials
        :param json_data:
        :return:
        """
        response = requests.post(
            url=f'{self.host}/v1/account/login',
            json=json_data
        )
        return response

    def delete_v1_account_login(self):
        """
        Logout as current user
        :return:
        """
        ...

    def delete_v1_account_login_all(self):
        """
        Logout from every device
        :return:
        """
        ...
