# UART Transmitter script on RPi3

import time
import serial

ser = serial.Serial(port='/dev/ttyS0', baudrate = 9600, parity = serial.PARITY_NONE, stopbits=serial.STOPBITS_ONE, bytesize=serial.EIGHTBITS, timeout=1)

while 1 :
    ser.write('Hello \n'.encode())
    time.sleep(1)
