# UART Receiver script on Pi4
# Serial port should be changed

import time
import serial
ser=serial.Serial(port='/dev/ttyAMA0', baudrate=9600, parity=serial.PARITY_NONE, stopbits=serial.STOPBITS_ONE, bytesize=serial.EIGHTBITS, timeout=1)

while 1:
    x=ser.readline().decode()[:-2]
    print(x)
