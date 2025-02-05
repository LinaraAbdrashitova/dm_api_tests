from datetime import datetime

from hamcrest import assert_that, has_property, starts_with, all_of, instance_of, has_properties, equal_to


def test_get_v1_account_auth(auth_account_helper):

    response = auth_account_helper.get_user()

    assert_that(response, all_of(
        has_property('resource', has_property('login', equal_to("linara_27_01_2025_13_05_15"))),
        has_property('resource', has_property('online', instance_of(datetime))),
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


def test_get_v1_account_no_auth(account_helper):
    account_helper.get_user(validate_response=False)
