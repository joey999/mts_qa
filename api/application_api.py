import allure
from api.client import HttpClient
from settings import configEnv


class ApplicationAPI(object):
    API_HOST = configEnv.get('api_host')

    def __init__(self):
        self._http_client = HttpClient(api_host=self.API_HOST)

    @allure.step("POST /auth/login")
    def login(self, login=None, password=None):
        data = dict()

        if login:
            data.update({'login': login})

        if password:
            data.update({'password': password})

        login_response = self._http_client.request('/auth/login', method='POST', data=data)

        return login_response


application_api = ApplicationAPI()
