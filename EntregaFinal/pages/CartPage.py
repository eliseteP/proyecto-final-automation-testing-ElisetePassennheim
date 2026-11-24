
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CartPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

        # LOCALIZADORES
        self.producto = (
            By.CLASS_NAME,
            "inventory_item_name"
        )

        self.checkout_button = (
            By.ID,
            "checkout"
        )

    # PRODUCTOS

    def obtener_nombre_producto(self):
        """
        Devuelve el nombre del producto que aparece en el carrito.
        """
        elemento = self.wait.until(
            EC.visibility_of_element_located(self.producto)
        )
        return elemento.text

    def ir_a_checkout(self):
        """
        Hace clic en el botón Checkout.
        """
        boton = self.wait.until(
            EC.element_to_be_clickable(self.checkout_button)
        )
        boton.click()

