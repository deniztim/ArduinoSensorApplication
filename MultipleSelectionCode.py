import serial
import time
from os import system

LIGHTDENSITY = '4'
HUMIDITYANDWARMTH = '3'
WARMTH = '2'
DISTANCE = '1'
START = '0'
sensorSelect = 'NullSensor'

ser = serial.Serial("COM3",9600,timeout=5);
time.sleep(1)


print("To read from the Distance Sensor, enter 'Distance'")
print("To read from the Warmth Sensor, enter 'Warmth'")
print("To read from the Light Density Sensor, enter 'Light Density'")
print("To read from the Humidity and Warmth Sensor, enter 'Humidity and Warmth'")
print("To Start Process, enter 'Start'")

while sensorSelect != "Start":
    sensorSelect = input("What do you want to measure?:")
    if(sensorSelect=='Distance'):
        ser.write(str.encode(DISTANCE))
    
    if(sensorSelect=='Warmth'):
        ser.write(str.encode(WARMTH))
        
    if(sensorSelect=='Humidity and Warmth'):
        ser.write(str.encode(HUMIDITYANDWARMTH))
        
    if(sensorSelect=='Light Density'):
        ser.write(str.encode(LIGHTDENSITY))
        
    if(sensorSelect=='Start'):
        break
        
write_to_file_path_garbage = "GarbageData.txt";
output_file_garbage = open(write_to_file_path_garbage, "w");

write_to_file_path_distance = "distanceOutput.txt";
output_file_distance = open(write_to_file_path_distance, "w");

write_to_file_path_warmth = "warmthOutput.txt";
output_file_warmth = open(write_to_file_path_warmth, "w");

write_to_file_path_humidity = "humidityOutput.txt";
output_file_humidity = open(write_to_file_path_humidity, "w");

write_to_file_path_lightDensity = "lightDensityOutput.txt";
output_file_lightDensity = open(write_to_file_path_lightDensity, "w");

while True:
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
