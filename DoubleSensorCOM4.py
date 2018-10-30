import serial
import time
import json
import os
import sys
from serial import SerialException

###Initialization###

LIGHTDENSITY = '4'
HUMIDITYANDWARMTH = '3'
WARMTH = '2'
DISTANCE = '1'
START = '0'
sensorSelect = 'NullSensor'
userSelection = 1
available_sensors=['Distance', 'Warmth', 'Light Density', 'Humidity', 'Warmth']

try:
    ser = serial.Serial("COM4",9600,timeout=5); #Might be changed according to OS and USB setup
    time.sleep(1)
except SerialException:
    print('There is no arduino connected!')
    sys.exit('Connect a device!')

    
###Serial Data Send TO Arduino###

with open("Sensor_Config.json", "r") as jsonfile:
    sensor_data = json.load(jsonfile)
    sensorlist = sensor_data['SensorSetup']
    
sensorcount = 0
while len(sensorlist) > sensorcount:
    if(sensorlist[sensorcount]=='Distance'):
        ser.write(str.encode(DISTANCE))
        
    if(sensorlist[sensorcount]=='Warmth'):
        ser.write(str.encode(WARMTH))
  
    if(sensorlist[sensorcount]=='Humidity and Warmth'):
        ser.write(str.encode(HUMIDITYANDWARMTH))
        
    if(sensorlist[sensorcount]=='Light Density'):
        ser.write(str.encode(LIGHTDENSITY))
        
    if(sensorlist[sensorcount]=='0'):
        break
    sensorcount=sensorcount+1
        
    
while True and ser.isOpen():
    try:
        line = ser.readline()
        line = line.decode("utf-8") #ser.readline returns a binary, convert to string
        print(line)

            
    except KeyboardInterrupt:
        print("Keyboard Interrupt")
        ser.close()
        break
