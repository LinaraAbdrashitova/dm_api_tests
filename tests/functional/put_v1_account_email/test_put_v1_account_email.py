from json import loads

from dm_api_account.apis.account_api import AccountApi
from dm_api_account.apis.login_api import LoginApi
from api_mailhog.apis.mailhog_api import MailhogApi
import structlog

structlog.configure(
    processors=[
        structlog.processors.JSONRenderer(
            indent=4,
            ensure_ascii=True,
            sort_keys=True)
    ]
)

def test_put_v1_account_email():
    # Регистрация
    account_api = AccountApi(host='http://5.63.153.31:5051')
    login_api = LoginApi(host='http://5.63.153.31:5051')
    mailhog_api = MailhogApi(host='http://5.63.153.31:5025')
    login = 'linara15'
    email = f'{login}@mail.ru'
    password = '123456789'
    json_data = {
        'login': login,
        'email': email,
        'password': password,
    }

    response = account_api.post_v1_account(json_data=json_data)
    assert response.status_code == 201, "Пользователь не был создан"

    # Получаем активационный токен
    response = mailhog_api.get_api_v2_messages()
    assert response.status_code == 200, "Письма не были получены"
    token = get_activation_token_by_login(login, response)

    assert token is not None, f"Токен для пользователя {login} не был получен"
    # Активируем
    response = account_api.put_v1_account_token(token=token)
    assert response.status_code == 200, "Пользователь не был активирован"

    # Заходим
    json_data = {
        'login': login,
        'password': password,
        'rememberMe': True,
    }

    response = login_api.post_v1_account_login(json_data=json_data)
    assert response.status_code == 200, "Пользователь не был авторизован"
    #Меняем емейл
    json_data = {
        'login': login,
        'password': password,
        'email': 'new_' + email,
    }
    response = account_api.put_v1_account_email(json_data=json_data)

    # Пытаемся войти, получаем 403
    json_data = {
        'login': login,
        'password': password,
        'rememberMe': True,
    }

    response = login_api.post_v1_account_login(json_data=json_data)
    assert response.status_code == 403, "Пользователь авторизован"
    # На почте находим токен по новому емейлу для подтверждения смены емейла
    response = mailhog_api.get_api_v2_messages()
    assert response.status_code == 200, "Письма не были получены"
    token = get_activation_token_by_login(login, response)

    assert token is not None, f"Токен для пользователя {login} не был получен"
    # Активируем этот токен
    response = account_api.put_v1_account_token(token=token)
    assert response.status_code == 200, "Пользователь не был активирован"
    # Логинимся
    json_data = {
        'login': login,
        'password': password,
        'rememberMe': True,
    }

    response = login_api.post_v1_account_login(json_data=json_data)
    #print(response.headers)
    assert response.status_code == 200, "Пользователь не был авторизован"

def get_activation_token_by_login(
        login,
        response
):
    token = None
    for item in response.json()['items']:
        user_data = loads(item['Content']['Body'])
        user_login = user_data['Login']
        if user_login == login:
            token = user_data['ConfirmationLinkUrl'].split('/')[-1]
            print(token)
    return token
