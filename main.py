from keypad import *
from grove_rgb_lcd import *

setText("Presione D para inicializar")
setRGB(0, 128, 15)


#variables
trigger = "N"
charge = ""
decimal_flag = 0

try:
    while read_char() !="D":
        pass 
except KeyboardInterrupt:
    print("\nApplication stopped!")

setText("Digite el monto\n >")
setRGB(0, 128, 15)

number_verification = True
while number_verification:
    try:
        trigger = read_char()
        while trigger != "A":
        
            if trigger.isdigit():
                charge = charge + trigger 
                setText("Digite el monto\n >"+str(charge))
                setRGB(0, 128, 15)
            elif  trigger == "*" and decimal_flag != 1:
                charge = charge + "."
                decimal_flag = 1
                setText("Digite el monto\n >"+str(charge))
                setRGB(0, 128, 15)

            

            
        

    except KeyboardInterrupt:
        print("\nApplication stopped!")
    
    number_verification = False
    
    try:
        val = float(charge)
    except value_error:
        setText("Error numerico")
        setRGB(200, 0, 0)
        number_verification = True