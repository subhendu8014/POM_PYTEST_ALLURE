import unittest
import pytest
from pages.login_page import LoginPage
from pages.dashboard_page import DashBoardPage
from pages.customer_page import CustomerPage
from utilities.teststatus import QAStatus
import test_data.testData as td
from base.basepage import BasePage
import allure


@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class TestCustomerFunctionality(unittest.TestCase, BasePage):

    @allure.title('Verifying customer creation')
    @pytest.mark.run(order=1)
    def test_customer_creation(self):
        self.loginPage = LoginPage(self.driver)
        self.dashboardPage = DashBoardPage(self.driver)
        self.customerPage = CustomerPage(self.driver)
        self.testStatus = QAStatus(self.driver)
        self.loginPage.login(email=td.testData("email"), password=td.testData("password"))
        self.testStatus.markFinal(self.dashboardPage.isAt, "login failed")
        with allure.step('Checking whether customer is created successfully'):
            self.customerPage.verify_add_customer()
