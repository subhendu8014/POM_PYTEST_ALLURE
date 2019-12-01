from base.selenium_driver import SeleniumDriver
import logging
from traceback import print_stack


class QAStatus(SeleniumDriver):

    def __init__(self, driver):
        """
        Inits CheckPoint class

        """
        super(QAStatus, self).__init__(driver)
        super().__init__(driver)
        self.resultList = []

    def setResult(self, result, resultMessage):
        try:
            if result is not None:
                if result:
                    self.resultList.append("PASS")
                else:
                    self.resultList.append("FAIL")
            else:
                self.resultList.append("FAIL")
        except:
            self.resultList.append("FAIL")
            print_stack()

    def mark(self, result, resultMessage):
        """
        Mark the result of the verification point in a test case
        """
        self.setResult(result, resultMessage)

    def markFinal(self, result, resultMessage):
        """
        Mark the final result of the verification point in a test case
        This needs to be called at least once in a test case
        This should be final test status of the test case
        """
        self.setResult(result, resultMessage)
        if "FAIL" in self.resultList:
            self.resultList.clear()
            assert False, resultMessage
        else:
            self.resultList.clear()
            assert True
