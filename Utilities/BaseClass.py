import inspect
import logging

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.mark.usefixtures("setup")
class BaseClass:

    def VerifyLinkTextPresence(self, text):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.LINK_TEXT, text)))

    def WaitForAlertPresence(self):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".alert.alert-success.alert-dismissible")))

    def WaitForElementsInBasket(self, text):
        WebDriverWait(self.driver, 10).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, "a[class$='nav-link btn btn-primary']"),f"Checkout ( {text} )"))

    def selectOptionByText(self, locator, text):
        select = Select(locator)
        select.select_by_visible_text(text)

    def getLogger(self):
        loggerName = inspect.stack()[1][3]
        logger = logging.getLogger(loggerName)
        fileHandler = logging.FileHandler('logfile.log')
        formatter = logging.Formatter("%(asctime)s :%(levelname)s : %(name)s :%(message)s")
        fileHandler.setFormatter(formatter)

        logger.addHandler(fileHandler)  # filehandler object

        logger.setLevel(logging.DEBUG)
        return logger

