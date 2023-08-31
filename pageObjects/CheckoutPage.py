from selenium.webdriver.common.by import By
from pageObjects.ConfirmPage import ConfirmPage


class CheckoutPage:

    def __init__(self, driver):
        self.driver = driver

    cardTitle = (By.XPATH, "//h4/a")
    cardFooterButton = (By.CSS_SELECTOR, ".card-footer button")
    checkoutButton = (By.CSS_SELECTOR, "a[class$='nav-link btn btn-primary']")
    successButton = (By.XPATH, "//button[@class='btn btn-success']")

    def GetCardTitles(self):
        return self.driver.find_elements(*CheckoutPage.cardTitle)

    def GetFooterButton(self):
        return self.driver.find_elements(*CheckoutPage.cardFooterButton)

    def GetCheckoutButton(self):
        return self.driver.find_element(*CheckoutPage.checkoutButton)

    def GetSuccessButton(self):
        self.driver.find_element(*CheckoutPage.successButton).click()
        confirm_page = ConfirmPage(self.driver)
        return confirm_page
