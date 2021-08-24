import sys
import os
import time
import serial

class Serial_Port():
    def __init__(self, port_name='/dev/ttyS0', baudrate=9600, 
            parity_bit=serial.PARITY_NONE, stop_bits=serial.STOPBITS_ONE,
            byte_size=serial.EIGHTBITS, timeout=1):

        os.write("sudo chmod 777 /dev/ttyS0")
        self.port_name = port_name
        self.ser = serial.Serial(port=port_name, baudrate=baudrate, 
                parity=parity_bit, stopbits=stop_bits, bytesize=byte_size, timeout=timeout)
        self.ser.flush()

    def write_serial_message(self, message):
        print(f'Writing to {self.port_name} {message}')
        self.ser.write(message.encode('utf-8'))

    def get_serial_message(self):
        return self.ser.readline().decode('utf-8').rstrip()

    def has_message(self):
        return (self.ser.in_waiting > 0)
        

if(__name__ == "__main__"):
    option = sys.argv[1]

    ser = Serial_Port()

    number_of_args = len(sys.argv)
    if number_of_args > 2 :
        device_type = sys.argv[2]
        if device_type == "pi4":
            ser=Serial_Port(port_name='/dev/ttyAMA0')

    while 1 :
        if option == "tx":
            ser.write_serial_message('1')
        if option == "rx":
            message = ser.get_serial_message()
            print(message)
        time.sleep(1)
