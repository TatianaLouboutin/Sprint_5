import time
import settings
from locators import StellarBurgersLocators
from data import StellarBurgersData
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


class TestAuthenticationStellarBurgers:
    def test_auth_personal_area(self, driver):
        driver.find_element(*StellarBurgersLocators.BUTTON_PERSONAL_AREA).click()
        driver.find_element(*StellarBurgersLocators.AUTH_EMAIL).send_keys(StellarBurgersData.AUTH_EMAIL)
        driver.find_element(*StellarBurgersLocators.AUTH_PASSWORD).send_keys(StellarBurgersData.AUTH_PASSWORD)
        driver.find_element(*StellarBurgersLocators.BUTTON_AUTH).click()
        WebDriverWait(driver,3).until(expected_conditions.presence_of_element_located(StellarBurgersLocators.BUTTON_CREATE_ORDER))
        assert driver.find_element(*StellarBurgersLocators.BUTTON_CREATE_ORDER).text == 'Оформить заказ', 'Не нашел кнопку Оформить заказ'

    def test_auth_button_go_in_to_account(self, driver):
        driver.find_element(*StellarBurgersLocators.BUTTON_GO_TO_ACCOUNT).click()
        driver.find_element(*StellarBurgersLocators.AUTH_EMAIL).send_keys(StellarBurgersData.AUTH_EMAIL)
        driver.find_element(*StellarBurgersLocators.AUTH_PASSWORD).send_keys(StellarBurgersData.AUTH_PASSWORD)
        driver.find_element(*StellarBurgersLocators.BUTTON_AUTH).click()
        WebDriverWait(driver,3).until(expected_conditions.presence_of_element_located(StellarBurgersLocators.BUTTON_CREATE_ORDER))
        assert driver.find_element(*StellarBurgersLocators.BUTTON_CREATE_ORDER).text == 'Оформить заказ', 'Не нашел кнопку Оформить заказ'

    def test_auth_link_auth(self, driver):
        driver.find_element(*StellarBurgersLocators.BUTTON_GO_TO_ACCOUNT).click()
        driver.find_element(*StellarBurgersLocators.LINK_REG).click()
        driver.find_element(*StellarBurgersLocators.LINK_AUTH).click()
        driver.find_element(*StellarBurgersLocators.AUTH_EMAIL).send_keys(StellarBurgersData.AUTH_EMAIL)
        driver.find_element(*StellarBurgersLocators.AUTH_PASSWORD).send_keys(StellarBurgersData.AUTH_PASSWORD)
        driver.find_element(*StellarBurgersLocators.BUTTON_AUTH).click()
        WebDriverWait(driver,3).until(expected_conditions.presence_of_element_located(StellarBurgersLocators.BUTTON_CREATE_ORDER))
        assert driver.find_element(*StellarBurgersLocators.BUTTON_CREATE_ORDER).text == 'Оформить заказ', 'Не нашел кнопку Оформить заказ'

    def test_auth_recovery_link(self, driver):
        driver.find_element(*StellarBurgersLocators.BUTTON_GO_TO_ACCOUNT).click()
        driver.find_element(*StellarBurgersLocators.LINK_RECOVER_PASSWORD).click()
        driver.find_element(*StellarBurgersLocators.LINK_AUTH).click()
        driver.find_element(*StellarBurgersLocators.AUTH_EMAIL).send_keys(StellarBurgersData.AUTH_EMAIL)
        driver.find_element(*StellarBurgersLocators.AUTH_PASSWORD).send_keys(StellarBurgersData.AUTH_PASSWORD)
        driver.find_element(*StellarBurgersLocators.BUTTON_AUTH).click()
        WebDriverWait(driver,3).until(expected_conditions.presence_of_element_located(StellarBurgersLocators.BUTTON_CREATE_ORDER))
        assert driver.find_element(*StellarBurgersLocators.BUTTON_CREATE_ORDER).text == 'Оформить заказ', 'Не нашел кнопку Оформить заказ'