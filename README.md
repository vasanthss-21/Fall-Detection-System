# 🧠 Fall Detection System using Raspberry Pi 4, ESP32 & Twilio API

A smart IoT-based **Fall Detection System** designed to monitor elderly people and immediately alert caretakers via **SMS notification** when a fall is detected.  
This project integrates **Gyroscope sensors**, **ESP32 module**, **Raspberry Pi 4**, **USB camera**, and **Twilio Cloud API** for efficient real-time monitoring.

---

## 📸 System Workflow

![Workflow](Work%20Flow.jpg)

### 🔄 Working Principle
1. The **Gyroscope sensor** continuously monitors the orientation and acceleration of the subject.
2. The **ESP32** transmits sensor data wirelessly to the **Raspberry Pi 4**.
3. When a fall is detected, Raspberry Pi:
   - Triggers the **USB camera** to capture an image.
   - Runs a **machine learning model (Random Forest)** to verify the fall.
   - Sends an **SMS alert** through the **Twilio Cloud API** to the registered mobile number.

---

## ⚙️ Hardware Components
| Component | Description |
|------------|--------------|
| 🧭 **Gyroscope Sensor (MPU6050)** | Detects motion and orientation changes |
| 📡 **ESP32 Module** | Transfers data wirelessly to Raspberry Pi |
| 🍓 **Raspberry Pi 4** | Core processing unit and ML inference device |
| 📷 **USB Camera** | Captures images during fall incidents |
| ☁️ **Twilio Cloud API** | Sends SMS alerts to caregivers |

---

## 💻 Software & Libraries

| Tool / Library | Purpose |
|----------------|----------|
| **Python 3.x** | Main programming language |
| **OpenCV** | Image processing & camera control |
| **scikit-learn** | Random Forest model for fall detection |
| **Twilio API** | Sending SMS alerts |
| **Flask (optional)** | For creating monitoring dashboard |
| **ESP-IDF / Arduino IDE** | Programming ESP32 |
| **Serial / MQTT** | Communication protocol between ESP32 and Pi |

---

## 🚀 Setup & Installation

### 1️⃣ Clone the Repository
<details>
```bash 
git clone https://github.com/<your-username>/<your-repo-name>.git
cd <your-repo-name>
```
### 2️⃣ Create a Virtual Environment (Optional but Recommended)
```bash
python -m venv venv
source venv/bin/activate  # for Linux/Mac
venv\Scripts\activate     # for Windows
```
### 3️⃣ Install Required Libraries
```bash
   pip install -r requirements.txt
   ```
### 4️⃣ Add Your Twilio Credentials
Create a .env file in the project root directory:
TWILIO_ACCOUNT_SID=your_account_sid
TWILIO_AUTH_TOKEN=your_auth_token
TWILIO_PHONE_NUMBER=+1234567890
RECEIVER_PHONE_NUMBER=+919876543210
⚠️ Note: .env is added to .gitignore to protect sensitive credentials.

### 5️⃣ Run the Python Script
```bash
python fall_detection_code.py
```

---

### 🧠 Machine Learning Model

The Random Forest classifier is trained using gyroscope readings.
1. Predicts if the detected motion corresponds to a fall or normal movement.
2 .If fall probability > threshold → triggers camera + Twilio alert.
   
---

### 📲 Alert Example

When a fall is detected:
--Alert: Possible fall detected!
--Captured image sent to caretaker.
--Location: Living Room
--Timestamp: 2025-10-17 21:15

---

### 🧩 Project Architecture
Gyroscope → ESP32 → Raspberry Pi 4 → (Camera + ML Model + Twilio API)
                                       ↓
                                   Caretaker via SMS

---

### 🔒 Security
1. Sensitive credentials are stored in .env file.
2. .gitignore includes .env and dataset/image folders.
3. Network communication is encrypted via Wi-Fi (ESP32 to Raspberry Pi).

---

### 🧰 Future Enhancements
1. Integrate Firebase Cloud for data logging.
2. Add Real-Time Dashboard using Flask + WebSocket.
3. Use TensorFlow Lite for camera-based fall recognition.
4. Enable GPS integration for location tracking.

---

### 🧑‍💻 Author
Vasanth S S
B.E. Electronics and Communication Engineering
Chennai Institute of Technology
