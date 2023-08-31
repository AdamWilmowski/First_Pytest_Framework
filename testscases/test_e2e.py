import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Utilities.BaseClass import BaseClass
from pageObjects.HomePage import HomePage
from pageObjects.CheckoutPage import CheckoutPage


class TestOne(BaseClass):

    def test_e2e(self):
        log = self.getLogger()
        home_page = HomePage(self.driver)
        checkout_page = home_page.shopItems()
        products = checkout_page.GetCardTitles()
        i = -1
        for product in products:
            i = i + 1
            product_text = product.text
            if product_text == "Blackberry":
                checkout_page.GetFooterButton()[i].click()
        self.WaitForElementsInBasket("1")
        checkout_page.GetCheckoutButton().click()
        confirm_page = checkout_page.GetSuccessButton()
        confirm_page.GetInputCountry().send_keys("po")
        self.VerifyLinkTextPresence("Poland")
        confirm_page.GetCountryPoland().click()
        confirm_page.GePrimaryCheckbox().click()
        confirm_page.GetSubmitButton().click()
        self.WaitForAlertPresence()
        success_message = confirm_page.GetAlertMessage().text

        assert "Success" in success_message
