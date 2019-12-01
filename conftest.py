import pytest
from selenium import webdriver
import time
import test_data.testData as td


@pytest.fixture()
def setUp(request):
    print("Running method level setUp")
    print("initiating chrome driver")
    driver = webdriver.Chrome("./drivers/chromedriver.exe")
    driver.maximize_window()
    request.cls.driver = driver
    driver.get(td.testData("environment_url"))
    time.sleep(3)
    yield
    print("Running method level tearDown")
    driver.close()


@pytest.fixture(scope="class")
def oneTimeSetUp(request):
    print("Running class setUp")
