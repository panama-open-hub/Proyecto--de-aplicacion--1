from RPLCD.i2c import CharLCD
from time import sleep
import datetime
import logging
import asyncio


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
        sleep(2)
        self.screen.cursor_mode = "hide"
        print("Hecho")

    def Bienvenida(self):
        self.screen.clear()
        self.screen.display_enabled = True
        self.screen.backlight_enabled = True
        self.screen.write_string("Bienvenido")
        self.screen.cursor_mode = "blink"
        sleep(3)
        self.screen.cursor_mode = "hide"
        print("Bienvenido")

    async def Bienvenida_Async(self):
        self.screen.clear()
        self.screen.display_enabled = True
        self.screen.backlight_enabled = True
        self.screen.write_string("Bienvenido")
        self.screen.cursor_mode = "blink"
        self.screen.cursor_mode = "hide"
        print("[DEBUG]: ","Bienvenido async")
        
    def Apagar(self):
        self.screen.display_enabled = False
        self.screen.backlight_enabled = False
        print("[DEBUG]: ","Apagado")
    
    async def Apagar_async(self):
        self.screen.display_enabled = False
        self.screen.backlight_enabled = False
        print("[DEBUG]: ","Apagado async")
        
    def Limpiar(self):
        self.screen.clear()
        self.screen.cursor_mode = "hide"
        print("[DEBUG]","Pantalla limpia")

    async def Limpiar_async(self):
        self.screen.clear()
        self.screen.cursor_mode = "hide"
        print("[DEBUG]","Pantalla limpia async")
        await asyncio.sleep(1)
        self.screen.cursor_mode = "blink"
        await asyncio.sleep(2)

    def Imprimir(self):
        self.screen.clear()
        self.screen.display_enabled = True
        self.screen.cursor_mode = "blink"
        self.text1 = self.texto
        print("prueba de texto ", self.text1)
        self.text1 = input("Ingrese el texto que desea que se imprima: ")
        if self.text1 == str(""):
            self.text1=self.texto
            print(self.text1)
            self.screen.write_string(self.text1)
        else:
            self.screen.write_string(self.text1)
    
    async def Imprimir_async(self):
        self.screen.clear()
        self.screen.display_enabled = True
        self.screen.cursor_mode = "blink"
        self.text1 = self.texto
        print("prueba de texto ", self.text1)
        self.text1 = input("Ingrese el texto que desea que se imprima: ")
        if self.text1 == str(""):
            self.text1=self.texto
            print(self.text1)
            self.screen.write_string(self.text1)
        else:
            self.screen.write_string(self.text1)
        await asyncio.sleep(3)

    def FechaHora(self):
        t= datetime.datetime.now()
        self.screen.clear()
        self.screen.display_enabled = True #prende la pantalla
        self.screen.cursor_pos = (0,0)
        texto2 = "%s/%s/%s\r\n%s:%s:%s" % (t.day, t.month, t.year, t.hour, t.minute, t.second)
        print("[DEBUG]: ",type(texto2)," ",texto2)
        self.screen.write_string(texto2)
    
    async def MostrarFechaHora_async(self, loop = False, sleepTime = 0.95):
        #TODO: agregar cero delante de 1 a 9 segundos
        if self.screen.backlight_enabled == False:
            self.screen.backlight_enabled = True #prende luz de la pantalla
        self.screen.cursor_pos = (0,0)
        while loop == True:
            self.screen.clear()
            ta= datetime.datetime.now()
            texto2 = "%s/%s/%s\r\n%s:%s:%s" % (ta.day, ta.month, ta.year, ta.hour, ta.minute, ta.second)
            print("[DEBUG]: ",type(texto2)," ",texto2)
            self.screen.write_string(texto2)
            await asyncio.sleep(sleepTime)
        self.screen.clear()
        ta= datetime.datetime.now()
        texto2 = "%s/%s/%s\r\n%s:%s:%s" % (ta.day, ta.month, ta.year, ta.hour, ta.minute, ta.second)
        print("[DEBUG]: ",type(texto2)," ",texto2)
        self.screen.write_string(texto2)
        await asyncio.sleep(sleepTime)