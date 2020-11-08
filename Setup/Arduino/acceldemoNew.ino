
// Basic demo for accelerometer readings from Adafruit LIS3DH

#include <Wire.h>
#include <Adafruit_LIS3DH.h>
#include <Adafruit_Sensor.h>

// For SD Card
#include <SPI.h>
#include <SD.h>

// IF USING SD CARD READER MAKE THIS VARIABLE TRUE
boolean usingSD = false;

File myFile;
const int chipSelect = 10; // Change to connection of CS pin on SD card module to Arduino


// Loop delay [ms] (affects data printing frequency)
int loopDelay = 250;

// I2C
Adafruit_LIS3DH lis = Adafruit_LIS3DH();

void setup(void) {
  Serial.begin(9600);
  while (!Serial) delay(10);     // will pause Zero, Leonardo, etc until serial console opens

  Serial.println("LIS3DH test + SD Card Test!");

  if (! lis.begin(0x18)) {   // change this to 0x19 for alternative i2c address
    Serial.println("LIS3DH Sensor Couldnt start");
    while (1) yield();
  }
  if (usingSD && !SD.begin()) {
    Serial.println("SD Card couldn't start");
    while (1) yield();
  }

  if (usingSD) {
    Serial.println("LIS3DH found and SD card found!");
  } else {
    Serial.println("LIS3DH found!");
  }
  
  // lis.setRange(LIS3DH_RANGE_4_G);   // 2, 4, 8 or 16 G!

if (usingSD) {
  // Opening file to write to
  myFile = SD.open("test.txt", FILE_WRITE);

  if (!myFile) {
    Serial.println("Something happened while trying to open test file!");
    while (1) yield();
  }
}

  Serial.print("Range = "); Serial.print(2 << lis.getRange());
  Serial.println("G");

  lis.setDataRate(LIS3DH_DATARATE_25_HZ);
  Serial.print("Data rate set to: ");
  switch (lis.getDataRate()) {
    case LIS3DH_DATARATE_1_HZ: Serial.println("1 Hz"); break;
    case LIS3DH_DATARATE_10_HZ: Serial.println("10 Hz"); break;
    case LIS3DH_DATARATE_25_HZ: Serial.println("25 Hz"); break;
    case LIS3DH_DATARATE_50_HZ: Serial.println("50 Hz"); break;
    case LIS3DH_DATARATE_100_HZ: Serial.println("100 Hz"); break;
    case LIS3DH_DATARATE_200_HZ: Serial.println("200 Hz"); break;
    case LIS3DH_DATARATE_400_HZ: Serial.println("400 Hz"); break;

    case LIS3DH_DATARATE_POWERDOWN: Serial.println("Powered Down"); break;
    case LIS3DH_DATARATE_LOWPOWER_5KHZ: Serial.println("5 Khz Low Power"); break;
    case LIS3DH_DATARATE_LOWPOWER_1K6HZ: Serial.println("16 Khz Low Power"); break;
  }

  Serial.print("Serial monitor data printing set to: ");
  Serial.print(loopDelay);
  Serial.println(" ms");

}


void loop() {
  lis.read();      // get X Y and Z data at once
  // Then print out the raw data
  Serial.print("X:  "); Serial.print(lis.x);
  Serial.print("  \tY:  "); Serial.print(lis.y);
  Serial.print("  \tZ:  "); Serial.print(lis.z);

  /* Or....get a new sensor event, normalized */
  sensors_event_t event;
  lis.getEvent(&event);

  /* Display the results (acceleration is measured in m/s^2) */
  Serial.print("\t\tX: "); Serial.print(event.acceleration.x);
  Serial.print(" \tY: "); Serial.print(event.acceleration.y);
  Serial.print(" \tZ: "); Serial.print(event.acceleration.z);
  Serial.println(" m/s^2 ");

  //kSerial.println();

  if (usingSD) {
    // Writing to the opened file
    myFile.print("\t\tX: "); myFile.print(event.acceleration.x);
    myFile.print(" \tY: "); myFile.print(event.acceleration.y);
    myFile.print(" \tZ: "); myFile.print(event.acceleration.z);
    myFile.println(" m/s^2 ");
  
    if (event.acceleration.y > 2) {
      myFile.close();
      Serial.println("FILE CLOSED");
    }

  }
  delay(loopDelay);
}
