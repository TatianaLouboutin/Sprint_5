import time
import settings
from locators import StellarBurgersLocators
from data import StellarBurgersData
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from faker import Faker
from random import randint

class TestStellarBurgersRegistration:
    def test_registration_incorrecr_password(self, driver):
        driver.find_element(*StellarBurgersLocators.BUTTON_GO_TO_ACCOUNT).click()
        driver.find_element(*StellarBurgersLocators.LINK_REG).click()
        driver.find_element(*StellarBurgersLocators.REG_NAME).send_keys(StellarBurgersData.REG_NAME)
        driver.find_element(*StellarBurgersLocators.REG_EMAIL).send_keys(StellarBurgersData.REG_EMAIL)
        driver.find_element(*StellarBurgersLocators.REG_PASSWORD).send_keys(StellarBurgersData.REG_PASSWORD_INCORRECT)
        driver.find_element(*StellarBurgersLocators.BUTTON_REG).click()
        WebDriverWait(driver, 3).until(expected_conditions.presence_of_element_located(StellarBurgersLocators.PASSWORD_INCORRECT))
        assert driver.find_element(*StellarBurgersLocators.PASSWORD_INCORRECT).text == 'Некорректный пароль', 'Не нашел кнопку Оформить заказ'

    def test_registration_valid_data(self, driver):
        fake = Faker()
        name = fake.name()
        email = fake.email()
        password = fake.password(randint(6,10))
        driver.find_element(*StellarBurgersLocators.BUTTON_GO_TO_ACCOUNT).click()
        driver.find_element(*StellarBurgersLocators.LINK_REG).click()
        driver.find_element(*StellarBurgersLocators.REG_NAME).send_keys(name)
        driver.find_element(*StellarBurgersLocators.REG_EMAIL).send_keys(email)
        driver.find_element(*StellarBurgersLocators.REG_PASSWORD).send_keys(password)
        driver.find_element(*StellarBurgersLocators.BUTTON_REG).click()
        WebDriverWait(driver,3).until(expected_conditions.presence_of_element_located(StellarBurgersLocators.BUTTON_AUTH))
        assert driver.current_url == settings.URL_log

