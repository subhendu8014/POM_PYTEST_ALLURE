import unittest
import pytest
from pages.login_page import LoginPage
from pages.dashboard_page import DashBoardPage
from utilities.teststatus import QAStatus
import test_data.testData as td
from base.basepage import BasePage
import allure
import logging
import utilities.custom_logger as cl


@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class TestLoginFunctionality(unittest.TestCase, BasePage):
    log = cl.customLogger(logging.DEBUG)

    @allure.title('Verifying landing in login page')
    @pytest.mark.run(order=1)
    def test_title(self):
        self.loginPage = LoginPage(self.driver)
        print('Validating landing in Login Page.')
        with allure.step('Checking whether login page is launched'):
            assert "Your store. Login" in self.driver.title
            print('Login page launched successfully')
            self.log.info('Login page launched successfully')

    @allure.title('Verifying login with valid credential')
    @pytest.mark.run(order=2)
    def test_valid_login(self):
        self.loginPage = LoginPage(self.driver)
        self.dashboardPage = DashBoardPage(self.driver)
        self.testStatus = QAStatus(self.driver)
        print('Performing login')
        self.loginPage.login(email=td.testData("email"), password=td.testData("password"))
        with allure.step('Checking whether dashboard page is launched'):
            self.testStatus.markFinal(self.dashboardPage.isAt, "login failed")
            print('Login successful')
            self.log.info('Login successful with valid credential')

    @allure.title('Verifying login with invalid credential')
    @pytest.mark.run(order=3)
    def test_invalid_login(self):
        self.loginPage = LoginPage(self.driver)
        self.testStatus = QAStatus(self.driver)
        print('Performing invalid login')
        self.loginPage.login(email=td.testData("wrong_email"), password=td.testData("wrong_password"))
        with allure.step('Checking whether control stays in Login page'):
            self.testStatus.markFinal(self.loginPage.isAt, "Invalid login failed")
            print('Login unsuccessful')
            self.log.info('Login unsuccessful with invalid credential')
