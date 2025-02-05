from datetime import datetime
from checkers.http_checkers import check_status_code_http
import pytest
from hamcrest import assert_that, has_property, starts_with, all_of, instance_of, has_properties, equal_to




def test_post_v1_account(account_helper, prepare_user):
    login = prepare_user.login
    password = prepare_user.password
    email = prepare_user.email
    response = account_helper.register_new_user(
        login=login,
        email=email,
        password=password
    )
    response = account_helper.user_login(login=login, password=password, validate_response=True)
    assert_that(
        response, all_of(
            has_property('resource', has_property('login', starts_with("linara"))),
            has_property('resource', has_property('registration', instance_of(datetime))),
            has_property(
                'resource', has_property(

                    'rating', has_properties(
                        {

                            "enabled": equal_to(True),
                            "quality": equal_to(0),
                            "quantity": equal_to(0)
                        }
                    )

                ))
        )
    )

@pytest.mark.parametrize("login, email, password, error_message, expected_status_code", [
    ("linara_short_password1", "linara@yandex.ru", "short", "Validation failed", 400),
    ("linara_short_password2", "linarayandex.ru", "1234567", "Validation failed", 400),
    ("1", "linara@yandex.ru", "1234567", "Validation failed", 400)
])
def test_post_v1_account_bad(account_helper, login, email, password, error_message, expected_status_code):
    with check_status_code_http(expected_status_code, error_message):
        response = account_helper.register_new_user(
            login=login,
            email=email,
            password=password
        )
        #response = account_helper.user_login(login=login, password=password, validate_response=True)










