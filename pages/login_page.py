# # Ruta: C:\CURSO_TESTER_QA\Python_arcoiris-automation\pages\login_page.py
#130925 - 10:20 ######################
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# import os
#
#
# class LoginPage:
#     def __init__(self, browser):
#         self.browser = browser
#         self.url = os.getenv("BASE_URL")
#         self.username_field = (By.NAME, "OperadorCod")
#         self.password_field = (By.NAME, "OpeClave")
#         self.login_button = (By.CLASS_NAME, "BtnLogin")
#
#         # Localizador para el botón de cerrar sesión (la flecha)
#         self.logout_button = (By.CSS_SELECTOR, 'div[title="Cerrar Sesión"]')
#
#     def navigate(self):
#         """
#         Se navega a la página de inicio de sesión.
#         """
#         self.browser.get(self.url)
#
#     def login(self, username, password):
#         """
#         Se realiza el proceso de inicio de sesión.
#         """
#         self.browser.find_element(*self.username_field).send_keys(username)
#         self.browser.find_element(*self.password_field).send_keys(password)
#         self.browser.find_element(*self.login_button).click()
#
#     def click_logout_arrow(self):
#         """
#         Se hace clic en la flecha para mostrar el modal de cerrar sesión.
#         """
#         WebDriverWait(self.browser, 10).until(
#             EC.element_to_be_clickable(self.logout_button)
#         ).click()
#--------------------------------------------------------------------------
# Ruta: C:\CURSO_TESTER_QA\Python_arcoiris-automation\pages\login_page.py
#130925 - 10:22 ######################
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os


class LoginPage:
    def __init__(self, browser):
        self.browser = browser
        self.url = os.getenv("BASE_URL")
        self.username_field = (By.NAME, "OperadorCod")
        self.password_field = (By.NAME, "OpeClave")
        self.login_button = (By.CLASS_NAME, "BtnLogin")

        # Localizador para el botón de cerrar sesión (la flecha)
        self.logout_button = (By.CSS_SELECTOR, 'div[title="Cerrar Sesión"]')

        # Localizadores para los botones del modal
        self.modal_accept_button = (By.CSS_SELECTOR, "button.swal2-confirm")
        self.modal_cancel_button = (By.CSS_SELECTOR, "button.swal2-cancel")
        self.modal_container = (By.CSS_SELECTOR, ".swal2-container")

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

    def click_logout_arrow(self):
        """
        Se hace clic en la flecha para mostrar el modal de cerrar sesión.
        """
        WebDriverWait(self.browser, 10).until(
            EC.element_to_be_clickable(self.logout_button)
        ).click()

    def accept_logout(self):
        """
        Se hace clic en el botón 'Aceptar' del modal de cerrar sesión.
        """
        WebDriverWait(self.browser, 10).until(
            EC.element_to_be_clickable(self.modal_accept_button)
        ).click()

    def cancel_logout(self):
        """
        Se hace clic en el botón 'Cancelar' del modal de cerrar sesión.
        Se espera a que el modal sea visible antes de intentar hacer clic en el botón.
        """
        WebDriverWait(self.browser, 10).until(
            EC.visibility_of_element_located(self.modal_container)
        )
        WebDriverWait(self.browser, 10).until(
            EC.element_to_be_clickable(self.modal_cancel_button)
        ).click()