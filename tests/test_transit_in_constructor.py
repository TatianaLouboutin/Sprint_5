import time
import settings
from locators import StellarBurgersLocators
from data import StellarBurgersData
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

class TestStellarBurgerConstructor:
    def test_transit_in_constructor_souces(self, driver):
        driver.find_element(*StellarBurgersLocators.SOUCES).click()
        assert (driver.find_element(*StellarBurgersLocators.SOUCES_CLASS_PARENT).
                       get_attribute('class') == 'tab_tab__1SPyG tab_tab_type_current__2BEPc pt-4 pr-10 pb-4 pl-10 noselect')

    def test_transit_in_constructor_fillings(self, driver):
        driver.find_element(*StellarBurgersLocators.FILLINGS).click()
        assert (driver.find_element(*StellarBurgersLocators.FILLINGS_CLASS_PARENT).
                       get_attribute('class') == 'tab_tab__1SPyG tab_tab_type_current__2BEPc pt-4 pr-10 pb-4 pl-10 noselect')

    def test_transit_in_constructor_bulki(self, driver):
        driver.find_element(*StellarBurgersLocators.FILLINGS).click()
        driver.find_element(*StellarBurgersLocators.BULKI).click()
        assert (driver.find_element(*StellarBurgersLocators.BULKI_CLASS_PARENT).
                       get_attribute('class') == 'tab_tab__1SPyG tab_tab_type_current__2BEPc pt-4 pr-10 pb-4 pl-10 noselect')