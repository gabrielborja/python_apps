import time
import serial

device = 'COM3' #port is a device name according to the operating system. e.g. /dev/ttyUSB0 on GNU/Linux or COM3 on Windows.

try:
    arduino = serial.Serial(port=device, baudrate=9600, bytesize=8)
    print('Connection OK')
except:
  print("Cannot read port")

while True:
  port_data = arduino.readline()
  port_data = port_data.decode('utf-8').strip()
  
  print(port_data)