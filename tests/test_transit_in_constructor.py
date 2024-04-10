import time
import settings
from locators import StellarBurgersLocators
from data import StellarBurgersData
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

class TestStellarBurgerConstructor:
    def test_transit_in_constructor_souces(self, driver):
        driver.find_element(*StellarBurgersLocators.SOUCES).click()
        assert driver.find_element(*StellarBurgersLocators.SOUCES_NAME).is_displayed()

    def test_transit_in_constructor_fillings(self, driver):
        driver.find_element(*StellarBurgersLocators.FILLINGS).click()
        assert driver.find_element(*StellarBurgersLocators.FILLINGS_NAME).is_displayed()

    def test_transit_in_constructor_bulki(self, driver):
        driver.find_element(*StellarBurgersLocators.FILLINGS).click()
        assert driver.find_element(*StellarBurgersLocators.FILLINGS_NAME).is_displayed()
        driver.find_element(*StellarBurgersLocators.BULKI).click()
        assert driver.find_element(*StellarBurgersLocators.BULKI_NAME).is_displayed()