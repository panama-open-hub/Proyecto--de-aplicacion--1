from RPLCD.i2c import CharLCD
from time import sleep


lcd = CharLCD(i2c_expander='PCF8574', address=0x27,
              cols=16, rows=2,
              auto_linebreaks=True,
              backlight_enabled=False)
lcd.clear()
lcd.backlight_enabled = True
lcd.write_string('Hello\r\n  World!')
lcd.cursor_mode = "blink"
sleep(3)
lcd.cursor_mode = "hide"
lcd.clear()
lcd.backlight_enabled = False
print("done")
