#include <SPI.h>
#include <Adafruit_GFX.h>
#include <Adafruit_PCD8544.h>
#include <dht11.h>

int LDRPin = 1;
int tempPin = 0;
byte trigger = 10;
byte echo = 11;
Adafruit_PCD8544 display = Adafruit_PCD8544(4, 5, 6, 7, 8);

dht11 DHT11;
int tempVal;
int SelectionArray[8];
int i = 0;
unsigned long travelTime;
double totalDistance; 
int distance; 
int data;
int LDRValue = 0;

void setup()
{
  pinMode(trigger, OUTPUT);
  pinMode(echo, INPUT);
  Serial.begin(9600); 
  display.begin();
  display.setContrast(80);  /* Initializes the display. Sets SPI freq, SPI data mode, Bit order */
  display.setTextColor(BLACK); /* Color of text*/
  display.clearDisplay();  /* Clears the screen and buffer */  
  display.setCursor(13,5);  /* Set x,y coordinates */
  display.setTextSize(1); /* Select font size of text. Increases with size of argument. */
  display.println("Awaiting");
  display.setCursor(7,15);
  display.println("Selection...");
  display.display();
  delay(500);
}

void loop()
{
  display.clearDisplay();
  while (Serial.available())
  {
    data=Serial.read();
    SelectionArray[i]=data;
    i++;
  }
  for (int count = 0 ; count < i ; count++)
  {
    if (SelectionArray[count] == '1')
    {
      SetupDistance();
    }
    else if (SelectionArray[count] == '2')
    {
      SetupTemparature();
    }
    else if (SelectionArray[count] == '3')
    {
      SetupHumidityWarmth();
    }
    else if (SelectionArray[count] == '4')
    {
      SetupLDR();
    }
  }
    
    delay(500);
}

void SetupTemparature()
{
  display.setCursor(5,27);
  tempVal = analogRead(tempPin);
  float mv = ( tempVal/1024.0)*5000; 
  float cel = mv/10;
  
  Serial.print("\nC ");
  Serial.println(cel);
  display.println("C: ");
  display.setCursor(20,27);
  display.print(cel);
  display.display();
  delay(500);
}
  
void SetupDistance()
{
  display.setCursor(5,14);
  digitalWrite(trigger, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigger, LOW);

  travelTime = pulseIn(echo, HIGH);

  totalDistance = (double)travelTime*0.034;
  distance = totalDistance / 2;
  
  Serial.print("\ncm ");
  Serial.println(distance);
  display.println("Cm: ");
  display.setCursor(20,14);
  display.print(distance);
  display.display();
  delay(500);
}

void SetupHumidityWarmth()
{
  DHT11.attach(9);
  int chk = DHT11.read();
  Serial.print("\nHumidity: ");
  Serial.println((double)DHT11.humidity, 9);
  delay(50);
  Serial.print("\nTemparature: ");
  Serial.println((double)DHT11.temperature, 9);
  delay(50);
  Serial.print("\nDewPoint: ");
  Serial.println(DHT11.dewPoint(), 9);
  delay(500);
}

void SetupLDR()
{
  display.setCursor(5,5);
  LDRValue = analogRead(LDRPin);
  Serial.print("\nLightDensity: ");
  Serial.println(LDRValue);
  display.println("\nLight: ");
  display.setCursor(35,5);
  display.print(LDRValue);
  display.display();
  delay(500);
}
