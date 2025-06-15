# 🤖 Head Tracking Robotic Arm Using Arduino Uno

This project demonstrates a simple yet effective **head-tracking robotic arm** built using an **Arduino Uno**, **4 DOF robotic arm**, and a **laptop webcam** (instead of OV7670, which was not functional). The robotic arm mimics head movements by detecting face position using Python and OpenCV, and transmits the data via serial to Arduino for servo actuation.

---

## 🚀 Features

- 👀 **Real-Time Head Tracking** using laptop webcam and OpenCV
- 🦾 **4 DOF Robotic Arm Control** using servo motors
- 🔌 **External Power Management** for stable servo operation
- 💬 **Serial Communication** between Python (PC) and Arduino
- 💡 Modular code design with facial detection and servo actuation split into separate scripts

---

## 🛠️ Components Used

- Arduino Uno
- 4x Servo Motors (SG90 or MG90S)
- Laptop Webcam
- Breadboard and jumper wires
- 5V External Power Supply (Battery pack or adapter)
- (Optional) PCA9685 Servo Driver for enhanced servo control

---

## 📦 How It Works

1. **Face Detection on PC:** A Python script using OpenCV detects the user’s face and calculates X/Y coordinates and size.
2. **Position Mapping:** The position is mapped to servo angles (base, shoulder, elbow).
3. **Serial Communication:** Values are sent from Python to Arduino Uno over serial.
4. **Servo Control:** The Arduino reads these values and moves the servos to track the detected face.

---

## 📂 Files Included

```
facedetection.py       --> Simple OpenCV face detection with bounding box
facetracking.py        --> Advanced tracking + angle mapping + serial output
facetracking.ino       --> Arduino code to receive data and control servos
haarcascade_frontalface_default.xml  --> Face detection model for OpenCV
```

---

## 💾 Requirements and Setup

### 🔧 Python Libraries

Install the required libraries using pip:

```bash
pip install opencv-python
pip install cvzone
pip install numpy
pyserial
```

> Make sure Python is installed. Use `python --version` to check.

### 📁 How to Open the Project

1. **Connect Arduino Uno** and upload `facetracking.ino` using the Arduino IDE.
2. **Download Python dependencies** using the pip commands above.
3. **Place **`` in the same folder as the Python scripts.
4. **Run Python Script:**
   - For basic face detection: `python facedetection.py`
   - For tracking and servo control: `python facetracking.py`
5. **Ensure the correct COM port** is selected in `facetracking.py` (e.g., `COM7`).
6. **Press **`` to exit the webcam window.

---

## 📸 Demo

> *Add a GIF or YouTube video link here showing the robotic arm tracking your face using the webcam.*

---

## 📁 Folder Structure

```
/Arduino_Code        --> facetracking.ino
/Webcam_Tracking     --> facedetection.py, facetracking.py
/Model               --> haarcascade_frontalface_default.xml
/Schematics          --> Circuit diagram and wiring images
/Hardware_Setup      --> Images and descriptions of physical build
```

---

## 🔋 Power Management Tips

- Always use an external 5V power source for servo motors.
- Connect Arduino GND and external power GND together.
- Add capacitors (470µF or more) on breadboard rails to handle voltage drops.

---

## 💬 Contributions

Pull requests, ideas, and suggestions are welcome! Whether it's improving the tracking logic, switching to wireless serial, or enhancing detection — feel free to contribute!

---

## 📄 License

This project is open-source under the MIT License. Feel free to use, modify, and share.

