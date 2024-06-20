import datetime
import pytest
from selenium import webdriver
import logging


def pytest_addoption(parser):
    parser.addoption("--browser", default="chrome")
    parser.addoption("--log_level", action="store", default="INFO")


@pytest.fixture
def driver(request):
    url = "https://demo-opencart.ru"

    browser = request.config.getoption("--browser")
    log_level = request.config.getoption("--log_level")
    logger = logging.getLogger(request.node.name)
    file_handler = logging.FileHandler(f"logs/{request.node.name}.log")
    file_handler.setFormatter(logging.Formatter("%(levelname)s %(message)s"))
    logger.addHandler(file_handler)
    logger.setLevel(level=log_level)
    logger.info("===> Test %s started at %s" % (request.node.name, datetime.datetime.now()))

    if browser == "chrome":
        driver = webdriver.Chrome()
    elif browser == "firefox":
        driver = webdriver.Firefox()
    else:
        raise Exception("Driver not supported")

    driver.log_level = log_level
    driver.logger = logger

    logger.info("Browser %s started" % browser)

    def fin():
        driver.quit()
        logger.info("===> Test %s finished at %s" % (request.node.name, datetime.datetime.now()))

    request.addfinalizer(fin)

    driver.get(url)
    return driver
