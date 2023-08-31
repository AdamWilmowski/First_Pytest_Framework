from selenium.webdriver.common.by import By


class ConfirmPage:

    def __init__(self, driver):
        self.driver = driver

    input_country = (By.ID, "country")
    country_poland = (By.LINK_TEXT, "Poland")
    primary_checkbox = (By.XPATH, "//div[@class='checkbox checkbox-primary']")
    submit_button = (By.CSS_SELECTOR, "input[type='submit']")
    alert_message = (By.CSS_SELECTOR, ".alert.alert-success.alert-dismissible")

    def GetInputCountry(self):
        return self.driver.find_element(*ConfirmPage.input_country)

    def GetCountryPoland(self):
        return self.driver.find_element(*ConfirmPage.country_poland)

    def GePrimaryCheckbox(self):
        return self.driver.find_element(*ConfirmPage.primary_checkbox)

    def GetSubmitButton(self):
        return self.driver.find_element(*ConfirmPage.submit_button)

    def GetAlertMessage(self):
        return self.driver.find_element(*ConfirmPage.alert_message)