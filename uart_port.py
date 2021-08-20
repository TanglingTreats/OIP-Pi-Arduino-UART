import sys
import time
import serial

class Serial_Port():
    def __init__(self, port_name='/dev/ttyS0', baudrate=9600, 
            parity_bit=serial.PARITY_NONE, stop_bits=serial.STOPBITS_ONE,
            byte_size=serial.EIGHTBITS, timeout=1):

        self.ser = serial.Serial(port=port_name, baudrate=baudrate, 
                parity=parity_bit, stopbits=stop_bits, bytesize=byte_size, timeout=timeout)

    def writeSerialMessage(self, message):
        self.ser.write(message.encode())

    def getSerialMessage(self):
        return self.ser.readline().decode()[:-2]

        

if(__name__ == "__main__"):
    option = sys.argv[1]
    print(option)
    ser = Serial_Port()
    while 1 :
        if option == "tx":
            ser.writeSerialMessage('Hello \n')
        if option == "rx":
            ser.getSerialMessage()
        time.sleep(1)
