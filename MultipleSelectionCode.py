import serial
import time
import json
import os

###Initialization###

LIGHTDENSITY = '4'
HUMIDITYANDWARMTH = '3'
WARMTH = '2'
DISTANCE = '1'
START = '0'
sensorSelect = 'NullSensor'
userSelection = 1
available_sensors=['Distance', 'Warmth', 'Light Density', 'Humidity', 'Warmth']

ser = serial.Serial("ACM0",9600,timeout=5); #Might be changed according to OS and USB setup
time.sleep(1)

###Configuration File Part###

if (os.path.exists('Config.json')==True):
    with open("Config.json", "r") as jsonfile:
        config_data = json.load(jsonfile)
    
    print("A Company Information file has been found!")
    print('Company Name:'+ config_data['Company'])
    print('Dept Name:'+ config_data['Dept'])
    print('Field of Work:'+ config_data['Field'])
    print("Machine's ID:"+ config_data['MachineId'])
    print('')
    
    Initialize = input("Do you want to set another Configuration file for your Company? Enter Y/N:")
    
    if (Initialize == 'Y'):
        os.remove('Config.json')
        
if (os.path.exists('Config.json')==False):
    print("Config file hasnt been initialized Please follow these steps")
    
    Company = input("Enter your company name:")
    Dept = input("Enter the Departments Name:")
    Field = input("Enter the field of work:")
    MachineId = input("Enter the Machine's ID:")
    
    Config = {
            'Company':Company,
            'Dept':Dept,
            'Field':Field,
            'MachineId':MachineId
            }
    json_dump = json.dumps(Config)
    f = open("Config.json","w")
    f.write(json_dump)
    f.close()
    
###Sensor Configuration File Part###
    
if (os.path.exists('Sensor_Config.json')==True):
    with open("Sensor_Config.json", "r") as jsonfile:
        sensor_data = json.load(jsonfile)
    
    print('')
    print("A config file has been found!")
    sensorlist = sensor_data['SensorSetup']
    print('Sensors Setup:')
    print(sensorlist)
    print('')
    
    Initialize = input("Do you want to set another Configuration file for your Sensors? Enter Y/N:")
    
    if (Initialize == 'Y'):
        os.remove('Sensor_Config.json')
        
if (os.path.exists('Sensor_Config.json')==False):
    print("")
    print("There isny any Sensor Information at the moment. Please proceed to selecting Sensors.")
    print("Please Select the Sensors you want to setup")

    print("The sensors available are: ")
    print(available_sensors)
    print("To Start Processing, enter 'Start'")
    print("What do you want to measure?:")
    
    sensorSelect=[]

    while userSelection != 'Start':
        userSelection = input(":->")
        
        if(userSelection=='Distance'):
            sensorSelect.append('Distance')
        
        if(userSelection=='Warmth'):
            sensorSelect.append('Warmth')
            
        if(userSelection=='Humidity and Warmth'):
            sensorSelect.append('Humidity and Warmth')
            
        if(userSelection=='Light Density'):
            sensorSelect.append('Light Density')
            
        if(userSelection=='Start'):
            sensorSelect.append(START)
    
    sensorselect = {
        'SensorSetup':sensorSelect
        }
    
    json_dump = json.dumps(sensorselect)
    f = open("Sensor_Config.json","w")
    f.write(json_dump)
    f.close()
    
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
        
write_to_file_path_garbage = "GarbageData.txt";
output_file_garbage = open(write_to_file_path_garbage, "w");

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
