from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


# Класс страницы авторизации
class LoginPageMesto:
    email_field = [By.ID, 'email']
    password_field = [By.ID, 'password']
    sign_in_button = [By.CLASS_NAME, 'auth-form__button']

    def __init__(self, driver):
        self.driver = driver

    def set_email(self, email):
        self.driver.find_element(*self.email_field).send_keys(email)

    def set_password(self, password):
        self.driver.find_element(*self.password_field).send_keys(password)

    def click_sign_in_button(self):
        self.driver.find_element(*self.sign_in_button).click()

    def login(self, email, password):
        self.set_email(email)
        self.set_password(password)
        self.click_sign_in_button()


# Класс главной страницы
class HomePageMesto:
    # создай локатор для поля «Занятие» в профиле пользователя
    profile_description = [By.ID, 'owner-description']

    def __init__(self, driver):
        self.driver = driver

    # метод ожидания загрузки страницы - ожидаем загрузку по появлению поля Занятие
    def wait_for_load_home_page(self):
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(self.profile_description))

    # метод для получения текстового значения поля «Занятие»
    def get_description(self):
        return self.driver.find_element(*self.profile_description).text


class TestPraktikum:
    driver = None

    @classmethod
    def setup_class(cls):
        # создали драйвер для браузера Chrome
        cls.driver = webdriver.Chrome()

    def test_get_description(self):
        # перешли на страницу тестового приложения
        self.driver.get('https://stellarburgers.nomoreparties.site/account/profile')

        # создай объект класса страницы авторизации
        loginpage = LoginPageMesto(self.driver)
        # выполнить авторизацию
        login_page.login('nadya_terekhina_5_123@yandex.ru', '123456')
        # создай объект класса главной страницы приложения
        home_page = HomePageMesto(self.driver)
        # дождись загрузки главной страницы
        home_page.wait_for_load_home_page()
        # сохрани в переменную description текстовое значение поля «Занятие»
        description = home_page.get_description()

        # проверь, через assert что полученное текстовое значение поля «Занятие» совпадает с ожидаемым
        assert description == "Занятие"

    @classmethod
    def teardown_class(cls):
        # закрыли браузер
        cls.driver.quit()
