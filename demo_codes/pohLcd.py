from RPLCD.i2c import CharLCD
from time import sleep

class Pantalla(CharLCD):
    def __init__(self, i2c_expander='PCF8574', address=0x27, cols=16, rows=2, auto_linebreaks=True, backlight_enabled=False, texto="texto por defecto"):
        self.i2c = i2c_expander
        self.address = address
        self.cols = cols
        self.rows = rows
        self.auto_linebreaks = auto_linebreaks
        self.backlight_enabled = backlight_enabled
        self.texto = texto
    
    def Encender(self):
        self.display_enabled = True
        self.backlight_enabled = True
        self.write_string(self.texto)
        self.cursor_mode = "blink"
        sleep(3)
        self.cursor_mode = "hide"
        print("Encendido")
    
    def Apagar(self):
        self.display_enabled = False
        self.backlight_enabled = False
        print("Apagado")

    def Limpiar(self):
        self.clear()
        self.cursor_mode = "hide"
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