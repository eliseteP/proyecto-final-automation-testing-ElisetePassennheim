
Propósito: automatizar flujos básicos de navegación Web.
Proyecto Final.Incluye pruebas de interfaz Web y de API, reporte Html, registros de los e integración con GitHub.

Objetivo: implementar pruebas automatizadas de API y UI para validar el correcto funcionamiento de servicios y funcionalidad de la web.

Web utilizada: saucedemo.com
usuario  : "standard_user" desde usuarios.csv & usuarios.json
Cuando el login es exitoso es redirigido a la pag de inventario.
Se completa la automatización con el flujo total de la compra.

Se prueban : saucedemo_para las pruebas de interfaz y JSONPlaceholder_para las pruebas API

TECNOLOGÍAS utilizadas:
	- Python como lenguaje principal
	- Pytest para la estructura del testing
	- Selenium WebDriver para la automatización
	- Requests: ejecución de solicitudes HTTP para pruebas API
	- POM ( Page Object Model) : organización y reutilización de elementos y acciones de la interfaz.
	- Git y GitHub para el control de las versiones



Comando de ejecución : py -m pytest -v tests/test_saucedemo.py

TIPOS DE PRUEBAS:
				Automatización API

Se realizan pruebas sobre servicios HTTP para validar:

    Métodos HTTP.
    Respuestas de los endpoints.
    Códigos de estado HTTP.
    Creación y consulta de publicaciones.
    Eliminación de registros.
    Validaciones de respuestas.

Ubicación: automatizacionApi/tests/

			 Automatización UI

Se realizan pruebas automatizadas sobre la interfaz de usuario para validar:

    Inicio de sesión.
    Acceso a funcionalidades.
    Navegación.
    Inventario.
    Comportamiento de los elementos de la aplicación.

Ubicación: tests/

ESTRUCTURA:
EntregaFinal/

├── automatizacionApi/
		├── __init__.py
		├── main.py
		├── metodos_http.py
		├── validaciones.py


		├── tests/
				├── __init__.py
			 	└── test_post.py

		└── reports/
			  └── reporte_api.html

├─── tests/
├─── pages/
├── utils/
└── reports/			  
 	└── reporte_ui.

	├── test_inventory.py
│   ├── test_login_exito.py
│   └── test_saucedemo.py
│
├── utils/
├── .gitignore
└── Readme.md


EJECUCION DE PRUEBAS, desde la carpeta raiz EntregaFinal

Ejecución Pruebas API: py -m pytest automatizacionApi/tests -v

Ejecución Pruebas UI: py -m pytest tests -v


REPORTES
Se generan 2 Reportes independientes, una para prueba API y otro para UI

Comando de generacion de Reportes API:
py -m pytest automatizacionApi/tests -v --html=automatizacionApi/reports/reporte_api.html --self-contained-html


Comando de generacion de Reporte UI: 
py -m pytest tests -v --html=reports/reporte_ui.html --self-contained-html


