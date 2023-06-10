from selenium.webdriver.common.by import By


class RegistrationPageMesto:
    # локатор поля «Email»
    email_field = [By.ID, 'email']
    # локатор поля «Пароль»
    password_field = [By.ID, 'password']
    # локатор кнопки "Зарегистрироваться"
    registration_button = [By.CLASS_NAME, 'auth-form__button']

    # конструктор класса
    def __init__(self, driver):
        self.driver = driver

    # метод заполняет поле «Email»
    def set_email(self, email_value):
        self.driver.find_element(*self.email_field).send_keys(email_value)

    # метод заполняет поля «Пароль»
    def set_password(self, password_value):
        self.driver.find_element(*self.email_field).send_keys(password_value)

    # метод кликает по кнопке «Зарегистрироваться»
    def click_registration_button(self):
        self.driver.find_element(*self.registration_button).click()

    # метод регистрации в приложении: объединяет ввод email-а, пароля и клик по кнопке «Зарегистрироваться»
    def register(self, email_value, password_value):
        self.set_email(email_value)
        self.set_password(password_value)
        self.click_registration_button()