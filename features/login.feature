@smoke
Feature: Inicio de sesion en el sitio PuntosPremiumPlus
  Como usuario del sitio
  Se desea ingresar con credenciales validas
  Para poder acceder al sistema

  @login @login-valido
  Scenario: Ingreso con credenciales validas
    Given Se esta en la pagina de inicio de sesion
    When Se ingresan las credenciales validas
    And Se hace clic en el boton de Ingresar
    Then Se es redirigido a la pagina de inicio

  @login @perfil
  Scenario: Acceso al perfil de usuario
    Given Se esta en la pagina de inicio de sesion
    When Se ingresan las credenciales validas
    And Se hace clic en el boton de Ingresar
    Then Se es redirigido a la pagina de inicio
    When Se hace clic en el menu hamburguesa
    And Se hace clic en el enlace "PERFIL"
    Then Se muestra el contenido del perfil de usuario

  @login @suscripcion
  Scenario: Activar la suscripcion a promociones en el perfil
    Given Se esta en la pagina de inicio de sesion
    When Se ingresan las credenciales validas
    And Se hace clic en el boton de Ingresar
    Then Se es redirigido a la pagina de inicio
    When Se hace clic en el menu hamburguesa
    And Se hace clic en el enlace "PERFIL"
    Then Se muestra el contenido del perfil de usuario
    When Se activa la suscripcion para recibir promociones
    Then Se muestra el contenido del perfil de usuario

  @login @suscripcion @desactivar
  Scenario: Desactivar la suscripcion a promociones en el perfil
    Given Se esta en la pagina de inicio de sesion
    When Se ingresan las credenciales validas
    And Se hace clic en el boton de Ingresar
    Then Se es redirigido a la pagina de inicio
    When Se hace clic en el menu hamburguesa
    And Se hace clic en el enlace "PERFIL"
    Then Se muestra el contenido del perfil de usuario
    When Se desactiva la suscripcion para recibir promociones
    Then Se muestra el contenido del perfil de usuario

  @hamburguesa
  Scenario: Comprobar el comportamiento de mostrar y ocultar el menu hamburguesa
    Given Se esta en la pagina de inicio de sesion
    When Se ingresan las credenciales validas
    And Se hace clic en el boton de Ingresar
    Then Se es redirigido a la pagina de inicio
    When Se hace click en el menu hamburguesa para mostrar las opciones y se lo vuelve a presionar luego de 10 segundos
    Then Se permanece en la pagina de inicio

  @logout @logout-exitoso
  Scenario: Cerrar sesion con exito
    Given Se esta en la pagina de inicio de sesion
    When Se ingresan las credenciales validas
    And Se hace clic en el boton de Ingresar
    Then Se es redirigido a la pagina de inicio
    When Se hace clic en el icono de usuario
    Then Se muestra la ventana modal de cerrar sesion
    When Se hace clic en el boton Aceptar del modal
    Then Se es redirigido a la pagina de inicio de sesion

  @logout @cancelar-logout
  Scenario: Cancelar el cierre de sesion
    Given Se esta en la pagina de inicio de sesion
    When Se ingresan las credenciales validas
    And Se hace clic en el boton de Ingresar
    Then Se es redirigido a la pagina de inicio
    When Se hace clic en el icono de usuario
    Then Se muestra la ventana modal de cerrar sesion
    When Se hace clic en el boton Cancelar del modal
    Then Se permanece en la pagina de inicio

  @login @login-invalido
  Scenario Outline: Validacion de credenciales invalidas
    Given Se esta en la pagina de inicio de sesion
    When Se ingresa el usuario "<usuario>" y la contrasena "<contrasena>"
    And Se hace clic en el boton de Ingresar
    Then Se muestra un mensaje de error de credenciales invalidas

    Examples: Casos de credenciales invalidas
      | usuario            | contrasena         |
      | INVALID_USERNAME   | INVALID_PASSWORD   |
      | VALID_USERNAME     | INVALID_PASSWORD   |
      | INVALID_USERNAME   | VALID_PASSWORD     |