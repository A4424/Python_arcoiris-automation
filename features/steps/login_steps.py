# # # Ruta: C:\CURSO_TESTER_QA\Python_arcoiris-automation\features\steps\login_steps.py
# # from behave import given, when, then
# # from pages.login_page import LoginPage
# # from selenium.webdriver.support import expected_conditions as EC
# # from selenium.webdriver.support.ui import WebDriverWait
# # from selenium.webdriver.common.by import By
# # from selenium.common.exceptions import TimeoutException
# # import os
# #
# #
# # @given("Se esta en la pagina de inicio de sesion")
# # def step_impl(context):
# #     """
# #     Se inicializa la pagina de login y se navega a la URL.
# #     """
# #     context.login_page = LoginPage(context.browser)
# #     context.login_page.navigate()
# #
# #
# # # Nuevo paso para usar variables de entorno
# # @when('Se ingresan las credenciales validas')
# # def step_impl(context):
# #     """
# #     Se obtienen las credenciales desde el archivo .env y se ingresan.
# #     """
# #     username = os.getenv("VALID_USERNAME")
# #     password = os.getenv("VALID_PASSWORD")
# #     context.login_page.login(username, password)
# #
# #
# # # Paso anterior para credenciales invalidas, se puede mantener si se desea
# # @when('Se ingresan el nombre de usuario "{username}" y la contrasena "{password}"')
# # def step_impl(context, username, password):
# #     """
# #     Se ingresan las credenciales proporcionadas.
# #     """
# #     context.login_page.login(username, password)
# #
# #
# # @when("Se hace clic en el boton de Ingresar")
# # def step_impl(context):
# #     """
# #     Se hace clic en el boton de login.
# #     """
# #     pass
# #
# #
# # @then("Se es redirigido a la pagina de inicio")
# # def step_impl(context):
# #     """
# #     Se verifica que la URL actual sea la esperada.
# #     """
# #     try:
# #         wait = WebDriverWait(context.browser, 10)
# #         wait.until(EC.invisibility_of_element_located(context.login_page.login_button))
# #
# #         print(f"Redireccion exitosa. URL actual: {context.browser.current_url}")
# #
# #     except TimeoutException:
# #         assert False, "No se produjo una redireccion despues de iniciar sesion. La URL no cambio."
# #
# #
# # @then("Se muestra un mensaje de error de credenciales invalidas")
# # def step_impl(context):
# #     """
# #     Se verifica la visibilidad y el contenido del mensaje de error.
# #     """
# #     error_message_locator = (By.ID, "swal2-title")
# #
# #     try:
# #         wait = WebDriverWait(context.browser, 10)
# #         error_message_element = wait.until(EC.visibility_of_element_located(error_message_locator))
# #
# #         expected_text = "Error!"
# #
# #         assert expected_text in error_message_element.text, f"El mensaje de error no es el esperado. Se encontro: {error_message_element.text}"
# #
# #         print(f"Mensaje de error validado: {error_message_element.text}")
# #
# #     except TimeoutException:
# #         assert False, "El mensaje de error no fue visible en el tiempo de espera."
#
# # Ruta: C:\CURSO_TESTER_QA\Python_arcoiris-automation\features\steps\login_steps.py
# from behave import given, when, then
# from pages.login_page import LoginPage
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.common.by import By
# from selenium.common.exceptions import TimeoutException
# import os
#
#
# @given("Se esta en la pagina de inicio de sesion")
# def step_impl(context):
#     """
#     Se inicializa la pagina de login y se navega a la URL.
#     """
#     context.login_page = LoginPage(context.browser)
#     context.login_page.navigate()
#
#
# @when('Se ingresan las credenciales validas')
# def step_impl(context):
#     """
#     Se obtienen las credenciales desde el archivo .env y se ingresan.
#     """
#     username = os.getenv("VALID_USERNAME")
#     password = os.getenv("VALID_PASSWORD")
#     context.login_page.login(username, password)
#
#
# @when('Se ingresan el nombre de usuario "{username}" y la contrasena "{password}"')
# def step_impl(context, username, password):
#     """
#     Se ingresan las credenciales proporcionadas.
#     """
#     context.login_page.login(username, password)
#
#
# @when("Se hace clic en el boton de Ingresar")
# def step_impl(context):
#     """
#     Se hace clic en el boton de login.
#     """
#     pass
#
#
# @then("Se es redirigido a la pagina de inicio")
# def step_impl(context):
#     """
#     Se verifica que la URL actual sea la de la página de inicio.
#     """
#     try:
#         wait = WebDriverWait(context.browser, 10)
#         # Se espera a que el boton de login ya no sea visible, lo que implica que se ha navegado fuera de la página de login.
#         wait.until(EC.invisibility_of_element_located(context.login_page.login_button))
#
#         # Opcional: Se puede agregar una espera a un elemento de la página de destino para mayor robustez
#         # wait.until(EC.visibility_of_element_located((By.ID, "main-dashboard")))
#
#         print(f"Redireccion exitosa. URL actual: {context.browser.current_url}")
#
#     except TimeoutException:
#         assert False, "No se produjo una redireccion a la pagina de inicio."
#
#
# @then("Se muestra un mensaje de error de credenciales invalidas")
# def step_impl(context):
#     """
#     Se verifica la visibilidad y el contenido del mensaje de error.
#     """
#     error_message_locator = (By.ID, "swal2-title")
#
#     try:
#         wait = WebDriverWait(context.browser, 10)
#         error_message_element = wait.until(EC.visibility_of_element_located(error_message_locator))
#
#         expected_text = "Error!"
#
#         assert expected_text in error_message_element.text, f"El mensaje de error no es el esperado. Se encontro: {error_message_element.text}"
#
#         print(f"Mensaje de error validado: {error_message_element.text}")
#
#     except TimeoutException:
#         assert False, "El mensaje de error no fue visible en el tiempo de espera."

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


# El paso para el Scenario Outline
@when('Se ingresa el usuario "{username}" y la contrasena "{password}"')
def step_impl(context, username, password):
    """
    Se ingresan el usuario y la contrasena proporcionados en el escenario.
    """
    # En este punto, las variables 'username' y 'password' provienen del Scenario Outline
    context.login_page.login(username, password)


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


@then("Se muestra un mensaje de error de credenciales invalidas")
def step_impl(context):
    """
    Se verifica la visibilidad y el contenido del mensaje de error.
    """
    error_message_locator = (By.ID, "swal2-title")

    try:
        wait = WebDriverWait(context.browser, 10)
        error_message_element = wait.until(EC.visibility_of_element_located(error_message_locator))

        expected_text = "Error!"

        assert expected_text in error_message_element.text, f"El mensaje de error no es el esperado. Se encontro: {error_message_element.text}"

        print(f"Mensaje de error validado: {error_message_element.text}")

    except TimeoutException:
        assert False, "El mensaje de error no fue visible en el tiempo de espera."