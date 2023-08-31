import pytest
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from Utilities.BaseClass import BaseClass
from pageObjects.HomePage import HomePage


class TestHomePage(BaseClass):

    @pytest.mark.parametrize("name, email, password, gender", [("Adam", "example.com", "1qaz", "Male"),
                                                               ("Dominika", "example.pl", "2wsx", "Female")])
    def test_formSubmission(self, name, email, password, gender):
        home_page = HomePage(self.driver)
        home_page.getName().send_keys(name)
        home_page.getEmail().send_keys(email)
        home_page.getPassword().send_keys(password)
        home_page.getCheckbox().click()
        home_page.getRadio().click()
        self.selectOptionByText(home_page.getGender(), gender)
        home_page.getSubmit().click()
        alert_text = home_page.getAlert().text
        assert "Success" in alert_text
        self.driver.refresh()

