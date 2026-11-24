from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CheckoutPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 18)

        self.campo_nombre = (By.ID, "first-name")
        self.campo_apellido = (By.ID, "last-name")
        self.campo_codigo_postal = (By.ID, "postal-code")
        self.boton_continuar = (By.ID, "continue")

    def completar_datos(self, nombre, apellido, codigo_postal):
        self.wait.until(
            EC.visibility_of_element_located(self.campo_nombre)
        ).send_keys(nombre)

        self.wait.until(
            EC.visibility_of_element_located(self.campo_apellido)
        ).send_keys(apellido)

        self.wait.until(
            EC.visibility_of_element_located(self.campo_codigo_postal)
        ).send_keys(codigo_postal)

    def continuar(self):
        self.wait.until(
            EC.element_to_be_clickable(self.boton_continuar)
        ).click()

