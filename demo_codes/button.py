#!/usr/bin/python3
from gpiozero import LED, Button
from signal import pause

def pressed():
    print("boton presionado")

def released():
    print("boton soltado")

button = Button(17)
button.when_pressed = pressed
button.when_released = released

pause()