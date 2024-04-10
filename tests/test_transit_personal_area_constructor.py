import time
import settings
from locators import StellarBurgersLocators
from data import StellarBurgersData
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

class TestStellarBurgersTransit:
    def test_transit_personal_area(self, driver):
        driver.find_element(*StellarBurgersLocators.BUTTON_PERSONAL_AREA).click()
        time.sleep(3)
        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/login'

    def test_transit_button_constructor(self, driver):
        driver.find_element(*StellarBurgersLocators.BUTTON_PERSONAL_AREA).click()
        time.sleep(3)
        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/login'
        driver.find_element(*StellarBurgersLocators.BUTTON_CONSTRUCTOR).click()
        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/'

    def test_transit_button_burger(self, driver):
        driver.find_element(*StellarBurgersLocators.BUTTON_PERSONAL_AREA).click()
        time.sleep(3)
        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/login'
        driver.find_element(*StellarBurgersLocators.BUTTON_BURGER).click()
        time.sleep(2)
        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/'
