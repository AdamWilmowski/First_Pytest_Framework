from selenium.webdriver.common.by import By
from pageObjects.CheckoutPage import CheckoutPage


class HomePage:

    def __init__(self, driver):
        self.driver = driver

    shop = (By.LINK_TEXT, "Shop")
    name = (By.XPATH, "//input[@name='name']")
    email = (By.XPATH, "//input[@name='email']")
    password = (By.ID, "exampleInputPassword1")
    checkbox = (By.ID, "exampleCheck1")
    radiobutton = (By.ID, "inlineRadio2")
    gender = (By.ID, "exampleFormControlSelect1")
    submit = (By.CSS_SELECTOR, "input[value='Submit']")
    alert = (By.XPATH, "//div[@class='alert alert-success alert-dismissible'] ")

    def shopItems(self):
        self.driver.find_element(*HomePage.shop).click()
        checkOutPage = CheckoutPage(self.driver)
        return checkOutPage

    def getName(self):
        return self.driver.find_element(*HomePage.name)

    def getEmail(self):
        return self.driver.find_element(*HomePage.email)

    def getPassword(self):
        return self.driver.find_element(*HomePage.password)

    def getCheckbox(self):
        return self.driver.find_element(*HomePage.checkbox)

    def getRadio(self):
        return self.driver.find_element(*HomePage.radiobutton)

    def getGender(self):
        return self.driver.find_element(*HomePage.gender)

    def getSubmit(self):
        return self.driver.find_element(*HomePage.submit)

    def getAlert(self):
        return self.driver.find_element(*HomePage.alert)