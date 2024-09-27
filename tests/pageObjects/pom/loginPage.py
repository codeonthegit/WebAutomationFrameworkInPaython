from selenium.webdriver.common.by import By
from tests.utils.common_utilis import webdriver_wait
class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    # Page Locators
    username = (By.ID, "login-username")
    password = (By.NAME, "password")
    submit_button = (By.ID,"js-login-btn")
    error_message = (By.ID,"js-notification-box-msg")

    #Page Actions
    def get_username(self):
        return self.driver.find_element(*LoginPage.username)

    def get_password(self):
        return self.driver.find_element(*LoginPage.password)

    def get_submit_button(self):
        return self.driver.find_element(*LoginPage.submit_button)

    def get_error_message(self):
        webdriver_wait(driver=self.driver, element_tuple=self.username, timeout=5)
        return self.driver.find_element(*LoginPage.error_message)


    def login_to_vwo(self, usr, pwd):
        self.get_username().send_keys(usr)
        self.get_password().send_keys(pwd)
        self.get_submit_button().click()

    def get_error_message_text(self):
        return self.get_error_message().text








