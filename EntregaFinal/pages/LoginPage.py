from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC





# Creacion de  LA CLASE LOGINPAGE
class LoginPage:


     def __init__(self, driver):
        self.driver = driver
        self.wait=WebDriverWait (driver,10)


        # LOCALIZADORES
        self.username = (By.ID, "user-name") #ESTRUCTURA DE DATOS: TUPLA. 
        self.password = (By.ID, "password")
        self.login_button = (By.ID, "login-button")
        # login_button = 'login_button'

     def ingresar_usuario(self, usuario):
        self.driver.find_element(
            *self.username
        ).send_keys(usuario)


     def ingresar_password(self, password):
        self.driver.find_element(
                    *self.password
        ).send_keys(password)


     def presionar_login(self):
        self.driver.find_element(
            *self.login_button
        ).click()

     def hacer_login(self, usuario, password ):
        self.ingresar_usuario(usuario)
        self.ingresar_password(password)
        
        self.driver.find_element(
            *self.login_button
            # By.ID => como buscar , que buscar
        ).click()



     def obtener_mensaje_error(self):
         return self.driver.find_element(*self.error_message).text








