# Ruta: C:\CURSO_TESTER_QA\Python_arcoiris-automation\features\steps\login_steps.py
# 150925 -14:50
from behave import given, when, then
from pages.login_page import LoginPage
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
import os
import time

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
    context.login_page.enter_credentials(username, password)

@when('Se ingresa el usuario "{username}" y la contrasena "{password}"')
def step_impl(context, username, password):
    """
    Se ingresan el usuario y la contrasena proporcionados en el escenario.
    """
    user = os.getenv(username) if username in os.environ else username
    passw = os.getenv(password) if password in os.environ else password

    context.login_page.enter_credentials(user, passw)

@when("Se hace clic en el boton de Ingresar")
def step_impl(context):
    """
    Se hace clic en el botón de ingreso.
    """
    context.login_page.click_login_button()

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
    Luego se hace clic en el botón 'Aceptar' del modal para volver al login.
    """
    error_message_locator = (By.ID, "swal2-html-container")
    accept_button_locator = (By.CSS_SELECTOR, "button.swal2-confirm")

    try:
        wait = WebDriverWait(context.browser, 10)
        error_message_element = wait.until(
            EC.visibility_of_element_located(error_message_locator)
        )

        actual_text = error_message_element.text
        expected_messages = ["Clave Usuario Invalida.!!", "Usuario Inexistente.!!"]

        if any(msg in actual_text for msg in expected_messages):
            print(f"Mensaje de error validado: {actual_text}")
        else:
            assert False, f"El mensaje de error no es el esperado. Se encontró: {actual_text}"

        accept_button = wait.until(EC.element_to_be_clickable(accept_button_locator))
        accept_button.click()
        print("Se hizo clic en el botón 'Aceptar' y se volvió a la pantalla inicial.")

    except TimeoutException:
        assert False, "El mensaje de error o el botón 'Aceptar' no fueron visibles en el tiempo de espera."

@when("Se hace clic en el icono de usuario")
def step_impl(context):
    """
    Se hace clic en el icono de usuario para mostrar el modal de cerrar sesión.
    """
    context.login_page.click_logout_arrow()

@then("Se muestra la ventana modal de cerrar sesion")
def step_impl(context):
    """
    Se verifica que la ventana modal de cerrar sesión sea visible.
    """
    modal_locator = (By.CLASS_NAME, "swal2-modal")
    try:
        WebDriverWait(context.browser, 10).until(
            EC.visibility_of_element_located(modal_locator)
        )
        print("La ventana modal de cerrar sesión es visible.")
    except TimeoutException:
        assert False, "La ventana modal de cerrar sesión no se hizo visible."

@when("Se hace clic en el boton Aceptar del modal")
def step_impl(context):
    """
    Se hace clic en el botón 'Aceptar' del modal de cerrar sesión.
    """
    context.login_page.accept_logout()

@when("Se hace clic en el boton Cancelar del modal")
def step_impl(context):
    """
    Se hace clic en el botón 'Cancelar' del modal de cerrar sesión.
    """
    context.login_page.cancel_logout()

@then("Se es redirigido a la pagina de inicio de sesion")
def step_impl(context):
    """
    Se verifica que la URL actual sea la de la página de inicio de sesión.
    """
    expected_url = context.login_page.url + "Login.php"
    try:
        WebDriverWait(context.browser, 10).until(
            EC.url_to_be(expected_url)
        )
        print(f"Redireccion exitosa. La URL actual es: {context.browser.current_url}")
    except TimeoutException:
        assert False, f"No se produjo una redireccion a la pagina de inicio de sesion. La URL actual es: {context.browser.current_url}"

@then("Se permanece en la pagina de inicio")
def step_impl(context):
    """
    Se verifica que la URL actual no haya cambiado.
    """
    current_url = context.browser.current_url
    expected_url_part = "Home.php"

    if expected_url_part not in current_url:
        assert False, f"No se permaneció en la página de inicio. Se redirigió a: {current_url}"
    else:
        print("Se permaneció en la página de inicio.")

@when("Se hace clic en el menu hamburguesa")
def step_impl(context):
    """
    Se hace clic en el ícono del menú hamburguesa para desplegar las opciones.
    """
    context.login_page.click_hamburger_menu()

@when("Se hace clic en el enlace \"PERFIL\"")
def step_impl(context):
    """
    Se hace clic en el enlace "PERFIL".
    """
    context.login_page.click_profile_link()

@then("Se muestra el contenido del perfil de usuario")
def step_impl(context):
    """
    Se verifica que el contenido del perfil se haya hecho visible.
    """
    profile_content_locator = (By.ID, "Perfil")
    try:
        wait = WebDriverWait(context.browser, 10)
        wait.until(EC.visibility_of_element_located(profile_content_locator))
        print("El contenido del perfil es visible.")
    except TimeoutException:
        assert False, "No se visualizó el contenido del perfil de usuario."

@when("Se activa la suscripcion para recibir promociones")
def step_impl(context):
    """
    Se hace clic en el checkbox de suscripción para activarlo.
    """
    context.login_page.click_subscription_checkbox()

@when("Se desactiva la suscripcion para recibir promociones")
def step_impl(context):
    """
    Se hace clic en el checkbox de suscripción para desactivarlo.
    """
    context.login_page.click_subscription_checkbox()

@when("Se hace click en el menu hamburguesa para mostrar las opciones y se lo vuelve a presionar luego de 10 segundos")
def step_impl(context):
    """
    Se hace click en el menú hamburguesa, se espera 10 segundos
    y se lo vuelve a presionar para ocultar las opciones.
    """
    context.login_page.click_hamburger_menu()
    print("Esperando 10 segundos...")
    time.sleep(10)
    context.login_page.click_hamburger_menu()

# Pasos para el canje de puntos ###############################
@when('Se hace clic en la seccion "{section_name}"')
def step_impl(context, section_name):
    """
    Se hace clic en la sección especificada (por ejemplo, "Premios").
    """
    if section_name == "Premios":
        context.login_page.click_prizes_button()
    else:
        raise NotImplementedError(f'La seccion "{section_name}" no esta implementada.')

@when('Se selecciona la sucursal "{branch_name}"')
def step_impl(context, branch_name):
    """
    Se selecciona la sucursal del menu desplegable.
    """
    context.login_page.select_branch(branch_name)

@when('Se hace clic en el boton "VER" del producto "{product_name}"')
def step_impl(context, product_name):
    """
    Se hace clic en el botón "VER" del producto especificado.
    """
    print(f"Intento de hacer clic en el botón 'VER' para el producto: {product_name}")
    context.login_page.click_product_ver_button()

@when('Se hace clic en el boton "CANJEAR" del modal')
def step_impl(context):
    """
    Se hace clic en el botón "CANJEAR" del modal de detalles del producto.
    """
    context.login_page.click_redeem_button_modal()

@then('Se muestra el modal de confirmacion con el mensaje "{message}"')
def step_impl(context, message):
    """
    Se verifica que el modal de confirmación de canje sea visible y muestre el mensaje esperado.
    """
    modal_text = context.login_page.get_summary_message()
    assert message in modal_text, f"El mensaje esperado era '{message}', pero se obtuvo '{modal_text}'."

@when('Se hace clic en el boton "ACEPTAR" del modal de confirmacion')
def step_impl(context):
    """
    Se hace clic en el botón 'ACEPTar' del modal de confirmación de canje.
    """
    context.login_page.click_accept_button_modal()

@then('Se muestra el modal de resumen de la transaccion')
def step_impl(context):
    """
    Se verifica que el modal de resumen de la transacción sea visible.
    """
    try:
        WebDriverWait(context.browser, 10).until(
            EC.visibility_of_element_located(context.login_page.volver_button)
        )
        print("El modal de resumen de la transaccion es visible.")
    except TimeoutException:
        assert False, "El modal de resumen de la transaccion no se hizo visible."

@when('Se hace clic en el boton "VOLVER"')
def step_impl(context):
    """
    Se hace clic en el botón "VOLVER" para cerrar el modal de resumen.
    """
    context.login_page.click_volver_button()

@then('Se es redirigido a la pagina de premios')
def step_impl(context):
    """
    Se verifica que se haya regresado a la página de premios.
    """
    expected_url_part = "Punto.php"
    assert expected_url_part in context.browser.current_url, f"No se regreso a la pagina de premios. La URL actual es: {context.browser.current_url}"

@then('Se muestra el modal de canje fallido con el mensaje "{message}"')
def step_impl(context, message):
    """
    Se verifica que el modal de canje fallido sea visible y muestre el mensaje esperado.
    """
    modal_text = context.login_page.get_summary_message()
    assert message in modal_text, f"El mensaje esperado era '{message}', pero se obtuvo '{modal_text}'."

@when('Se hace clic en el boton "OK" del modal de canje fallido')
def step_impl(context):
    """
    Se hace clic en el botón "OK" del modal de canje fallido.
    """
#     context.login_page.click_ok_button_modal()
# #
# # ---------------- CANJE DE PUNTOS (actualizado 150925) ----------------#######################
#
# @when('Se hace clic en la seccion "Premios"')
# def step_impl(context):
#     context.login_page.click_prizes_button()
#
#
# @when('Se selecciona la sucursal "{sucursal}"')
# def step_impl(context, sucursal):
#     context.login_page.select_branch(sucursal)
#
#
# @when('Se hace clic en el boton "VER" del producto "{producto}"')
# def step_impl(context, producto):
#     # Nota: el metodo click_product_ver_button() actual estático se usa aquí.
#     # Si luego querés hacer click según el nombre del producto, lo adaptamos.
#     context.login_page.click_product_ver_button()
#
#
# @when('Se hace clic en el boton "CANJEAR" del modal')
# def step_impl(context):
#     context.login_page.click_redeem_button_modal()
#
#
# @then('Se muestra el modal de confirmacion con el mensaje "¡Felicitaciones! Tu premio fue reservado con exito"')
# def step_impl(context):
#     """
#     Buscamos el contenido del modal de SweetAlert2 por su contenedor
#     'swal2-html-container' (id). Si no aparece en 20s, fallamos con mensaje claro.
#     """
#     try:
#         container = WebDriverWait(context.browser, 20).until(
#             EC.visibility_of_element_located((By.ID, "swal2-html-container"))
#         )
#         texto = container.text.strip()
#         assert "¡Felicitaciones! Tu premio fue reservado con exito" in texto or "Felicitaciones" in texto, \
#             f" Texto inesperado en modal: '{texto}'"
#     except TimeoutException:
#         # fallback: intentar con el método del page object (si existe)
#         mensaje = None
#         try:
#             mensaje = context.login_page.get_summary_message()
#         except Exception:
#             mensaje = None
#         assert mensaje is not None and "Felicitaciones" in mensaje, \
#             " No apareció el modal de confirmación con el mensaje esperado."
#
#
# @when('Se hace clic en el boton "ACEPTAR" del modal de confirmacion')
# def step_impl(context):
#     context.login_page.click_accept_button_modal()
#     # Después del click, esperamos un pequeño lapso para que el siguiente modal/aplicación procese
#     try:
#         # si el modal anterior se oculta, esperamos su desaparición
#         WebDriverWait(context.browser, 8).until(
#             EC.invisibility_of_element_located((By.ID, "swal2-html-container"))
#         )
#     except TimeoutException:
#         # no es crítico: puede quedar el mismo contenedor con nuevo texto -> lo toleramos
#         pass
#
#
# @then("Se muestra el modal de resumen de la transaccion")
# def step_impl(context):
#     """
#     Validamos que aparezca (de nuevo) el contenedor del modal de resumen.
#     Aceptamos cualquier texto visible dentro del contenedor como indicador.
#     """
#     try:
#         container = WebDriverWait(context.browser, 20).until(
#             EC.visibility_of_element_located((By.ID, "swal2-html-container"))
#         )
#         texto = container.text.strip()
#         assert len(texto) > 0, " El modal de resumen apareció pero está vacío."
#     except TimeoutException:
#         # fallback: intentar con get_summary_message()
#         mensaje = None
#         try:
#             mensaje = context.login_page.get_summary_message()
#         except Exception:
#             mensaje = None
#         assert mensaje is not None, " No se mostró el modal de resumen de la transacción."
#
#
# @when('Se hace clic en el boton "VOLVER"')
# def step_impl(context):
#     context.login_page.click_volver_button()
#
#
# @then("Se es redirigido a la pagina de premios")
# def step_impl(context):
#     # Validamos por URL o por la presencia del listado de premios (se prueba por URL primero)
#     try:
#         WebDriverWait(context.browser, 10).until(
#             EC.url_contains("Premios")
#         )
#     except TimeoutException:
#         # fallback: comprobar que volvimos al listado buscando el boton CANJEAR o similar
#         try:
#             # intentamos detectar el botón CANJEAR en la lista (si existe)
#             WebDriverWait(context.browser, 8).until(
#                 EC.presence_of_element_located((By.XPATH, "//*[contains(text(),'CANJEAR') or contains(text(),'Canjear')]"))
#             )
#         except TimeoutException:
#             assert False, " No se detectó redirección a la página de premios (ni URL ni elemento CANJEAR)."
