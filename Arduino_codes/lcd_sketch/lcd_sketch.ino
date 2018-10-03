#include <SPI.h>
#include <Adafruit_GFX.h>
#include <Adafruit_PCD8544.h>

// Software SPI (slower updates, more flexible pin options):
// pin 13 - Serial clock out (SCLK)
// pin 11 - Serial data out (DIN)
// pin 8 - Data/Command select (D/C)
// pin 7 - LCD chip select (CS)
// pin 9 - LCD reset (RST)
Adafruit_PCD8544 display = Adafruit_PCD8544(4, 5, 6, 7, 8);

void setup()   {
  display.begin();

  display.setContrast(50);  /* Initializes the display. Sets SPI freq, SPI data mode, Bit order */

  display.clearDisplay();  /* Clears the screen and buffer */  

  display.setCursor(13,5);  /* Set x,y coordinates */
  display.setTextSize(1); /* Select font size of text. Increases with size of argument. */
  display.setTextColor(BLACK); /* Color of text*/
  display.println("Electronic"); /* Text to be displayed */
  display.setCursor(28,15);
  display.println("Wings");
  display.display();
  delay(500);
}

void loop() {  
  display.clearDisplay();
  display.drawBitmap(0, 0, Smiley_1, 84, 48, 1);
  display.display();
  delay(300);
  display.clearDisplay();
  display.drawBitmap(0, 0, Smiley_2, 84, 48, 1);
  display.display();
  delay(300);
  display.clearDisplay();
  display.drawBitmap(0, 0, Smiley_3, 84, 48, 1);
  display.display();
  delay(300);
  display.clearDisplay();
  display.drawBitmap(0, 0, Smiley_4, 84, 48, 1);
  display.display();
  delay(300);
}
