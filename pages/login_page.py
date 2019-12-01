import logging
from base.basepage import BasePage
import time
import logging
import utilities.custom_logger as cl
import allure


class LoginPage(BasePage):

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.loginPage_locators = self.pageLocators('LoginPage')

    @property
    def isAt(self):
        header_login = self.getElementList(*self.locator(self.loginPage_locators, 'invalid_login_message'))
        print(len(header_login))
        if len(header_login) > 0:
            return True
        else:
            return False

    def login(self, email, password):
        self.clearKeys(*self.locator(self.loginPage_locators, 'email_textbox'))
        with allure.step('Entering username'):
            self.sendKeys(email, *self.locator(self.loginPage_locators, 'email_textbox'))
            self.log.info('Username has been entered successfully')
        with allure.step('Entering password'):
            self.clearKeys(*self.locator(self.loginPage_locators, 'password_textbox'))
            self.sendKeys(password, *self.locator(self.loginPage_locators, 'password_textbox'))
            self.log.info('Password has been entered successfully')
        with allure.step('Login button clicked'):
            self.elementClick(*self.locator(self.loginPage_locators, 'login_button'))
            self.log.info('Login button clicked')
            time.sleep(6)
