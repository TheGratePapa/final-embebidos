import time
import RPi.GPIO as GPIO
import mfrc522
 

 
# Welcome message
#print("Looking for cards")
#print("Press Ctrl-C to stop.")
 
# This loop checks for chips. If one is near it will get the UID

def card_reader():
  # Create an object of the class MFRC522
  MIFAREReader = mfrc522.MFRC522()
  try:
    
    while True:
  
      # Scan for cards
      (status,TagType) = MIFAREReader.MFRC522_Request(MIFAREReader.PICC_REQIDL)
  
      # Get the UID of the card
      (status,uid) = MIFAREReader.MFRC522_Anticoll()
  
      # If we have the UID, continue
      if status == MIFAREReader.MI_OK:
  
        # Print UID
        print("UID: "+str(uid[0])+","+str(uid[1])+","+str(uid[2])+","+str(uid[3]))
        return uid
      time.sleep(2)
  
  except KeyboardInterrupt:
    GPIO.cleanup()
