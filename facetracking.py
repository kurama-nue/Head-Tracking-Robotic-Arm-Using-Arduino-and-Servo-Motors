import cv2
from cvzone.FaceDetectionModule import FaceDetector
import numpy as np
import serial
import time

# Connect to Arduino on COM7
try:
    arduino = serial.Serial('COM7', 9600)
    time.sleep(2)
except Exception as e:
    print(f"Failed to connect to Arduino: {e}")
    exit()

# Setup webcam
cap = cv2.VideoCapture(0)
ws, hs = 1280, 720
cap.set(3, ws)
cap.set(4, hs)

detector = FaceDetector()

while True:
    success, img = cap.read()
    img, bboxs = detector.findFaces(img, draw=False)

    if bboxs:
        fx, fy = bboxs[0]["center"]
        bbox = bboxs[0]["bbox"]
        w = bbox[2]  # Width of the face box

        # Map face X/Y to base/shoulder servo
        servoX = int(np.interp(fx, [0, ws], [0, 180]))
        servoY = int(np.interp(fy, [0, hs], [180, 0]))

        # Map distance to elbow position
        # Closer face = larger bbox width → retract arm (lower angle)
        # Farther face = smaller bbox width → extend arm (higher angle)
        elbow = int(np.interp(w, [80, 250], [160, 60]))  # Adjust range if needed

        # Clamp all values
        servoX = np.clip(servoX, 0, 180)
        servoY = np.clip(servoY, 0, 180)
        elbow = np.clip(elbow, 60, 160)

        # Send to Arduino
        data = f"<{servoX},{servoY},{elbow}>"
        arduino.write(data.encode())

        # Draw info
        cv2.circle(img, (fx, fy), 80, (0, 255, 0), 2)
        cv2.putText(img, f"Arm: {elbow}", (fx + 10, fy - 50), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), 2)

    else:
        cv2.putText(img, "NO FACE DETECTED", (800, 50), cv2.FONT_HERSHEY_PLAIN, 3, (0, 0, 255), 3)

    cv2.imshow("Face Tracking", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
