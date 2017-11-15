import serial
import time
import random
arduino = serial.Serial('COM5', 9600, timeout=0)
i=1
while 1==1:
    command = str.encode('22222')
    arduino.write(command)   
    time.sleep(1.5)
