# ArduinoSensorApplication

This is currently an Arduino Uno application. The sensors currently available as of this version are Warmth(LM35), Distance(HC-SR04), Humidity and Warmth(DHT11) and LDR.
LCD view of Centigrats and Centimeters measured are available.

When run, Python code first asks you to configurate settings. Then everytime it opens, it gives you a chance to use the existing config files.
The data received is currently sent to a local server using a simple requests() function.
