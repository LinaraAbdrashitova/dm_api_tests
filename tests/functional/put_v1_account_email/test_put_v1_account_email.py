from dm_api_account.models.login_credentials import LoginCredentials
from checkers.http_checkers import check_status_code_http

def test_put_v1_account_email(account_helper, prepare_user):
    login = prepare_user.login
    password = prepare_user.password
    email = prepare_user.email
    account_helper.register_new_user(login=login, password=password, email=email)
    account_helper.user_login(login=login, password=password)
    account_helper.change_email(login=login, password=password, email='new_'+email)

    # Пытаемся войти, получаем 403
    with check_status_code_http(403, "User is inactive. Address the technical support for more details"):
        login_credentials = LoginCredentials(
            login=login,
            password=password,
            remember_me=True
        )
        response = account_helper.user_login(login=login, password=password)


    token = account_helper.get_activation_token_by_login(login=login)
    assert token is not None, f"Токен для пользователя {login} не был получен"
    # Активируем этот токен
    account_helper.activation_token(token=token)
    # Логинимся
    account_helper.user_login(login=login, password=password)


