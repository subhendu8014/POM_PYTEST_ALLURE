import logging
from base.basepage import BasePage
import logging
import utilities.custom_logger as cl
from pages.login_page import LoginPage
from utilities.teststatus import QAStatus
import test_data.testData as td
import time


class DashBoardPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.dashboardPage_locators = self.pageLocators('DashboardPage')

    @property
    def isAt(self):
        header_login = self.getElementList(*self.locator(self.dashboardPage_locators, 'dashboard_logo'))
        if len(header_login) > 0:
            return True
        else:
            return False



