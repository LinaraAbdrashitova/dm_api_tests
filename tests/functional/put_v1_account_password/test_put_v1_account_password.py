def test_put_v1_account_password(account_helper, prepare_user):
    login = prepare_user.login
    password = prepare_user.password
    email = prepare_user.email
    account_helper.register_new_user(
        login=login,
        email=email,
        password=password
    )
    account_helper.user_login(login=login, password=password)
    # Смена пароля с пробросом авторизационного токена в хэдэры и указанием токена для сброса пароля из письма
    account_helper.change_password(login=login, oldPassword=password, newPassword='987654321', email=email)
    # Авторизация пользователя с новым паролем
    account_helper.user_login(login=login, password='987654321')
