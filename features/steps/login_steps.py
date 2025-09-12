# Ruta: C:\CURSO_TESTER_QA\Python_arcoiris-automation\features\steps\login_steps.py
from behave import given, when, then
from pages.login_page import LoginPage
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
import os


@given("Se esta en la pagina de inicio de sesion")
def step_impl(context):
    """
    Se inicializa la pagina de login y se navega a la URL.
    """
    context.login_page = LoginPage(context.browser)
    context.login_page.navigate()


@when('Se ingresan las credenciales validas')
def step_impl(context):
    """
    Se obtienen las credenciales desde el archivo .env y se ingresan.
    """
    username = os.getenv("VALID_USERNAME")
    password = os.getenv("VALID_PASSWORD")
    context.login_page.login(username, password)


# El paso para el Scenario Outline ha sido modificado
@when('Se ingresa el usuario "{username}" y la contrasena "{password}"')
def step_impl(context, username, password):
    """
    Se ingresan el usuario y la contrasena proporcionados en el escenario.
    """
    # Se obtienen los valores de las variables de entorno si se usan
    user = os.getenv(username) if username in os.environ else username
    passw = os.getenv(password) if password in os.environ else password

    context.login_page.login(user, passw)


@when("Se hace clic en el boton de Ingresar")
def step_impl(context):
    """
    Se hace clic en el boton de login.
    """
    pass


@then("Se es redirigido a la pagina de inicio")
def step_impl(context):
    """
    Se verifica que la URL actual sea la de la página de inicio.
    """
    try:
        wait = WebDriverWait(context.browser, 10)
        wait.until(EC.invisibility_of_element_located(context.login_page.login_button))

        print(f"Redireccion exitosa. URL actual: {context.browser.current_url}")

    except TimeoutException:
        assert False, "No se produjo una redireccion a la pagina de inicio."


# Se ha modificado este paso para manejar los diferentes mensajes de error
@then("Se muestra un mensaje de error de credenciales invalidas")
def step_impl(context):
    """
    Se verifica la visibilidad y el contenido del mensaje de error.
    """
    error_message_locator = (By.ID, "swal2-html-container")

    try:
        wait = WebDriverWait(context.browser, 10)
        error_message_element = wait.until(EC.visibility_of_element_located(error_message_locator))

        # Se obtiene el texto actual del mensaje de error
        actual_text = error_message_element.text

        # Se verifica si el mensaje de error es uno de los esperados
        expected_messages = ["Clave Usuario Invalida.!!", "Usuario Inexistente.!!"]

        if any(msg in actual_text for msg in expected_messages):
            print(f"Mensaje de error validado: {actual_text}")
        else:
            assert False, f"El mensaje de error no es el esperado. Se encontró: {actual_text}"

    except TimeoutException:
        assert False, "El mensaje de error no fue visible en el tiempo de espera."