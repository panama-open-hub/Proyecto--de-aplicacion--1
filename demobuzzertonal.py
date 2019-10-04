from gpiozero import TonalBuzzer
from gpiozero.tones import Tone
from time import sleep
t = TonalBuzzer(27) # change to whatever pin the buzzer is connected

v1 = ["C4", "C4", "G4","G4","A4","A4","G4"]
v2 = ["F4","F4","E4","E4","D4","D4","C4"]
v3 = ["G4", "G4", "F4","F4","E4","E4","D4"]
v4 = ["C4", "D4", "E4","F4","G4","G4"]
v5 = ["A4","A4", "A4", "A4","G4","G4"]
v6 = ["F4", "F4", "F4","F4","E4","E4"]
v7 = ["D4","D4","D4","E4","C4","C4"]

song = [v1,v2,v3,v3,v1,v2,v4,v5,v6,v7]


for verse in song:
    for note in verse:
        t.play(note)
        sleep(0.4)
        t.stop()
        sleep(0.1)
    sleep(0.2)
