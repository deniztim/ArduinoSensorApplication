#include <SPI.h>
#include <Adafruit_GFX.h>
#include <Adafruit_PCD8544.h>

byte trigger = 10;
byte echo = 11;

int tempVal;
int tempPin = 0;
int SelectionArray[3];
int i = 0;
unsigned long travelTime;
double totalDistance; 
int distance; 
int data;
Adafruit_PCD8544 display = Adafruit_PCD8544(4, 5, 6, 7, 8);

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
  }
    
    delay(1000);
}

void SetupTemparature()
{
  display.setCursor(5,27);
  tempVal = analogRead(tempPin);
  float mv = ( tempVal/1024.0)*5000; 
  float cel = mv/10;
  
  Serial.print(cel);
  Serial.println(" C\n");
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
  
  Serial.print(distance);
  Serial.println(" cm\n");
  display.println("Cm: ");
  display.setCursor(20,14);
  display.print(distance);
  display.display();
  delay(500);
}
