import pytest
from pathlib import Path
import csv 
import json

from pathlib import Path
from selenium import webdriver
# import glob
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# datos externos utilizados para ejecutar pruebas con diferentes credenciales
#import sys
#import os
#sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
#from data.datos import datos_login, datos_compra
from data.datos import datos_login
from data.datos import datos_compra

#Logger para registrar eventos y facilitar el diagnostico de fallos
from utils.helpers import logger
#Cada clase representa una página o sección de la apliación
from pages.LoginPage import LoginPage
from pages.InventoryPage import InventoryPage
from pages.InventoryPage import InventoryPage
from pages.CartPage import CartPage
from pages.CheckoutOverview import CheckoutOverview
from pages.CheckoutPage import CheckoutPage

#Fixture: configuración y finalizador del navegador
@pytest.fixture
def driver():
    driver= webdriver.Chrome()
    
    opciones = webdriver.ChromeOptions()
    # Desactivar avisos de contraseñas de Google
    opciones.add_experimental_option(
        "prefs",
        {
            "credentials_enable_service": False,
            "profile.password_manager_enabled": False,
            "profile.password_manager_leak_detection": False,
        }
    )


    # Evitar algunas notificaciones del navegador
    opciones.add_argument("--disable-notifications")
    
    
    
    
    driver.maximize_window()
    driver.get("https://www.saucedemo.com/")
    
    yield driver
    driver.quit()

#Ubicación de archivos de datos externos

RUTA_CSV = (
    Path(__file__).resolve()
    / "data"
    / "usuarios.csv"
)

#def leeer_datos_csv():
#    datos = []
#    with open(RUTA_CSV, mode='r', encoding='utf-8', newline='') as archivo:
#     leer = csv.DictReader(archivo)
    

#    open()
#    for fila in leer :
#            usuario = fila['usuario']
#            password = fila['password']
#
#            datos.append((usuario,password))
#    return datos


# RUTA_JSON = (
#     Path(__file__).resolve().parents[1]
#     / "data"
#     / "usuarios.json"
# )

#def leer_datos_json():
#    datos = []
#    with open(RUTA_CSV, mode='r', encoding='utf-8', newline='') as archivo:
#        leer = json.load(archivo)
#
#        for fila in leer :
#           usuario = fila['usuario']
#           password = fila['password']
#
#            datos.append((usuario,password))
#    return datos



#Parametrizacion
#Validaciones: Login, logo del inventario, 




@pytest.mark.parametrize("usuario,password", datos_login)
def test_01_login(driver,usuario,password):

    # CREAR UN OBJETO
    login = LoginPage(driver)

    # login.ingresar_password()

    driver.get("https://www.saucedemo.com/")

    login.hacer_login(usuario, password)
    
    WebDriverWait(driver,10).until(
        EC.url_contains('inventory.html')
    )

    assert "/inventory.html" in driver.current_url , "ERROR: No se redirigió a /inventory.html"



def test_logo_inventario(driver):

     login = LoginPage(driver)
     inventory = InventoryPage(driver)

     driver.get("https://www.saucedemo.com/")

     login.hacer_login("standard_user","secret_sauce")

     assert inventory.obtener_logo() == 'Swag Labs'

     inventario_texto = inventory.obtener_logo()

     assert inventario_texto == 'Swag Labs'

































@pytest.mark.parametrize("usuario, password,nombre, apellido, codigo_postal",datos_compra)

def test_compra_completa(driver, usuario, password, nombre, apellido, codigo_postal):
    wait=WebDriverWait (driver,10)
    
    #login
    login=LoginPage(driver)
    login.hacer_login(usuario,password)
    
    inventario = InventoryPage(driver)
    inventario.agregar_primer_producto()
    
    
    WebDriverWait(driver,10).until(
        EC.url_contains("inventory.html")
    )
    assert "inventory.html" in driver.current_url,(
        "ERROR: no se pudo ingresar al inventario"
    )
    #agregar producto al carrito
    inventario=InventoryPage(driver)
    inventario.agregar_primer_producto()
    inventario.abrir_carrito()
    wait.until (EC.url_contains("cart.html"))
    
    assert "cart.html" in driver.current_url, (
        "ERROR: no se abrió el carrito"
    )

    print("Producto agregado y carrito abierto")
    
    #inicio checkout
    checkout=CartPage(driver)
    checkout.ir_a_checkout()
    wait.until(EC.url_contains("checkout-step-one.html"))
    
    #completar datos del comprador para luego finalizar compra
    completar_datos=CheckoutPage (driver)
    completar_datos.completar_datos(nombre, apellido, codigo_postal)
    completar_datos.continuar()
    wait.until(EC.url_contains("checkout-step-two.html"))
   
    overview=CheckoutOverview(driver)
    assert "checkout-step-two.html" in driver.current_url, (
        "ERROR: no se procedió al resumen de compra"
    )

 # 7. Finalizar la compra
    overview.finalizar_compra()

    wait.until(EC.url_contains("checkout-complete.html"))

    # 8. Validar la confirmación final
    confirmacion = overview.obtener_confirmacion()

    assert confirmacion == "Thank you for your order!", (
        f"ERROR: confirmación inesperada: {confirmacion!r}"
    )













@pytest.mark.parametrize("usuario,password,nombre,apellido,codigo_postal", datos_compra
)
def test_compra_completa(
    driver, usuario, password,nombre, apellido, codigo_postal):
   
   #login
    login=LoginPage(driver)
    login.hacer_login(usuario,password)
   
   
    inventario=InventoryPage ( driver)
    inventario.agregar_primer_producto()
    inventario.abrir_carrito()
    
    checkouts=CartPage(driver)
    checkouts.ir_a_checkout()
    
    completar_datos=CheckoutPage(driver)
    completar_datos.completar_datos(nombre,apellido,codigo_postal)
    completar_datos.continuar()
    
    overview = CheckoutOverview(driver)
    overview.finalizar_compra()
    
    WebDriverWait(driver, 10).until(
    EC.url_contains("checkout-complete.html")
)

    confirmacion = overview.obtener_confirmacion()
    assert(
        overview.obtener_confirmacion()=="Thank you for your order!"
        
    )
    
inventario = InventoryPage(driver)

#Verificar que el inventario se haya cargado
#assert inventario.obtener_logo() == "Swag Labs"

# Agregar el producto y abrir el carrito
#inventario.agregar_primer_producto()
#inventario.abrir_carrito()

# Verificar que se abrió la página del carrito
#WebDriverWait(driver, 10).until(
#   EC.url_contains("cart.html")
#)

#assert "cart.html" in driver.current_url

