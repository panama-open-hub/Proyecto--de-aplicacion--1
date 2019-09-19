from RPLCD.i2c import CharLCD
from time import sleep

class Pantalla(CharLCD):
    def __init__(self, displayID='PCF8574', direccion=0x27, columnas=16, lineas=2, ropt_lineas=True, luz_trasera=False, texto="texto por defecto"):
        self.texto = texto
        self.screen = CharLCD(i2c_expander=displayID, address=direccion,
              cols=columnas, rows=lineas,
              auto_linebreaks=ropt_lineas,
              backlight_enabled=luz_trasera)
    
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
        text = input("Ingrese el texto que desea que se imprima: ")
        if text== "":
            text=self.texto
            print(text)
            self.write_string(text)
        else:
            pass