def test_get_v1_account_auth(auth_account_helper):
    auth_account_helper.get_user()


def test_get_v1_account_no_auth(account_helper):
    account_helper.get_user(validate_response=False)
