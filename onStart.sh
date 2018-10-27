#!/bin/bash
# Start script for arduino sensor app 
#author: R U hi!?
echo Hardwarecheck
sleep 3s
echo Done
sleep 1s
sudo apt-get update
sudo apt-get upgrade
source ENV_arSens/bin/activate
cd ArduinoSensorApplication
pip install requirements.txt

python MultipleSelectionCode.py 
