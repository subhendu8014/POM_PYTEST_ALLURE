from base.basepage import BasePage
import time
import logging
import utilities.custom_logger as cl


class CustomerPage(BasePage):

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.customerPage_locators = self.pageLocators('CustomerPage')

    @property
    def isAt(self):
        header_login = self.getElementList(*self.locator(self.customerPage_locators, 'customer_logo'))
        if len(header_login) > 0:
            return True
        else:
            return False

    def verify_add_customer(self):
        self.elementClick(*self.locator(self.customerPage_locators, 'customer_drop_down'))
        self.log.info('Customer drop down clicked')
        time.sleep(6)
        self.elementClick(*self.locator(self.customerPage_locators, 'customer_button'))
        self.log.info('Customer option clicked')


