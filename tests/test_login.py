import pytest
import allure
from api.application_api import application_api


@pytest.mark.categories(component='login', suite='smoke')
@allure.feature('POST /api/auth/login')
@pytest.mark.login
class TestLogin(object):
    @allure.story('Check Authorization')
    @allure.title('Login: {query[2]}; Pass - {query[0]}, Expect status - {query[1]}')
    @pytest.mark.parametrize("query", (
            ['Qwe123', '200', "Заглавная бука, цифры, буквы нижнего регистра"], ['   ', '401', 'пробельные символы'],
            ['sdasdqweQW', '401', 'латинские буквы нижнего и верхнего регистра'], ['', '406', 'пустой пароль']))
    def test_login(self, query):
        response_login = application_api.login('test4444', query[0])

        print('\ntest data: login - test4444, pass - %s, expected result: %s' % (query[0], query[1]))
        assert query[1] == str(response_login.status_code)
