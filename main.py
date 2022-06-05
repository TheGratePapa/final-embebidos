import keypad

try:
    while True:
        # call the readLine function for each row of the keypad
        readLine(L1, ["1","2","3","A"])
        readLine(L2, ["4","5","6","B"])
        readLine(L3, ["7","8","9","C"])
        readLine(L4, ["*","0","#","D"])
        time.sleep(0.1)
except KeyboardInterrupt:
    print("\nApplication stopped!")

