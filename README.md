# OIP-Pi-Arduino-UART
UART source code for Raspberry Pi and Arduino Mega communication in Design Project

### Steps to use the code
This Python repository makes use of virtual environments so it assumes that you have installed the `virtualenv` package.

Thereafter, follow the sequence of steps below.
1. `cd` into the repository
2. `source ./bin/activate`
3. `pip install -r requirements.txt`

Finally, ensure that the Raspberry Pi has an existing connection to the Arduino Mega via the serial ports either using USB or GPIO pins.

To run the program: `python sterilize.py`

Custom port names can be used such as `/dev/serial0` or `/dev/ttyS0` as necessary. The default value in this script is `/dev/ttyACM0`.
To run with a specific port: `python sterilize.py -port '/dev/ttyS0'`

Or, to run without initialising a port: `python sterilize.py -no-port`
