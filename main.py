from keypad import *
from grove_rgb_lcd import *
from Read import *
#from buzzer import *
from transaction import *
import os
import sys

def cancel_verification(var):
    if var == "B":
        os.execl(sys.executable, sys.executable, *sys.argv)

def visible_password(var):
    if var == "C"
        if check:
            check = False
        else
            check = True

while True:
    setText("Presione D para inicializar")
    setRGB(0, 128, 15)


    #variables
    trigger = "N"
    charge = ""
    pin = ""
    decimal_flag = 0
    check = True
    

    #salir de modo standby
    try:
        while read_char() !="D":
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nApplication stopped!")

    #ingresar monto
    setText("Digite el monto\n >")
    setRGB(0, 128, 15)

    number_verification = True
    while number_verification:
        try:
        
            while trigger != "A":
                trigger = read_char()
                time.sleep(0.2)
                print("charge: " + charge)
                print("trigger: "+ trigger)
                if trigger.isdigit():
                    charge = charge + trigger 
                    setText("Digite el monto\n >"+str(charge))
                    setRGB(0, 128, 15)
                elif  trigger == "*" and decimal_flag != 1:
                    charge = charge + "."
                    decimal_flag = 1
                    setText("Digite el monto\n >"+str(charge))
                    setRGB(0, 128, 15)
                cancel_verification(trigger)
                
        except KeyboardInterrupt:
            print("\nApplication stopped!")
        
        number_verification = False
        
        try:
            charge = int(float(charge)*100)
        except value_error:
            setText("Error numerico")
            setRGB(200, 0, 0)
            number_verification = True

    #read card
    setText("coloque tarjeta")
    setRGB(50, 50, 255)
    card = card_reader()
    print("tarjeta leida: "+ str(card)) 
    #half_sec_beep()
    #password

    setText("Digite PIN\n >")
    setRGB(0, 128, 15)

    
    pin_verification = True
    while pin_verification:
        number_verification = True
        while number_verification:
            try:
                n=0
                pin = ""
                while n<4:

                    trigger = read_char()
                    cancel_verification(trigger)
                    visible_password(trigger)
                    time.sleep(0.2)
                    print("pin: " + pin)
                    print("trigger: "+ trigger)
                    if trigger.isdigit() and check != True:
                        pin = pin + trigger 
                        setText("Digite el pin\n >"+str(pin))
                        setRGB(0, 128, 15)
                    elif trigger.isdigit() and check:
                         pin = pin + trigger 
                        setText("Digite el pin\n >"+ len(pin)*"*")
                        setRGB(0, 128, 15)
                    n+=1
            except KeyboardInterrupt:
                print("\nApplication stopped!")
            
            number_verification = False
            
            try:
                val = int(pin)
                
            except value_error:
                setText("Error numerico")
                setRGB(200, 0, 0)
                number_verification = True

        #Verificacion

        setText("Verificacion")
        setRGB(255, 255, 255)
        if verification_check((card[0],card[1],card[2],card[3]), pin, charge)!= True:
            print("Error en la transaccion")
            setText("Error en la \ntransaccion")
            setRGB(255, 30, 30)
            time.sleep(2)
            setText("Digite PIN\n >")
            setRGB(0, 128, 15)
        else:
            print("Transaccion exitosa")
            setText("Transaccion exitosa")
            setRGB(30, 255, 255)
            pin_verification = False
            time.sleep(2)
            
