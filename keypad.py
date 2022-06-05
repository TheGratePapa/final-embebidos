import RPi.GPIO as GPIO
import time

# these GPIO pins are connected to the keypad
# change these according to your connections!
L1 = 5
L2 = 6
L3 = 13
L4 = 19

C1 = 26
C2 = 16
C3 = 20
C4 = 21

# Initialize the GPIO pins

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

GPIO.setup(L1, GPIO.OUT)
GPIO.setup(L2, GPIO.OUT)
GPIO.setup(L3, GPIO.OUT)
GPIO.setup(L4, GPIO.OUT)

# Make sure to configure the input pins to use the internal pull-down resistors

GPIO.setup(C1, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(C2, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(C3, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(C4, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

# The readLine function implements the procedure discussed in the article
# It sends out a single pulse to one of the rows of the keypad
# and then checks each column for changes
# If it detects a change, the user pressed the button that connects the given line
# to the detected column

def readLine(line, characters):
    char = ""
    GPIO.output(line, GPIO.HIGH)
    if(GPIO.input(C1) == 1):
        #print(characters[0])
        char = characters[0]
    if(GPIO.input(C2) == 1):
        #print(characters[1])
        char = characters[1]
    if(GPIO.input(C3) == 1):
        #print(characters[2])
        char = characters[2]
    if(GPIO.input(C4) == 1):
        #print(characters[3])
        char = characters[3]
    GPIO.output(line, GPIO.LOW)
    return char
    

while True:
    try:     
        return_value = readLine(L1, ["1","2","3","A"])
        if return_value != "":
            stored_char = return_value
        return_value = readLine(L2, ["4","5","6","B"])
        if return_value != "":
            stored_char = return_value
        return_value = readLine(L3, ["7","8","9","C"])
        if return_value != "":
            stored_char = return_value
        return_value = readLine(L4, ["*","0","#","D"])
         if return_value != "":
            stored_char = return_value
        if stored_char != "":
            print(stored_char)
            stored_char = ""
        time.sleep(0.2)

            
    except KeyboardInterrupt:
        print("\nApplication stopped!")

