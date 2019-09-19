from RPLCD.i2c import CharLCD
from time import sleep

class Pantalla(CharLCD):
    def __init__(self, i2c_expander='PCF8574', address=0x27, cols=16, rows=2, auto_linebreaks=True, backlight_enabled=False, texto="texto por defecto"):
        """
        self.expander = i2c_expander
        self.address = address
        self.cols = cols
        self.rows = rows
        self.auto_linebreaks = auto_linebreaks
        self.backlight_enabled = backlight_enabled
        """
        self.texto = texto
        
        self.screen = CharLCD(i2c_expander='PCF8574', address=0x27,
              cols=16, rows=2,
              auto_linebreaks=True,
              backlight_enabled=False)
    

    def Test(self):
        self.screen.clear()
        self.screen.backlight_enabled = True
        self.screen.write_string('Hello\r\n  World!')
        self.screen.cursor_mode = "blink"
        sleep(3)
        self.screen.cursor_mode = "hide"
        self.screen.clear()
        self.screen.backlight_enabled = False
        print("done")

    def Encender(self):
        self.screen.display_enabled = True
        self.screen.backlight_enabled = True
        self.screen.write_string(self.texto)
        self.screen.cursor_mode = "blink"
        sleep(3)
        self.screen.cursor_mode = "hide"
        print("Encendido")
    
    def Apagar(self):
        self.screen.display_enabled = False
        self.screen.backlight_enabled = False
        print("Apagado")

    def Limpiar(self):
        self.screen.clear()
        self.screen.cursor_mode = "hide"
        print("Pantalla limpia")
    
    def Imprimir(self):
        text = self.texto
        text = input("Ingrese el texto que desea que se imprima")
        if text== "":
            text=self.texto
            print(text)
            self.write_string(text)
        else:
            pass