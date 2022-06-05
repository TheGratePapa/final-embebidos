import keypad
from grove_rgb_lcd import *

setText("Presione D para inicializar")
setRGB(0, 128, 15)

try:
    while True:
        # call the readLine function for each row of the keypad
        #readLine(L1, ["1","2","3","A"])
        #readLine(L2, ["4","5","6","B"])
        #readLine(L3, ["7","8","9","C"])
        trigger = readLine(L4, ["*","0","#","D"])
        time.sleep(0.2)
        if trigger = "D":
            break

except KeyboardInterrupt:
    print("\nApplication stopped!")

setText("Digite el monto")
setRGB(0, 128, 15)

