#include <LiquidCrystal_I2C.h>
#include <Wire.h>

LiquidCrystal_I2C lcd(0x27, 16, 2); // set the LCD address to 0x27 for a 16 chars and 2 line display

void setup() {
  Serial.begin(9600);
  pinMode(13, OUTPUT);

  //--------------------Display-------------------------------
  lcd.init();       // initialize the lcd 
  lcd.backlight();
  //----------------------------------------------------------------

  // Display on the display start
  lcd.setCursor(3, 0);
  lcd.print("MONITORING");
  lcd.setCursor(0, 1);
  lcd.print("No Signal Found!");
  // Display on the display end
}

void loop() {
  Serial.println("What is the speed limit");
  while (Serial.available() == 0) {
    // Wait for input
  }

  int speed_limit = Serial.parseInt();

  if (speed_limit == -1) {
    lcd.clear();
    digitalWrite(13, HIGH);  // turn the LED on (HIGH is the voltage level)
    lcd.setCursor(2, 1);
    lcd.print("Signal Found!");
    delay(1000);
    // Buzzer Starts
    delay(1000);            // wait for a second
    digitalWrite(13, LOW);  // turn the LED off by making the voltage LOW
    delay(1000);            // wait for a second
    // Buzzer Ends
    lcd.clear();
  } else if (speed_limit > 0) {
    // Buzzer Starts
    for (int i = 0; i < 2; i++) {
      digitalWrite(13, HIGH);  // turn the LED on (HIGH is the voltage level)
      delay(90);               // wait for a second
      digitalWrite(13, LOW);   // turn the LED off by making the voltage LOW
      delay(90);               // wait for a second
    }
    // Buzzer Ends

    // Display on the display start
    lcd.clear();
    delay(1000);
    lcd.setCursor(2, 0);
    lcd.print("Speed Limit");
    lcd.setCursor(2, 1);
    lcd.print("Processing");
    delay(3000);
    lcd.clear();
    delay(1000);
    lcd.setCursor(1, 0);
    lcd.print("Reducing Speed");
    lcd.setCursor(2, 1);
    lcd.print(String(speed_limit) + "Kmph");
    delay(4000);
    lcd.clear();
    delay(1000);
    // Display on the display end

    // Buzzer Starts
    for (int i = 0; i < 2; i++) {
      digitalWrite(13, HIGH);  // turn the LED on (HIGH is the voltage level)
      delay(90);               // wait for a second
      digitalWrite(13, LOW);   // turn the LED off by making the voltage LOW
      delay(90);               // wait for a second
    }
    // Buzzer Ends
  }
}
