#include <SPI.h>
#include <Adafruit_GFX.h>
#include <Adafruit_PCD8544.h>

byte trigger = 10;
byte echo = 11;

int i=0;
int SelectionArray[16];
unsigned long sure;
double toplamYol; 
int aradakiMesafe; 
int data;
Adafruit_PCD8544 display = Adafruit_PCD8544(4, 5, 6, 7, 8);

void setup() {
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
  while (Serial.available())
  {
  data=Serial.read();
  SelectSensorArray();
   }
   
}

void SetupOther(){
    Serial.print("I am not setup yet.\n");
    delay(2000);
  }
  
void SetupDistance(){
  digitalWrite(trigger, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigger, LOW);

  sure = pulseIn(echo, HIGH);

  toplamYol = (double)sure*0.034;
  aradakiMesafe = toplamYol / 2;
  
  Serial.print(sure);
  Serial.println(" mikro saniye");

  Serial.print(toplamYol);
  Serial.println(" cm.");
  
  Serial.print(aradakiMesafe);
  Serial.println(" cm.\n");
  display.clearDisplay();
  display.setCursor(28,15);
  display.println(aradakiMesafe);
  display.display();
  delay(2000);
  }
  
void SelectSensorArray()
 {
  SelectionArray[i] = data;
  i++;
  }
void SetupSelected()
{
  for(int count =  0 ; count < i ; count++)
   {
    if (SelectionArray[count] == '1')
    {
      SetupDistance();
    }
    else if (SelectionArray[count] == '2')
    {
      SetupOther();
    }
}
