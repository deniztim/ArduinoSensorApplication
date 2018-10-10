# -*- coding: utf-8 -*-
"""
Created on Fri Oct  5 18:29:50 2018

@author: Deniz Timartas
"""

import serial
import time

WARMTH = '2'
DISTANCE = '1'

ser = serial.Serial("COM3",9600,timeout=5);
time.sleep(1)


write_to_file_path_distance = "DistanceOutput.txt";
output_file_distance = open(write_to_file_path_distance, "w");

write_to_file_path_other = "WarmthOutput.txt";
output_file_warmth = open(write_to_file_path_other, "w");


while True:
    try:
        line = ser.readline()
        line = line.decode("utf-8") #ser.readline returns a binary, convert to string
        print(line)
        if " cm" in line:
            output_file_distance.write(line)
        else:
            output_file_warmth.write(line)
    except KeyboardInterrupt:
        print("Keyboard Interrupt")
        ser.close()
        break