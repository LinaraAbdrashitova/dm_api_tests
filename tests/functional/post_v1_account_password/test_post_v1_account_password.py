# def test_post_v1_account_password(account_helper, prepare_user):
#     login = prepare_user.login
#     password = prepare_user.password
#     email = prepare_user.email
#     account_helper.register_new_user(
#         login=login,
#         email=email,
#         password=password
#     )
#     account_helper.user_login(login=login, password=password)
#     account_helper.reset_password(login=login, email=email)
#     account_helper.user_login(login=login, password=password)