import time
import settings
from locators import StellarBurgersLocators
from data import StellarBurgersData
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


class TestStellarBurgersLogout:
    def test_logout(self, driver):
        driver.find_element(*StellarBurgersLocators.BUTTON_GO_TO_ACCOUNT).click()
        driver.find_element(*StellarBurgersLocators.AUTH_EMAIL).send_keys(StellarBurgersData.AUTH_EMAIL)
        driver.find_element(*StellarBurgersLocators.AUTH_PASSWORD).send_keys(StellarBurgersData.AUTH_PASSWORD)
        driver.find_element(*StellarBurgersLocators.BUTTON_AUTH).click()
        time.sleep(3)
        assert driver.find_element(*StellarBurgersLocators.BUTTON_CREATE_ORDER).text == 'Оформить заказ', 'Не нашел кнопку Оформить заказ'

        driver.find_element(*StellarBurgersLocators.BUTTON_PERSONAL_AREA).click()
        time.sleep(3)
        driver.find_element(*StellarBurgersLocators.BUTTON_LOGOUT).click()
        time.sleep(3)
        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/login'