# # Ruta: C:\CURSO_TESTER_QA\Python_arcoiris-automation\pages\login_page.py
# #130925 - 14:52 ######################
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
#         # Localizadores para los botones del modal
#         self.modal_accept_button = (By.CSS_SELECTOR, "button.swal2-confirm")
#         self.modal_cancel_button = (By.CSS_SELECTOR, "button.swal2-cancel")
#         self.modal_container = (By.CSS_SELECTOR, ".swal2-container")
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
#
#     def accept_logout(self):
#         """
#         Se hace clic en el botón 'Aceptar' del modal de cerrar sesión.
#         """
#         WebDriverWait(self.browser, 10).until(
#             EC.element_to_be_clickable(self.modal_accept_button)
#         ).click()
#
#     def cancel_logout(self):
#         """
#         Se hace clic en el botón 'Cancelar' del modal de cerrar sesión.
#         Se espera a que el modal sea visible antes de intentar hacer clic en el botón.
#         """
#         WebDriverWait(self.browser, 10).until(
#             EC.visibility_of_element_located(self.modal_container)
#         )
#         WebDriverWait(self.browser, 10).until(
#             EC.element_to_be_clickable(self.modal_cancel_button)
#         ).click()

# # Ruta: C:\CURSO_TESTER_QA\Python_arcoiris-automation\pages\login_page.py
# #130925 - 14:55 ######################


# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common.action_chains import ActionChains
# from selenium.common.exceptions import TimeoutException
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
#         # Localizadores para los botones del modal, se usan las clases directas
#         self.modal_accept_button = (By.CLASS_NAME, "swal2-confirm")
#         self.modal_cancel_button = (By.CLASS_NAME, "swal2-cancel")
#         self.modal_container = (By.CSS_SELECTOR, ".swal2-container")
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
#         Se hace clic en el botón 'Aceptar' del modal de cerrar sesión.
#         """
#         WebDriverWait(self.browser, 10).until(
#             EC.element_to_be_clickable(self.modal_accept_button)
#         ).click()
#
#     def cancel_logout(self):
#         """
#         Se hace clic en el botón 'Cancelar' del modal de cerrar sesión.
#         Se utiliza ActionChains para evitar problemas de sincronización,
#         y se espera a que el modal desaparezca.
#         """
#         try:
#             # Se espera a que el botón esté visible en el DOM.
#             cancel_button = WebDriverWait(self.browser, 10).until(
#                 EC.visibility_of_element_located(self.modal_cancel_button)
#             )
#
#             # Se utiliza ActionChains para mover el cursor y hacer clic.
#             ActionChains(self.browser).move_to_element(cancel_button).click().perform()
#
#             # Se espera a que la ventana modal desaparezca.
#             WebDriverWait(self.browser, 10).until(
#                 EC.invisibility_of_element_located(self.modal_container)
#             )
#         except TimeoutException:
#             raise TimeoutException("No se pudo hacer clic en el botón Cancelar o el modal no desapareció.")

