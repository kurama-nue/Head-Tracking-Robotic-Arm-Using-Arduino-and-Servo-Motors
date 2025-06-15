#include <Servo.h>

Servo baseServo;      // X-axis (base rotation)
Servo shoulderServo;  // Y-axis (tilt up/down)
Servo elbowServo;     // optional - pin 4
Servo gripperServo;   // optional - pin 3

String inputString = "";
boolean newData = false;

void setup() {
  Serial.begin(9600);

  baseServo.attach(6);       // Base servo (X)
  shoulderServo.attach(5);   // Shoulder servo (Y)
  elbowServo.attach(4);      // Free for future
  gripperServo.attach(3);    // Free for future

  baseServo.write(90);
  shoulderServo.write(90);
}

void loop() {
  recvWithStartEndMarkers();
  if (newData) {
    parseData();
    newData = false;
  }
}

void recvWithStartEndMarkers() {
  static boolean recvInProgress = false;
  char startMarker = '<';
  char endMarker = '>';
  char rc;

  while (Serial.available() > 0 && newData == false) {
    rc = Serial.read();

    if (recvInProgress) {
      if (rc != endMarker) {
        inputString += rc;
      } else {
        recvInProgress = false;
        newData = true;
      }
    } else if (rc == startMarker) {
      inputString = "";
      recvInProgress = true;
    }
  }
}

void parseData() {
  int commaIndex = inputString.indexOf(',');
  if (commaIndex > 0) {
    int x = inputString.substring(0, commaIndex).toInt();
    int y = inputString.substring(commaIndex + 1).toInt();

    x = constrain(x, 0, 180);
    y = constrain(y, 0, 180);

    baseServo.write(x);        // Horizontal movement
    shoulderServo.write(y);    // Vertical movement
  }
}
