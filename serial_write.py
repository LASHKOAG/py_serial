import time
import serial

ser=serial.Serial(
	port='/dev/ttyUSB0',
	baudrate = 115200,
	parity=serial.PARITY_NONE,
	stopbits=serial.STOPBITS_ONE,
	bytesize=serial.EIGHTBITS,
	timeout=1
	)
counter=0
          
      
while 1:
	#ser.write('Write counter: %d \n'%(counter))
	ser.write(b'hello')
	time.sleep(1)
	counter += 1
