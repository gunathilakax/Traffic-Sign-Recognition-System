# 🚦 Traffic Sign Recognition System

## 📌 Introduction
The **Traffic Sign Recognition System** is an Arduino-powered solution that identifies road speed signs and dynamically adjusts vehicle speed accordingly. This innovative system enhances road safety by ensuring vehicles adhere to legal speed limits based on real-time sign detection.

## ✨ Features
- 🏎️ **Automatic Speed Control** – Adjusts vehicle speed dynamically.
- 📷 **Real-Time Sign Recognition** – Utilizes a camera to detect road signs.
- 🎯 **High Accuracy** – Machine learning-based detection algorithm.
- 🔗 **Arduino Integration** – Works seamlessly with microcontrollers.
- 📊 **Data Logging** – Stores and analyzes detected signs.

## 📁 Repository Structure
```
📦 Traffic-Sign-Recognition-System
├── 🚀 TrafficSignRecognition.ino  # Arduino code for sign recognition & speed control
├── 📷 TrafficSign_Detection.py    # Python script for webcam-based sign detection
├── 📜 README.md                   # Project documentation
└── 📂 Resources                    # Supporting files & datasets
```

## 🛠 Installation & Setup
1. **Clone the repository:**
   ```bash
   git clone https://github.com/gunathilakax/Traffic-Sign-Recognition-System.git
   cd Traffic-Sign-Recognition-System
   ```
2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
3. **Upload the Arduino code:**
   - Open `TrafficSignRecognition.ino` in the Arduino IDE.
   - Upload to the microcontroller.
4. **Run the recognition script:**
   ```bash
   python TrafficSign_Detection.py
   ```

## 🖥️ Usage
- Place the camera in a position where it can clearly see traffic signs.
- Start the Python script for real-time detection.
- The system will process the sign and adjust the vehicle’s speed accordingly.

## 🤝 Contributing
Contributions are welcome! Feel free to submit pull requests or open issues for discussions.

## 📢 Acknowledgments
💡 Inspired by advancements in **computer vision** and **autonomous vehicles**.

---
Made with ❤️ by **[@gunathilakax](https://github.com/gunathilakax)**

