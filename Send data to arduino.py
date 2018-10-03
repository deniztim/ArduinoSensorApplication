# -*- coding: utf-8 -*-
"""
Created on Tue Oct  2 21:37:58 2018

@author: Deniz Timartas
"""

import serial
import time
import sys

ser = serial.Serial("COM3",9600,timeout=5);
time.sleep(1)

print("To read from the Distance Sensor, enter 1")
print("To read from other Sensor, enter 2")

SensorSelect = input("Which Sensor do you want to read?:")
#ser.write(SensorSelect)

if(SensorSelect=='1'):
    ser.write(str.encode('1'))
if(SensorSelect=='2'):
    ser.write(str.encode('2'))