import time
from grovepi import *
import math

buzzer_pin = 2

pinMode(buzzer_pin,"OUTPUT")

def half_sec_beep(): 
    
    try:
        digitalWrite(buzzer_pin,1)
        time.sleep(0.5)
        digitalWrite(buzzer_pin,0)
    except KeyboardInterrupt:
        digitalWrite(buzzer_pin,0)
    

