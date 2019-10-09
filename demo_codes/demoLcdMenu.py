from RPLCD.gpio import CharLCD
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

"""
button 1 selects 1st option on on each menu (gpio 26)
button 2 selects 2nd option on on each menu (gpio 19)
button 3 selects steps you back through the menu one level at a time (gpio 20)
"""

GPIO.setup(26, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)# button 1
GPIO.setup(19, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)# button 2
GPIO.setup(20, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)# button 3
GPIO.setup(21, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # not used 

lcd = CharLCD(numbering_mode=GPIO.BCM, cols=16, rows=2, pin_rw=None, pin_rs=13, pin_e=6, pins_data=[5,22,17,27,12,25,24,23], 
charmap='A02', auto_linebreaks=False)

# set global variables used
update = 1 # causes LCD to be updated while set to 1
mlevel = 1 # current menu level
blevel = 1 # last menu level

def level1():
    #main menu
    lcd.cursor_pos = (0, 2)
    lcd.write_string("1.Footware")
    lcd.cursor_pos = (1, 2)
    lcd.write_string("2.Transport")
    
def level2():
    #sub menu 
    lcd.cursor_pos = (0, 2)
    lcd.write_string("1.Shoes")
    lcd.cursor_pos = (1, 2)
    lcd.write_string("2.Boots")
    
def level3():
    #sub menu 
    lcd.cursor_pos = (0, 2)
    lcd.write_string("1.Ground")
    lcd.cursor_pos = (1, 2)
    lcd.write_string("2.Air")
    
def level4():
    #sub menu
    lcd.cursor_pos = (0, 2)
    lcd.write_string("1.Red")
    lcd.cursor_pos = (1, 2)
    lcd.write_string("2.Black")
    
def level5():
    #sub menu 
    lcd.cursor_pos = (0, 2)
    lcd.write_string("1.Lace up")
    lcd.cursor_pos = (1, 2)
    lcd.write_string("2.Zip up")
    
def level6():
    #sub menu 
    lcd.cursor_pos = (0, 2)
    lcd.write_string("1.Car")
    lcd.cursor_pos = (1, 2)
    lcd.write_string("2.Bus") 
    
def level7():
    #sub menu 
    lcd.cursor_pos = (0, 2)
    lcd.write_string("1.Plane")
    lcd.cursor_pos = (1, 2)
    lcd.write_string("2.Helicopter")   
    
def option1(channel):
    global mlevel, update, blevel
    blevel = mlevel
    mlevel = mlevel*2
    update = 1
    
    
def option2(channel):
    global mlevel, update, blevel
    blevel = mlevel  
    mlevel = (mlevel*2) + 1
    update = 1  
    
def goback(channel):
    global mlevel, update, blevel
    mlevel = blevel
    blevel = int(mlevel/2)
    update = 1     
    
GPIO.add_event_detect(26, GPIO.RISING, callback=option1, bouncetime=200)    
GPIO.add_event_detect(19, GPIO.RISING, callback=option2, bouncetime=200)   
GPIO.add_event_detect(20, GPIO.RISING, callback=goback, bouncetime=200)    
        

#loop to update menu on LCD
while True:
    while update ==0:
        time.sleep (0.1)
        
     
    lcd.clear()
    
    if mlevel == 1: level1()
    if mlevel == 2: level2()
    if mlevel == 3: level3()
    if mlevel == 4: level4()
    if mlevel == 5: level5()
    if mlevel == 6: level6()
    if mlevel == 7: level7()
            
    update = 0

 