from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC





class CheckoutOverview:
   def __init__(self, driver):
    self.wait = WebDriverWait(driver, 10)
    
    
    self.driver=driver
   # self.finish_button=(By.ID,'finish')
    #self.confirmacion=(By.CLASS_NAME, 'complete-header')
    self.boton_finalizar = (By.ID, "finish")
    self.mensaje_confirmacion = (By.CLASS_NAME, "complete-header")
        
        
   def finalizar_compra(self):
        self.wait.until(
            EC.element_to_be_clickable(self.boton_finalizar)
        ).click()
    
   def obtener_confirmacion(self):
    # return self.driver.find_element(
      #    *self.confirmacion
       #     
        #).text
        return self.wait.until(
            EC.visibility_of_element_located(
                self.mensaje_confirmacion
            )
        ).text 