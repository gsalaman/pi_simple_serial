import serial
import time


print("running")

with serial.Serial("/dev/tty.usbserial-DN02Z5R6", 9600, timeout=1) as ser:
  time.sleep(0.01) # wait for serial port to open.
  if ser.isOpen():
    print("connected!")

    while True:

      while ser.inWaiting()==0:
        pass
      if ser.inWaiting() > 0:
        line = ser.readline()
        print(line)
        ser.flushInput() 