# # Ruta: C:\CURSO_TESTER_QA\Python_arcoiris-automation\pages\login_page.py
# #130925 - 15:05 ######################
#
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common.action_chains import ActionChains
# from selenium.common.exceptions import TimeoutException
# import os
#
#
# class LoginPage:
#     def __init__(self, browser):
#         self.browser = browser
#         self.browser = browser
#         self.url = os.getenv("BASE_URL")
#         self.username_field = (By.NAME, "OperadorCod")
#         self.password_field = (By.NAME, "OpeClave")
#         self.login_button = (By.CLASS_NAME, "BtnLogin")
#
#         # Localizador para el botón de cerrar sesión (la flecha)
#         self.logout_button = (By.CSS_SELECTOR, 'div[title="Cerrar Sesión"]')
#
#         # Localizadores para los botones del modal, se usan las clases directas
#         self.modal_accept_button = (By.CLASS_NAME, "swal2-confirm")
#         self.modal_cancel_button = (By.CLASS_NAME, "swal2-cancel")
#         self.modal_container = (By.CSS_SELECTOR, ".swal2-container")
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
#         Se hace clic en el botón 'Aceptar' del modal de cerrar sesión.
#         Se utiliza ActionChains para evitar problemas de sincronización,
#         y se espera a que el modal desaparezca.
#         """
#         try:
#             # Se espera a que el botón esté visible en el DOM.
#             accept_button = WebDriverWait(self.browser, 10).until(
#                 EC.visibility_of_element_located(self.modal_accept_button)
#             )
#
#             # Se utiliza ActionChains para mover el cursor y hacer clic.
#             ActionChains(self.browser).move_to_element(accept_button).click().perform()
#
#             # Se espera a que la ventana modal desaparezca.
#             WebDriverWait(self.browser, 10).until(
#                 EC.invisibility_of_element_located(self.modal_container)
#             )
#         except TimeoutException:
#             raise TimeoutException("No se pudo hacer clic en el botón Aceptar o el modal no desapareció.")
#
#     def cancel_logout(self):
#         """
#         Se hace clic en el botón 'Cancelar' del modal de cerrar sesión.
#         Se utiliza ActionChains para evitar problemas de sincronización,
#         y se espera a que el modal desaparezca.
#         """
#         try:
#             # Se espera a que el botón esté visible en el DOM.
#             cancel_button = WebDriverWait(self.browser, 10).until(
#                 EC.visibility_of_element_located(self.modal_cancel_button)
#             )
#
#             # Se utiliza ActionChains para mover el cursor y hacer clic.
#             ActionChains(self.browser).move_to_element(cancel_button).click().perform()
#
#             # Se espera a que la ventana modal desaparezca.
#             WebDriverWait(self.browser, 10).until(
#                 EC.invisibility_of_element_located(self.modal_container)
#             )
#         except TimeoutException:
#             raise TimeoutException("No se pudo hacer clic en el botón Cancelar o el modal no desapareció.")

# # Ruta: C:\CURSO_TESTER_QA\Python_arcoiris-automation\pages\login_page.py
# #130925 - 15:30 ######################
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.common.exceptions import TimeoutException
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
#         # Localizadores para los botones del modal
#         self.modal_accept_button = (By.CLASS_NAME, "swal2-confirm")
#         self.modal_cancel_button = (By.CLASS_NAME, "swal2-cancel")
#         self.modal_container = (By.CSS_SELECTOR, ".swal2-container")
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
#                 EC.visibility_of_element_located(self.modal_accept_button)
#             )
#             # Se usa JavaScript para forzar el clic
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
#             cancel_button = WebDriverWait(self.browser, 10).until(
#                 EC.visibility_of_element_located(self.modal_cancel_button)
#             )
#             # Se usa JavaScript para forzar el clic
#             self.browser.execute_script("arguments[0].click();", cancel_button)
#             WebDriverWait(self.browser, 10).until(
#                 EC.invisibility_of_element_located(self.modal_container)
#             )
#         except TimeoutException:
#             raise TimeoutException("No se pudo hacer clic en el botón Cancelar o el modal no desapareció.")

# # Ruta: C:\CURSO_TESTER_QA\Python_arcoiris-automation\pages\login_page.py
# #130925 - 15:50 ######################
#
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
#             # Se usa JavaScript para forzar el clic
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
#             # Se espera a que el botón Cancelar esté presente en el DOM
#             cancel_button = WebDriverWait(self.browser, 10).until(
#                 EC.presence_of_element_located(self.modal_cancel_button)
#             )
#             # Se usa JavaScript para forzar el clic
#             self.browser.execute_script("arguments[0].click();", cancel_button)
#             WebDriverWait(self.browser, 10).until(
#                 EC.invisibility_of_element_located(self.modal_container)
#             )
#         except TimeoutException:
#             raise TimeoutException("No se pudo hacer clic en el botón Cancelar o el modal no desapareció.")

# # Ruta: C:\CURSO_TESTER_QA\Python_arcoiris-automation\pages\login_page.py
# #130925 - 16:00  ######################

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
            # Se usa JavaScript para forzar el clic
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
            # Se espera a que el modal y el botón 'Cancelar' estén visibles para una interacción segura.
            WebDriverWait(self.browser, 10).until(
                EC.visibility_of_element_located(self.modal_container)
            )
            cancel_button = WebDriverWait(self.browser, 10).until(
                EC.presence_of_element_located(self.modal_cancel_button)
            )
            # Se usa JavaScript para forzar el clic
            self.browser.execute_script("arguments[0].click();", cancel_button)
            WebDriverWait(self.browser, 10).until(
                EC.invisibility_of_element_located(self.modal_container)
            )
        except TimeoutException:
            raise TimeoutException("No se pudo hacer clic en el botón Cancelar o el modal no desapareció.")

