import serial
import time

def get_button():
  global ser

  if ser.inWaiting() == 0:
    return None
  
  line = ser.readline()
  line = line.rstrip()

  print("Line: "+ line)


  ser.flushInput() 

print("running")
ser = serial.Serial("/dev/tty.usbserial-DN02Z5R6", 9600, timeout=1) 
time.sleep(0.01) # wait for serial port to open.
if ser.isOpen():
  print("connected!")

  while True:
    get_button()
    time.sleep(0.01)



