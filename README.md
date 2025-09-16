## Proyecto de Automatización PuntosPremiumPlus
Se trata de un proyecto de automatización de pruebas de interfaz de usuario (UI) para el sitio web PuntosPremiumPlus. Se utiliza el framework de pruebas Behave para la automatización Behavior-Driven Development (BDD), lo que permite que las pruebas sean escritas en un lenguaje claro y legible para humanos, gracias a la sintaxis Gherkin.
Autora: Adriana Loretán

## Requisitos Previos
Se necesitan los siguientes componentes instalados para poder ejecutar las pruebas:

Python 3.10 o superior.

Git para clonar el repositorio.

Google Chrome o cualquier navegador compatible.

## Instalación
Se clonó el repositorio y se instalaron las dependencias necesarias.

- Clonar el repositorio:
git clone https://github.com/tu_usuario/Python_arcoiris-automation.git
cd Python_arcoiris-automation
- Crear y activar el entorno virtual:

python -m venv .venv
# Para Windows
.\.venv\Scripts\activate
# Para macOS/Linux
source .venv/bin/activate
## Instalar las dependencias:

pip install -r requirements.txt

## Estructura del Proyecto
El proyecto está organizado de acuerdo con el framework de Behave, utilizando el patrón de diseño Page Object Model para una mayor mantenibilidad.

Python_arcoiris-automation/
├── features/
│   ├── steps/
│   │   └── login_steps.py  # Archivo que contiene la lógica de los pasos de prueba.
│   └── login.feature       # Archivo Gherkin con los escenarios de prueba.
├── pages/
│   └── login_page.py       # Archivo con los elementos y métodos de la página de login.
├── .env.example
├── README.md
├── requirements.txt
└── behave.ini
## Ejecución de Pruebas
- Para ejecutar las pruebas, se utiliza el siguiente comando en el terminal, asegurándose de que el entorno virtual esté activo.

behave
- Generar un reporte HTML
Para generar un reporte detallado en formato HTML, se utiliza el siguiente comando:
behave --format html --out behave_report.html
El reporte behave_report.html se creará en la carpeta raíz del proyecto y se puede abrir con cualquier navegador web.

## Casos de Prueba
Se incluyen pruebas para las siguientes funcionalidades:

- Inicio de Sesión: Se validan los escenarios de inicio de sesión exitoso e inválido.

- Cierre de Sesión: Se valida el cierre de sesión exitoso y la cancelación del mismo.

- Navegación: Se prueba el acceso al perfil de usuario y a la sección de premios.

- Funcionalidades del Perfil: Se verifica la activación y desactivación de la suscripción a promociones.

- IMPORTANTE (VER ALCANCE) Canje de Puntos: Se valida el proceso de canje de puntos por productos en diferentes sucursales, hasta el paso previo a aceptar el canje.

