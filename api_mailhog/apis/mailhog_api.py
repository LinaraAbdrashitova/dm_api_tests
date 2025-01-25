import requests

from restclient.client import RestClient


class MailhogApi(RestClient):

    def get_api_v2_messages(
            self,
            limit=10
    ):
        """
        Get Users emails
        :return:
        """
        params = {
            'limit': limit
        }
        response = self.get(
            path='/api/v2/messages',
            params=params,
            verify=False
        )
        return response
