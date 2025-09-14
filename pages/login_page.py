# # Ruta: C:\CURSO_TESTER_QA\Python_arcoiris-automation\pages\login_page.py
# # 140925 - 11:40  ######################
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.common.exceptions import TimeoutException
# import os
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
#         # Localizadores para los botones del modal
#         self.modal_accept_button = (By.CLASS_NAME, "swal2-confirm")
#         self.modal_cancel_button = (By.CLASS_NAME, "swal2-cancel")
#         self.modal_container = (By.CSS_SELECTOR, ".swal2-container")
#
#         # Localizadores para el menú y el enlace de perfil
#         self.hamburger_menu = (By.CSS_SELECTOR, 'div.menu-wrap input.toggler')
#         self.profile_link = (By.XPATH, "//a[@onclick=\"EnvioForm('Perfil')\"]")
#
#         # Nuevo localizador para el checkbox de suscripción
#         #self.subscription_checkbox = (By.ID, "fProCheck") NO funciona
#         self.subscription_checkbox = (By.CSS_SELECTOR, "label.switch")
#
#     def navigate(self):
#         """
#         Se navega a la página de inicio de sesión.
#         """
#         self.browser.get(self.url)
#
#     def enter_credentials(self, username, password):
#         """
#         Se ingresan las credenciales en los campos de usuario y contraseña.
#         """
#         self.browser.find_element(*self.username_field).send_keys(username)
#         self.browser.find_element(*self.password_field).send_keys(password)
#
#     def click_login_button(self):
#         """
#         Se hace clic en el botón de ingreso.
#         """
#         self.browser.find_element(*self.login_button).click()
#
#     def click_logout_arrow(self):
#         """
#         Se hace clic en la flecha para mostrar el modal de cerrar sesión.
#         """
#         WebDriverWait(self.browser, 10).until(
#             EC.element_to_be_clickable(self.logout_button)
#         ).click()
#
#     def accept_logout(self):
#         """
#         Se hace clic en el botón 'Aceptar' del modal de cerrar sesión
#         utilizando JavaScript para forzar el clic y se espera a que el
#         modal desaparezca.
#         """
#         try:
#             accept_button = WebDriverWait(self.browser, 10).until(
#                 EC.element_to_be_clickable(self.modal_accept_button)
#             )
#             self.browser.execute_script("arguments[0].click();", accept_button)
#             WebDriverWait(self.browser, 10).until(
#                 EC.invisibility_of_element_located(self.modal_container)
#             )
#         except TimeoutException:
#             raise TimeoutException("No se pudo hacer clic en el botón Aceptar o el modal no desapareció.")
#
#     def cancel_logout(self):
#         """
#         Se hace clic en el botón 'Cancelar' del modal de cerrar sesión
#         utilizando JavaScript para forzar el clic y se espera a que el
#         modal desaparezca.
#         """
#         try:
#             WebDriverWait(self.browser, 10).until(
#                 EC.visibility_of_element_located(self.modal_container)
#             )
#             cancel_button = WebDriverWait(self.browser, 10).until(
#                 EC.presence_of_element_located(self.modal_cancel_button)
#             )
#             self.browser.execute_script("arguments[0].click();", cancel_button)
#             WebDriverWait(self.browser, 10).until(
#                 EC.invisibility_of_element_located(self.modal_container)
#             )
#         except TimeoutException:
#             raise TimeoutException("No se pudo hacer clic en el botón Cancelar o el modal no desapareció.")
#
#     def click_hamburger_menu(self):
#         """
#         Se hace clic en el ícono del menú hamburguesa utilizando JavaScript
#         para evitar problemas de elementos cubiertos o de visibilidad.
#         """
#         element = WebDriverWait(self.browser, 20).until(
#             EC.presence_of_element_located(self.hamburger_menu)
#         )
#         self.browser.execute_script("arguments[0].click();", element)
#
#     def click_profile_link(self):
#         """
#         Se hace clic en el enlace "PERFIL" utilizando JavaScript para evitar
#         problemas de elementos interceptados o de sincronización.
#         """
#         element = WebDriverWait(self.browser, 10).until(
#             EC.presence_of_element_located(self.profile_link)
#         )
#         self.browser.execute_script("arguments[0].click();", element)
#
#     def click_subscription_checkbox(self):
#         """
#         Se hace clic en el checkbox de suscripción.
#         """
#         element = WebDriverWait(self.browser, 10).until(
#             EC.element_to_be_clickable(self.subscription_checkbox)
#         )
#         element.click()

