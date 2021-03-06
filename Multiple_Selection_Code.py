# -*- coding: utf-8 -*-
"""
Created on Tue Oct 30 16:28:48 2018

@author: Deniz Timartas
"""
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
    ser = serial.Serial("/dev/tty/ACM0",9600,timeout=5); #Might be changed according to OS and USB setup
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
        write_to_file_path_distance = "distanceOutput.txt"
        output_file_distance = open(write_to_file_path_distance, "w")
        
    if(sensorlist[sensorcount]=='Warmth'):
        ser.write(str.encode(WARMTH))
        write_to_file_path_warmth = "warmthOutput.txt"
        output_file_warmth = open(write_to_file_path_warmth, "w")
        
    if(sensorlist[sensorcount]=='Humidity and Warmth'):
        ser.write(str.encode(HUMIDITYANDWARMTH))
        write_to_file_path_humidity = "humidityOutput.txt"
        output_file_humidity = open(write_to_file_path_humidity, "w")
        
    if(sensorlist[sensorcount]=='Light Density'):
        ser.write(str.encode(LIGHTDENSITY))
        write_to_file_path_lightDensity = "lightDensityOutput.txt"
        output_file_lightDensity = open(write_to_file_path_lightDensity, "w")
        
    if(sensorlist[sensorcount]=='0'):
        break
    sensorcount=sensorcount+1
        

while True and ser.isOpen():
    try:
        line = ser.readline()
        line = line.decode("utf-8") #ser.readline returns a binary, convert to string
        print(line)
        if "cm " in line:
            output_file_distance.write(line)
        if "C " in line:
            output_file_warmth.write(line)
        if "Humidity: " in line:
            output_file_humidity.write(line)
        if "Temperature: " in line:
            output_file_humidity.write(line)
        if "DewPoint: " in line:
            output_file_humidity.write(line)
        if "LightDensity: " in line:
            output_file_lightDensity.write(line)
        else:
            output_file_garbage.write(line)
    except KeyboardInterrupt:
        print("Keyboard Interrupt")
        ser.close()
        break