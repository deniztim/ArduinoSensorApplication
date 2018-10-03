# -*- coding: utf-8 -*-
"""
Created on Tue Oct  2 21:37:58 2018

@author: Deniz Timartas
"""

import serial
import time
import sys

OTHER = '2'
DISTANCE = '1'
ser = serial.Serial("COM3",9600,timeout=5);
time.sleep(1)


print("To read from the Distance Sensor, enter 'Distance'")
print("To read from other Sensor, enter 'Other'")

SensorSelect = input("What do you want to measure?:")
#ser.write(SensorSelect)

if(SensorSelect=='Distance'):
    write_to_file_path = "DistanceOutput.txt";
    output_file = open(write_to_file_path, "a");
    ser.write(str.encode(DISTANCE))
    while True:
        try:
            line = ser.readline();
            line = line.decode("utf-8") #ser.readline returns a binary, convert to string
            print(line);
            output_file.write(line);
        except:
            print("Keyboard Interrupt")
            break

if(SensorSelect=='Other'):
    write_to_file_path = "OtherOutput.txt";
    output_file = open(write_to_file_path, "a");
    ser.write(str.encode(OTHER))
    while True:
        try:
            line = ser.readline();
            line = line.decode("utf-8") #ser.readline returns a binary, convert to string
            print(line);
            output_file.write(line);
        except:
            print("Keyboard Interrupt")
            break