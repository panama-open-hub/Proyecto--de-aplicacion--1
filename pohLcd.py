from RPLCD.i2c import CharLCD
from time import sleep
import datetime
import logging

t= datetime.datetime.now()
class Pantalla():
    def __init__(self, displayID='PCF8574', direccion=0x27, columnas=16, lineas=2, ropt_lineas=True, luz_trasera=False, texto="texto por defecto"):
        self.texto = texto
        self.screen = CharLCD(i2c_expander=displayID, address=direccion,
              cols=columnas, rows=lineas,
              auto_linebreaks=ropt_lineas,
              backlight_enabled=luz_trasera)
    
    def log():
        logging.basicConfig(
            filename='logger.log',filemode='a', 
            format='%(asctime)s - %(levelname)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S',
            level=logging.DEBUG)

    def Test(self):
        self.screen.clear()
        self.screen.backlight_enabled = True
        self.screen.write_string('Hello\r\nWorld!')
        self.screen.cursor_mode = "blink"
        sleep(3)
        self.screen.cursor_mode = "hide"
        logging.debug("Hecho")

    def Bienvenida(self):
        self.screen.clear()
        self.screen.display_enabled = True
        self.screen.backlight_enabled = True
        self.screen.write_string("Bienvenido")
        self.screen.cursor_mode = "blink"
        sleep(3)
        self.screen.cursor_mode = "hide"
        logging.debug("Encendido")
    
    def Apagar(self):
        self.screen.display_enabled = False
        self.screen.backlight_enabled = False
        logging.debug("Apagado")
        
    def Limpiar(self):
        self.screen.clear()
        self.screen.cursor_mode = "hide"
        logging.debug("Pantalla limpia")

    def Imprimir(self):
        self.screen.clear()
        self.screen.display_enabled = True
        self.screen.cursor_mode = "blink"
        self.text1 = self.texto
        logging.debug("prueba de texto ", self.text1)
        self.text1 = input("Ingrese el texto que desea que se imprima: ")
        if self.text1 == str(""):
            self.text1=self.texto
            logging.debug(self.text1)
            self.screen.write_string(self.text1)
        else:
            self.screen.write_string(self.text1)

    def FechaHora(self):
        self.screen.clear()
        self.screen.display_enabled = True #prende la pantalla
        self.screen.cursor_pos = (0,0)
        texto2 = "%s/%s/%s\r\n%s:%s:%s" % (t.day, t.month, t.year, t.hour, t.minute, t.second)
        logging.debug("[DEBUG]: ",type(texto2)," ",texto2)
        self.screen.write_string(texto2)