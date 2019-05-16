from hamcrest import *
import allure


@allure.step('Check status: Actual - {actual}; Expect - {expect}')
def check_status(expect, actual):
    return assert_that(expect, equal_to(actual.status_code), actual.text)
