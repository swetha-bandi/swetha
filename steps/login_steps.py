from pytest_bdd import given, when, then, parsers, scenarios

from conftest import driver
from pages.login_page import LoginPage

import allure
from pytest_bdd import scenarios



scenarios("../features/login.feature")
scenarios("../features/logout.feature")


@given("user on login page")
def user_on_login_page(driver):
    allure.dynamic.feature("Login")
    allure.dynamic.story("Valid Login")
    allure.dynamic.severity(allure.severity_level.CRITICAL)
    allure.dynamic.description(
        "Verify that a valid user can log in, add a product to the cart, complete checkout, and place an order successfully."
    )


@when(parsers.cfparse('user enter the username "{username}"'))
def user_enter_username(driver, username):
    login_page = LoginPage(driver)
    login_page.enter_username(username)

@when(parsers.cfparse('user enter the password "{password}"'))
def user_enter_password(driver, password):
    login_page = LoginPage(driver)
    login_page.enter_password(password)

@when("user click on login button")
def user_login_button(driver):
    login_page = LoginPage(driver)
    login_page.click_login()

@when("user add back pack to add to cart")
def user_add_to_cart_button(driver):
    login_page = LoginPage(driver)
    login_page.click_add_to_cart()

@when("user clicks on the cart button")
def user_click_cart_button(driver):
    login_page = LoginPage(driver)
    login_page.click_shopping_cart()

@when("user clicks on checkout button")
def user_click_checkout_button(driver):
    login_page = LoginPage(driver)
    login_page.click_checkout_button()

@when(parsers.cfparse('user enters firstname "{firstname}"'))
def user_enter_firstname(driver, firstname):
    login_page = LoginPage(driver)
    login_page.enter_first_name(firstname)

@when(parsers.cfparse('user enters lastname "{lastname}"'))
def user_enter_lastname(driver, lastname):
    login_page = LoginPage(driver)
    login_page.enter_last_name(lastname)

@when(parsers.cfparse('user enters postal code "{postal_code}"'))
def user_enter_postal_code(driver, postal_code):
    login_page = LoginPage(driver)
    login_page.enter_postal_code(postal_code)

@when("user clicks continue button")
def user_click_continue_button(driver):
    login_page = LoginPage(driver)
    login_page.click_continue()

@when("user click finish button")
def user_click_finish_button(driver):
    login_page = LoginPage(driver)
    login_page.click_finish()

@then("the order should be placed successfully")
def verify_order_success(driver):
    login_page = LoginPage(driver)

    expected = "Thank you for your order!"
    actual = login_page.get_complete_header()

    assert actual == expected

@when("user click on burger button")
def user_click_burger_button(driver):
    login_page = LoginPage(driver)
    login_page.click_react_burger_menu()

@then("user click on logout button")
def user_click_logout_button(driver):
    login_page = LoginPage(driver)
    login_page.click_logout_button()










