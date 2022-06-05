from keypad import *
from grove_rgb_lcd import *

setText("Presione D para inicializar")
setRGB(0, 128, 15)


#variables
trigger = "N"
charge = ""
decimal_flag = 0

try:
    while trigger !="D":
        # call the readLine function for each row of the keypad
        #readLine(L1, ["1","2","3","A"])
        #readLine(L2, ["4","5","6","B"])
        #readLine(L3, ["7","8","9","C"])
        trigger = readLine(L4, ["*","0","#","D"])
        time.sleep(0.2)

except KeyboardInterrupt:
    print("\nApplication stopped!")

setText("Digite el monto\n >")
setRGB(0, 128, 15)

number_verification = True
while number_verification:
    try:
        while trigger != "A":
            # call the readLine function for each row of the keypad
        
            trigger = readLine(L1, ["1","2","3","A"])
            trigger = readLine(L2, ["4","5","6","B"])
            trigger = readLine(L3, ["7","8","9","C"])
            trigger = readLine(L4, ["*","0","#","D"])
            time.sleep(0.4)

        
            if trigger.isdigit():
                charge = charge + trigger 
            elif  trigger == "*" and decimal_flag !=1
                charge = charge + "."
                decimal_flag = 1


            setText("Digite el monto\n >"+str(charge))
            setRGB(0, 128, 15)

            
        

    except KeyboardInterrupt:
        print("\nApplication stopped!")
    
    number_verification = False
    
    try:
        val = float(charge)
    except Value error:
        setText("Error numerico")
        setRGB(200, 0, 0)
        number_verification = True