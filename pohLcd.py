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
    
    def Test(self):
        self.screen.clear()
        self.screen.backlight_enabled = True
        self.screen.write_string('Hello\r\nWorld!')
        self.screen.cursor_mode = "blink"
        sleep(3)
        self.screen.cursor_mode = "hide"
        self.screen.clear()
        print("Hecho")

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
        self.screen.display_enabled = True
        self.text1 = self.texto
        print("prueba de texto ", self.text1)
        self.text1 = input("Ingrese el texto que desea que se imprima: ")
        if self.text1 == "":
            self.text1=self.texto
            print(self.text1)
            self.write_string("%c" %self.text1) #write_string no me ha servido, hay que buscar otro metodo
        else:
            self.write_string("%c" &self.text1)

    def FechaHora(self):
        self.screen.display_enabled = True #prende la pantalla
        self.screen.cursor_pos = (1,1)
        texto2 = "%s/%s/%s \r\n%s:%s:%s" % (t.day, t.month, t.year, t.hour, t.minute, t.second)
        print("[DEBUG]: ",type(texto2)," ",texto2)
        self.screen.write_string(texto2)