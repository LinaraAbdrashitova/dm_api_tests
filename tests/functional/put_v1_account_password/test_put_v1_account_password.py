def test_put_v1_account_password(account_helper, prepare_user):
    """
    Смена пароля с пробросом авторизационного токена в хэдэры и указанием токена для сброса пароля из письма
    :param account_helper:
    :param prepare_user:
    :return:
    """
    login = prepare_user.login
    password = prepare_user.password
    email = prepare_user.email
    new_password = '987654321'
    account_helper.register_new_user(
        login=login,
        email=email,
        password=password
    )
    account_helper.change_password(login=login, old_password=password, new_password=new_password, email=email)
    # Авторизация пользователя с новым паролем
    account_helper.user_login(login=login, password=new_password)
