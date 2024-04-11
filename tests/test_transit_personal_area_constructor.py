import time
import settings
from locators import StellarBurgersLocators
from data import StellarBurgersData
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

class TestStellarBurgersTransit:
    def test_transit_personal_area(self, driver):
        driver.find_element(*StellarBurgersLocators.BUTTON_PERSONAL_AREA).click()
        WebDriverWait(driver,3).until(expected_conditions.presence_of_element_located(StellarBurgersLocators.BUTTON_AUTH))
        assert driver.current_url == settings.URL_log

    def test_transit_button_constructor(self, driver):
        driver.find_element(*StellarBurgersLocators.BUTTON_PERSONAL_AREA).click()
        WebDriverWait(driver,3).until(expected_conditions.presence_of_element_located(StellarBurgersLocators.BUTTON_AUTH))
        assert driver.current_url == settings.URL_log
        driver.find_element(*StellarBurgersLocators.BUTTON_CONSTRUCTOR).click()
        assert driver.current_url == settings.URL

    def test_transit_button_burger(self, driver):
        driver.find_element(*StellarBurgersLocators.BUTTON_PERSONAL_AREA).click()
        WebDriverWait(driver,3).until(expected_conditions.presence_of_element_located(StellarBurgersLocators.BUTTON_AUTH))
        assert driver.current_url == settings.URL_log
        driver.find_element(*StellarBurgersLocators.BUTTON_BURGER).click()
        assert driver.current_url == settings.URL
