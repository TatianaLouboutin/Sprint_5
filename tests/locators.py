from selenium.webdriver.common.by import By


class StellarBurgersLocators:

    BUTTON_GO_TO_ACCOUNT = (By.XPATH, ".//button[text()='Войти в аккаунт']")   # Кнопка Войти в аккаунт
    BUTTON_AUTH = (By.XPATH, ".//button[text()='Войти']")                      # Кнопка Войти
    BUTTON_REG = (By.XPATH, ".//button[text()='Зарегистрироваться']")          # Кнопка Зарегистрироваться
    BUTTON_PERSONAL_AREA = (By.XPATH, ".//p[text()='Личный Кабинет']")         # Кнопка Личный кабинет
    BUTTON_CONSTRUCTOR = (By.XPATH, ".//p[text()='Конструктор']")              # Кнопка Конструктор
    BUTTON_BURGER =  (By.XPATH, ".//div[@class='AppHeader_header__logo__2D0X2']/a/*")   # Кнопка Бургер
    BUTTON_CREATE_ORDER = (By.XPATH, ".//button[text()='Оформить заказ']")     # Кнопка Оформить заказ
    BUTTON_LOGOUT = (By.XPATH, ".//button[text()='Выход']")                    # Кнопка разлогина


    AUTH_EMAIL = (By.XPATH, ".//input[@name='name']")                           # Поле ввода логина
    AUTH_PASSWORD = (By.XPATH, ".//input[@name='Пароль']")                      # Поле ввода пароля

    PASSWORD_INCORRECT = (By.XPATH, ".//p[text()='Некорректный пароль']")       # Ошибка: Пароль некорректный

    LINK_REG = (By.XPATH, ".//a[text() = 'Зарегистрироваться']")                # Ссылка Зарегистрироваться
    LINK_RECOVER_PASSWORD = (By.XPATH, ".//a[text() = 'Восстановить пароль']")  # Ссылка Восстановить пароль
    LINK_AUTH = (By.XPATH, ".//a[text() = 'Войти']")                            # Ссылка Войти

    REG_NAME = (By.XPATH, ".//label[text()='Имя']/parent::*/input")             # Поле ввода Имя
    REG_EMAIL = (By.XPATH, ".//label[text()='Email']/parent::*/input")          # Поле ввода Логина
    REG_PASSWORD = (By.XPATH, ".//input[@name='Пароль']")                       # Поле ввода Пароля

    SOUCES = (By.XPATH, ".//span[text()='Соусы']")                              # Раздел Соусы
    BULKI = (By.XPATH, ".//span[text()='Булки']")                               # Раздел Булки
    FILLINGS = (By.XPATH, ".//span[text()='Начинки']")                          # Раздел Начинки

    SOUCES_NAME = (By.XPATH, ".//img[@alt='Соус фирменный Space Sauce']")      # Картинка соуса
    FILLINGS_NAME = (By.XPATH, ".//img[@alt='Филе Люминесцентного тетраодонтимформа']") # Картинка начинки
    BULKI_NAME = (By.XPATH, ".//img[@alt='Краторная булка N-200i']")           # Картинка булки