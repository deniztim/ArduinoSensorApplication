import serial
import time
from os import system

WARMTH = '2'
DISTANCE = '1'
START = '0'
sensorSelect = 'NullSensor'

ser = serial.Serial("COM3",9600,timeout=5);
time.sleep(1)


print("To read from the Distance Sensor, enter 'Distance'")
print("To read from the Warmth Sensor, enter 'Warmth'")
print("To Start Process, enter 'Start'")

while sensorSelect != "Start":
    sensorSelect = input("What do you want to measure?:")
    if(sensorSelect=='Distance'):
        ser.write(str.encode(DISTANCE))
    
    if(sensorSelect=='Warmth'):
        ser.write(str.encode(WARMTH))
        
    if(sensorSelect=='Start'):
        break
        
write_to_file_path_distance = "distanceOutput.txt";
output_file_distance = open(write_to_file_path_distance, "w");

write_to_file_path_warmth = "warmthOutput.txt";
output_file_warmth = open(write_to_file_path_warmth, "w");


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
