# Ruta: C:\CURSO_TESTER_QA\Python_arcoiris-automation\pages\login_page.py
# 150925 - 14:30
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

        # Localizador para el checkbox de suscripción usando el label.switch
        self.subscription_checkbox = (By.CSS_SELECTOR, "label.switch")

        # Localizadores para la seccion de canje de puntos
        self.prizes_button = (By.XPATH, "//div[text()='Premios']")
        # Localizador de la lista desplegable por su ID.
        self.branch_dropdown = (By.ID, "FSuc")

       # self.redeem_button_modal = (By.XPATH, "//button[text()='CANJEAR']") ------------------------------------
        self.redeem_button_modal = (By.XPATH, '//*[@id="Div"]/div/div[2]/div')

        #self.summary_message = (By.XPATH, "//div[text()='¡Felicitaciones! Tu premio fue reservado con exito']")
        self.summary_message = (By.XPATH, "//div[@id='swal2-html-container' and text()='¡Felicitaciones! Tu premio fue reservado con exito']")
        #self.summary_message = (By.ID, "swal2-html-container")
        #self.summary_message = (By.ID, "swal2-html-container")
        #self.summary_message = (By.XPATH, "/html/body/div[6]/div")


        #self.volver_button = (By.XPATH, "//button[text()='VOLVER']") -----------------------------------
        self.volver_button = (By.XPATH, "//*[@id='Principal2']/div/div[6]/input")

        # Localizadores para el canje con puntos insuficientes
        self.modal_insufficient_points_message = (By.XPATH, "//div[@id='swal2-html-container' and text()='Tus puntos aún no son suficientes']")


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

    # Métodos para el canje de puntos
    def click_prizes_button(self):
        """
        Se hace clic en el botón 'Premios' de la página de inicio.
        """
        WebDriverWait(self.browser, 10).until(
            EC.element_to_be_clickable(self.prizes_button)
        ).click()

    def select_branch(self, branch_name):
        """
        Se selecciona la sucursal del menú desplegable.
        """
        # Se hace clic en el dropdown para abrir el menu de opciones
        WebDriverWait(self.browser, 10).until(
            EC.element_to_be_clickable(self.branch_dropdown)
        ).click()

        # Se construye un localizador dinámico para la opción de la sucursal
        branch_option = (By.XPATH, f"//option[text()='{branch_name}']")

        # Se hace clic en la opción de sucursal deseada
        WebDriverWait(self.browser, 10).until(
            EC.element_to_be_clickable(branch_option)
        ).click()

    def click_product_ver_button(self):
        """
        Se hace clic en el botón 'VER' del producto especificado.
        """
        # Se usa un localizador para el botón VER. Se espera que el elemento sea visible y clicable.
        product_ver_button = (By.XPATH, '//*[@id="Agrega"]')
        WebDriverWait(self.browser, 10).until(
            EC.element_to_be_clickable(product_ver_button)
        ).click()




    def click_redeem_button_modal(self):
        """
        Se hace clic en el botón 'CANJEAR' del modal.
        """
        WebDriverWait(self.browser, 10).until(
            EC.element_to_be_clickable(self.redeem_button_modal)
        ).click()

    def click_accept_button_modal(self):
        """
        Se hace clic en el botón 'ACEPTAR' del modal de confirmación.
        """
        WebDriverWait(self.browser, 10).until(
            EC.element_to_be_clickable(self.modal_accept_button)
        ).click()

    # def get_summary_message(self):
    #     """
    #     Se obtiene el mensaje de confirmación del canje.
    #     """
    #     return WebDriverWait(self.browser, 10).until(
    #         EC.visibility_of_element_located(self.summary_message)
    #     ).text

    def get_summary_message(self):
        try:
            element = WebDriverWait(self.browser, 20).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, "selector_del_modal"))
            )
            return element.text
        except TimeoutException:
            print("❌ El modal de confirmación no apareció dentro del tiempo esperado")
            return None


    def click_volver_button(self):
        """
        Se hace clic en el botón 'VOLVER' del modal de resumen.
        """
        WebDriverWait(self.browser, 10).until(
            EC.element_to_be_clickable(self.volver_button)
        ).click()

    def click_ok_button_modal(self):
        """
        Se hace clic en el botón 'OK' del modal de canje fallido.
        """
        WebDriverWait(self.browser, 10).until(
            EC.element_to_be_clickable(self.modal_accept_button)
        ).click()

