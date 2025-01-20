from services.dm_api_account import DMApiAccount
from services.api_mailhog import MailHogApi
from helpers.account_helper import AccountHelper

from restclient.configuration import Configuration as MailhogConfiguration
from restclient.configuration import Configuration as DmApiConfiguration
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
    mailhog_configuration = MailhogConfiguration(host='http://5.63.153.31:5025')
    dm_api_configuration = DmApiConfiguration(host='http://5.63.153.31:5051', disable_log=False)
    account = DMApiAccount(configuration=dm_api_configuration)
    mailhog = MailHogApi(configuration=mailhog_configuration)
    account_helper = AccountHelper(dm_account_api=account, mailhog=mailhog)
    login = 'linara41'
    email = f'{login}@mail.ru'
    password = '123456789'
    account_helper.register_new_user(login=login, password=password, email=email)
    account_helper.user_login(login=login,password=password)

    #Меняем емейл
    json_data = {
        'login': login,
        'password': password,
        'email': 'new_' + email,
    }
    response = account_helper.dm_account_api.account_api.put_v1_account_email(json_data=json_data)

    # Пытаемся войти, получаем 403
    json_data = {
        'login': login,
        'password': password,
        'remember_me': True,
    }
    response = account_helper.dm_account_api.login_api.post_v1_account_login(json_data=json_data)
    assert response.status_code == 403, "Пользователь авторизован"


    # На почте находим токен по новому емейлу для подтверждения смены емейла
    response = account_helper.mailhog.mailhog_api.get_api_v2_messages()
    assert response.status_code == 200, "Письма не были получены"
    token = account_helper.get_activation_token_by_login(login=login, response=response)
    assert token is not None, f"Токен для пользователя {login} не был получен"
    # Активируем этот токен
    response = account_helper.dm_account_api.account_api.put_v1_account_token(token=token)
    assert response.status_code == 200, "Пользователь не был активирован"
    # Логинимся
    account_helper.user_login(login=login, password=password)


