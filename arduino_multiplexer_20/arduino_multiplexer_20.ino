#include <Arduino.h>

/* application
PIN
  D2 --- A
  D3 --- B
  D4 --- C
  A0 --- COM1 (0 - 7)
  A1 --- COM2 (8 - 15)
  A2 --- COM3 (16 - 23)
*/

#define PLOT_MODE

int sensorValue[22];
const int numSns = 24;
byte BinaryData[27] = {65.0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,90};

void setup() {
    pinMode(2, OUTPUT);
    pinMode(3, OUTPUT);
    pinMode(4, OUTPUT);
    // overflow
    // analogReference(INTERNAL);
    Serial.begin(57600);
}

void loop() {
  int value = 0;
//  get
  for (int i = 0; i <7; i++) {
      digitalWrite(2, i % 2);
      digitalWrite(3, (i / 2) % 2);
      digitalWrite(4, (i / 4) % 2);
      // wait
      delay(1);

      sensorValue[i] = analogRead(A0);
//      delay(3);
      sensorValue[8 + i] = analogRead(A1);
//      delay(3);
      if(i!=6) sensorValue[16 + i] = analogRead(A2);
  }
  
  BinaryData[1] = ((sensorValue[0] >> 2) & 0xff);
  BinaryData[2] = ((sensorValue[1] >> 2) & 0xff);
  BinaryData[3] = ((sensorValue[2] >> 2) & 0xff);
  BinaryData[4] = ((sensorValue[3] >> 2) & 0xff);
  BinaryData[5] = ((sensorValue[4] >> 2) & 0xff);
  BinaryData[6] = ((sensorValue[5] >> 2) & 0xff);
  BinaryData[7] = ((sensorValue[6] >> 2) & 0xff);

  BinaryData[8] = ((sensorValue[8] >> 2) & 0xff);
  BinaryData[9] = ((sensorValue[9] >> 2) & 0xff);
  BinaryData[10] = ((sensorValue[10] >> 2) & 0xff);
  BinaryData[11] = ((sensorValue[11] >> 2) & 0xff);
  BinaryData[12] = ((sensorValue[12] >> 2) & 0xff);
  BinaryData[13] = ((sensorValue[13] >> 2) & 0xff);
  BinaryData[14] = ((sensorValue[14] >> 2) & 0xff);

  BinaryData[15] = ((sensorValue[16] >> 2) & 0xff);
  BinaryData[16] = ((sensorValue[17] >> 2) & 0xff);
  BinaryData[17] = ((sensorValue[18] >> 2) & 0xff);
  BinaryData[18] = ((sensorValue[19] >> 2) & 0xff);
  BinaryData[19] = ((sensorValue[20] >> 2) & 0xff);
  BinaryData[20] = ((sensorValue[21] >> 2) & 0xff);


  BinaryData[21] = (((sensorValue[0] & 0x03) << 0)
                  + ((sensorValue[1] & 0x03) << 2)
                  + ((sensorValue[2] & 0x03) << 4)
                  + ((sensorValue[3] & 0x03) << 6));
  BinaryData[22] = (((sensorValue[4] & 0x03) << 0)
                  + ((sensorValue[5] & 0x03) << 2)
                  + ((sensorValue[6] & 0x03) << 4)
                  + ((sensorValue[8] & 0x03) << 6));
  BinaryData[23] = (((sensorValue[9] & 0x03) << 0)
                  + ((sensorValue[10] & 0x03) << 2)
                  + ((sensorValue[11] & 0x03) << 4)
                  + ((sensorValue[12] & 0x03) << 6));
  BinaryData[24] = (((sensorValue[13] & 0x03) << 0)
                  + ((sensorValue[14] & 0x03) << 2)
                  + ((sensorValue[16] & 0x03) << 4)
                  + ((sensorValue[17] & 0x03) << 6));
  BinaryData[25] = (((sensorValue[18] & 0x03) << 0)
                  + ((sensorValue[19] & 0x03) << 2)
                  + ((sensorValue[20] & 0x03) << 4)
                  + ((sensorValue[21] & 0x03) << 6));
  //Serial.write(((sensorValue[20] & 0x03) << 0)
  //                + ((sensorValue[21] & 0x03) << 2)
  //                + ((sensorValue[22] & 0x03) << 4)
  //                + ((sensorValue[23] & 0x03) << 6));
  Serial.write(BinaryData, 27);
}
