import serial
import time
import json
import os

LIGHTDENSITY = '4'
HUMIDITYANDWARMTH = '3'
WARMTH = '2'
DISTANCE = '1'
START = '0'
sensorSelect = 'NullSensor'
userSelection = 1

ser = serial.Serial("/dev/ttyACM0",9600,timeout=5);
time.sleep(1)

Something = input("Do you want to set another Configuration file for your Sensors? Enter Y/N:")
if (Something == 'Y'):
    if (os.path.exists('Config.json')==True):
        os.remove('Config.json')

if (os.path.exists('Config.json')==False):
    
    Company = input("Enter your company name:")
    Dept = input("Enter the Departments Name:")
    Field = input("Enter the field of work:")
    MachineId = input("Enter the Machine's ID:")
    
    print("The sensors available are: Distance, Warmth, Light Density, Humidity and Warmth")
    print("To Start Processing, enter 'Start'")
    print("What do you want to measure?:")
    
    sensorSelect=[]
    count = 0
    while userSelection != 'Start':
        userSelection = input(":->")
        
        if(userSelection=='Distance'):
            sensorSelect.append(DISTANCE)
        
        if(userSelection=='Warmth'):
            sensorSelect.append(WARMTH)
            
        if(userSelection=='Humidity and Warmth'):
            sensorSelect.append(HUMIDITYANDWARMTH)
            
        if(userSelection=='Light Density'):
            sensorSelect.append(LIGHTDENSITY)
            
        if(userSelection=='Start'):
            sensorSelect.append(START)
        
    count=count+1
    
    Config = {
            'Company':Company,
            'Dept':Dept,
            'Field':Field,
            'MachineId':MachineId,
            'SensorSetup':sensorSelect
            }
    
    json = json.dumps(Config)
    f = open("Config.json","w")
    f.write(json)
    f.close()

sensorcount = 0
while sensorSelect[sensorcount] != 0:
    if(sensorSelect[sensorcount]=='Distance'):
        ser.write(str.encode(DISTANCE))
    
    if(sensorSelect[sensorcount]=='Warmth'):
        ser.write(str.encode(WARMTH))
        
    if(sensorSelect[sensorcount]=='Humidity and Warmth'):
        ser.write(str.encode(HUMIDITYANDWARMTH))
        
    if(sensorSelect[sensorcount]=='Light Density'):
        ser.write(str.encode(LIGHTDENSITY))
        
    if(sensorSelect=='Start'):
        break
    sensorcount=sensorcount+1
        
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