# Ruta: C:\CURSO_TESTER_QA\Python_arcoiris-automation\pages\login_page.py
# 140925 - 17:15 ######################
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
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
        self.modal_accept_button = (By.CLASS_NAME, "swal2-confirm")
        self.modal_cancel_button = (By.CLASS_NAME, "swal2-cancel")
        self.modal_container = (By.CSS_SELECTOR, ".swal2-container")

        # Localizadores para el menú y el enlace de perfil
        self.hamburger_menu = (By.CSS_SELECTOR, 'div.menu-wrap input.toggler')
        self.profile_link = (By.XPATH, "//a[@onclick=\"EnvioForm('Perfil')\"]")

        # Nuevo localizador para el checkbox de suscripción usando el label.switch
        self.subscription_checkbox = (By.CSS_SELECTOR, "label.switch")

    def navigate(self):
        """
        Se navega a la página de inicio de sesión.
        """
        self.browser.get(self.url)

    def enter_credentials(self, username, password):
        """
        Se ingresan las credenciales en los campos de usuario y contraseña.
        """
        self.browser.find_element(*self.username_field).send_keys(username)
        self.browser.find_element(*self.password_field).send_keys(password)

    def click_login_button(self):
        """
        Se hace clic en el botón de ingreso.
        """
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
        Se hace clic en el botón 'Aceptar' del modal de cerrar sesión
        utilizando JavaScript para forzar el clic y se espera a que el
        modal desaparezca.
        """
        try:
            accept_button = WebDriverWait(self.browser, 10).until(
                EC.element_to_be_clickable(self.modal_accept_button)
            )
            self.browser.execute_script("arguments[0].click();", accept_button)
            WebDriverWait(self.browser, 10).until(
                EC.invisibility_of_element_located(self.modal_container)
            )
        except TimeoutException:
            raise TimeoutException("No se pudo hacer clic en el botón Aceptar o el modal no desapareció.")

    def cancel_logout(self):
        """
        Se hace clic en el botón 'Cancelar' del modal de cerrar sesión
        utilizando JavaScript para forzar el clic y se espera a que el
        modal desaparezca.
        """
        try:
            WebDriverWait(self.browser, 10).until(
                EC.visibility_of_element_located(self.modal_container)
            )
            cancel_button = WebDriverWait(self.browser, 10).until(
                EC.presence_of_element_located(self.modal_cancel_button)
            )
            self.browser.execute_script("arguments[0].click();", cancel_button)
            WebDriverWait(self.browser, 10).until(
                EC.invisibility_of_element_located(self.modal_container)
            )
        except TimeoutException:
            raise TimeoutException("No se pudo hacer clic en el botón Cancelar o el modal no desapareció.")

    def click_hamburger_menu(self):
        """
        Se hace clic en el ícono del menú hamburguesa utilizando JavaScript
        para evitar problemas de elementos cubiertos o de visibilidad.
        """
        element = WebDriverWait(self.browser, 20).until(
            EC.presence_of_element_located(self.hamburger_menu)
        )
        self.browser.execute_script("arguments[0].click();", element)

    def click_profile_link(self):
        """
        Se hace clic en el enlace "PERFIL" utilizando JavaScript para evitar
        problemas de elementos interceptados o de sincronización.
        """
        element = WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located(self.profile_link)
        )
        self.browser.execute_script("arguments[0].click();", element)

    def click_subscription_checkbox(self):
        """
        Se hace clic en el checkbox de suscripción.
        """
        element = WebDriverWait(self.browser, 10).until(
            EC.element_to_be_clickable(self.subscription_checkbox)
        )
        element.click()