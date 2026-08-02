from locators.login_locators import LoginLocators
from pages.base_page import BasePage


class LoginPage(BasePage):

    def __init__(self,driver):
        super().__init__(driver)

    def enter_username(self,username):
        self.enter_text(LoginLocators.USERNAME, username)

    def enter_password(self,password):
        self.enter_text(LoginLocators.PASSWORD, password)

    def click_login(self):
        self.click(LoginLocators.LOGIN_BUTTON)

    def click_add_to_cart(self):
        self.click(LoginLocators.ADD_TO_CART)

    def click_shopping_cart(self):
        self.click(LoginLocators.CART_LINK)

    def click_checkout_button(self):
        self.click(LoginLocators.CHECKOUT_BUTTON)

    def enter_first_name(self,first_name):
        self.enter_text(LoginLocators.FIRST_NAME, first_name)

    def enter_last_name(self,last_name):
        self.enter_text(LoginLocators.LAST_NAME, last_name)

    def enter_postal_code(self,postal_code):
        self.enter_text(LoginLocators.POSTAL_CODE, postal_code)

    def click_continue(self):
        self.click(LoginLocators.CONTINUE_BUTTON)

    def click_finish(self):
        self.click(LoginLocators.FINISH_BUTTON)

    def get_complete_header(self):
        return self.get_text(LoginLocators.COMPLETE_HEADER)

    def click_react_burger_menu(self):
        self.click(LoginLocators.REACT_BURGER_MENU_BUTTON)

    def click_logout_button(self):
        self.click(LoginLocators.LOGOUT_BUTTON)





