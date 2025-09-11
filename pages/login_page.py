# Ruta: C:\CURSO_TESTER_QA\Python_arcoiris-automation\pages\login_page.py
from selenium.webdriver.common.by import By
import os

class LoginPage:
    def __init__(self, browser):
        self.browser = browser
        self.url = os.getenv("BASE_URL")
        self.username_field = (By.NAME, "OperadorCod")
        self.password_field = (By.NAME, "OpeClave")
        self.login_button = (By.CLASS_NAME, "BtnLogin")

    def navigate(self):
        """
        Se navega a la página de inicio de sesión.
        """
        self.browser.get(self.url)

    def login(self, username, password):
        """
        Se realiza el proceso de inicio de sesión.
        """
        self.browser.find_element(*self.username_field).send_keys(username)
        self.browser.find_element(*self.password_field).send_keys(password)
        self.browser.find_element(*self.login_button).click()