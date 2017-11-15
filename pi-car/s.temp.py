import serial, time
arduino = serial.Serial('COM10', 115200, timeout=1)
time.sleep(1) #give the connection a second to settle

i=0   
    
while True:
    arduino.write(str(i)+'\0')
    #i=i+1
    if i>100:
        i=0
    i=i+1
    data = arduino.readline()
    if data:
        
        print data.rstrip('\n') #strip out the new lines for now
		# (better to do .read() in the long run for this reason
