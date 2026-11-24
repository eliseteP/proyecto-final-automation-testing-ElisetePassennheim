from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC




class InventoryPage:


    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)


    # locatores

        self.logo = (By.CLASS_NAME, 'app_logo')
        self.primer_producto = (
            By.ID,
            "add-to-cart-sauce-labs-backpack"
        )

        self.carrito = (
            By.CLASS_NAME,
            "shopping_cart_link"
        )


    def obtener_logo( self ):
        """
            Devuelve el texto del logo
        """
        return self.driver.find_element(
            *self.logo
        ).text

       

    def agregar_primer_producto(self):
        """
        Agrega Sauce Labs Backpack al carrito.
        """
       # return self.driver.find_element(
       # *self.primer_producto
      
        #).click()
       
        boton = self.wait.until(
            EC.element_to_be_clickable(self.primer_producto)
        )
        boton.click()
    
    
   


    def abrir_carrito(self):
        """
        Abre el carrito de compras.
        """
        return self.driver.find_element(
        *self.carrito
        ).click()
       