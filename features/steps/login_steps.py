from behave import given, when, then
from pages.login_page import LoginPage
from selenium.webdriver.common.by import By
import os


@given("Se esta en la pagina de inicio de sesion")
def step_given_on_login_page(context):
    """
    Navega a la página de inicio de sesión.
    """
    context.login_page = LoginPage(context.browser)
    context.login_page.navigate()


@when("Se ingresan las credenciales validas")
def step_when_enter_valid_credentials(context):
    """
    Ingresa las credenciales válidas del archivo .env.
    """
    username = os.getenv("VALID_USERNAME")
    password = os.getenv("VALID_PASSWORD")
    context.login_page.login(username, password)


@when('Se ingresa el usuario "{username}" y la contrasena "{password}"')
def step_when_enter_invalid_credentials(context, username, password):
    """
    Ingresa las credenciales provistas por el Scenario Outline.
    """
    # Si las credenciales son vacías, no se hace nada en el campo.
    if username != '""':
        username_value = os.getenv(username, username)
    else:
        username_value = ""

    if password != '""':
        password_value = os.getenv(password, password)
    else:
        password_value = ""

    context.login_page.login(username_value, password_value)


@when("Se hace clic en el boton de Ingresar")
def step_when_click_login_button(context):
    """
    Hace clic en el botón de inicio de sesión.
    """
    context.login_page.browser.find_element(*context.login_page.login_button).click()


@then("Se es redirigido a la pagina de inicio")
def step_then_redirected_to_home_page(context):
    """
    Verifica que la URL de la página de inicio sea la correcta.
    """
    expected_url = f"{context.login_page.url}Index.aspx"
    current_url = context.login_page.browser.current_url
    assert current_url == expected_url, \
        f"Se esperaba la URL '{expected_url}' pero se obtuvo '{current_url}'"


@then("Se muestra un mensaje de error de credenciales invalidas")
def step_then_show_invalid_credentials_error_message(context):
    """
    Verifica que aparezca el mensaje de credenciales inválidas.
    """
    try:
        error_message_element = context.browser.find_element(By.ID, "lblmensaje")
        assert "Usuario Inexistente!!" in error_message_element.text or \
               "Clave Invalida!!" in error_message_element.text, \
            "El mensaje de error no coincide con el esperado."
    except Exception as e:
        assert False, f"No se pudo encontrar el elemento o validar el mensaje. Error: {e}"


@then("Se muestra el mensaje de campo requerido")
def step_then_show_required_field_message(context):
    """
    Verifica que el mensaje de 'Completa este campo' sea visible.
    """
    try:
        # Se verifica si los campos están vacíos
        username_input = context.browser.find_element(*context.login_page.username_field)
        password_input = context.browser.find_element(*context.login_page.password_field)

        # Se simula el envío del formulario para que aparezcan los mensajes de validación
        context.login_page.browser.find_element(*context.login_page.login_button).click()

        # Se obtienen los mensajes de validación de los campos
        username_message = context.browser.execute_script("return arguments[0].validationMessage;", username_input)
        password_message = context.browser.execute_script("return arguments[0].validationMessage;", password_input)

        # Se verifica que al menos uno de los campos tiene el mensaje de validación
        assert username_message == "Completa este campo." or password_message == "Completa este campo.", \
            f"El mensaje de validación no es el esperado. Usuario: '{username_message}', Clave: '{password_message}'"

    except Exception as e:
        assert False, f"No se pudo encontrar el elemento o validar el mensaje. Error: {e}"
