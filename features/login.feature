# Ruta: C:\CURSO_TESTER_QA\Python_arcoiris-automation\features\login.feature
Feature: Inicio de sesion en el sitio PuntosPremiumPlus
  Como usuario del sitio
  Se desea ingresar con credenciales validas
  Para poder acceder al sistema

  Scenario: Ingreso con credenciales validas
    Given Se esta en la pagina de inicio de sesion
    When Se ingresan las credenciales validas
    And Se hace clic en el boton de Ingresar
    Then Se es redirigido a la pagina de inicio

  Scenario Outline: Validacion de credenciales invalidas
    Given Se esta en la pagina de inicio de sesion
    When Se ingresa el usuario "<usuario>" y la contrasena "<contrasena>"
    And Se hace clic en el boton de Ingresar
    Then Se muestra un mensaje de error de credenciales invalidas

    Examples: Casos de credenciales invalidas
      | usuario               | contrasena         |
      | usuario_invalido      | contrasena_valida  |
      | usuario_valido        | contrasena_invalida|
