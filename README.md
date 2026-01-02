# 🎯 Face & Hand Detection with Finger Counting

![Python](https://img.shields.io/badge/Python-3.10-blue.svg)
![OpenCV](https://img.shields.io/badge/OpenCV-4.x-green.svg)
![MediaPipe](https://img.shields.io/badge/MediaPipe-0.9.1-orange.svg)

---

## 🚀 Overview

This project detects your **face** using **ML Kit FaceLandmarker** and detects **hands** with **MediaPipe Hands**.  
It counts the number of fingers raised (1-5) for each hand and displays the results **in real-time** using your webcam.

**Features:**

- 🟢 Face mesh + bounding box  
- 🟢 User info panel (Name, Gender, Age)  
- 🟢 Hands detected with landmarks  
- 🟢 Finger count per hand  
- 🟢 Real-time webcam display

---

## 🛠 Installation

### 1️⃣ Create Virtual Environment (Python 3.10 Recommended)
```
python -m venv venv310
.\venv310\Scripts\activate   # Windows
source venv310/bin/activate  # macOS/Linux
```
### 2️⃣ Install Dependencies
```
pip install mediapipe==0.9.1 opencv-python
```

### 3️⃣ Download ML Kit Face Landmark Model

Place face_landmarker.task in your project directory.

### 🎬 Usage
- Save your Python script as facedetection.py
- Make sure your webcam is connected

Run the script:
```
python facedetection.py
```
- The webcam will show in real-time:
- Face mesh + bounding box
- User info panel
- Hands detected
- Finger count per hand (e.g., Right Fingers: 3)
- Press q to exit the webcam feed.

### 🔍 How It Works
Face Detection

- Uses ML Kit Tasks API with face_landmarker.task

- Detects facial landmarks and draws mesh points

- Displays a panel with Name, Gender, and Age

- Hand Detection

- Uses MediaPipe Solutions API (mp.solutions.hands)

- Detects multiple hands

- Counts fingers based on landmark positions:

- Thumb: Horizontal position compared to adjacent joint based on hand label

- Other fingers: Vertical position of fingertip vs lower joint

### ⚠️ Notes

- Python 3.11+ is not compatible with mp.solutions.hands in MediaPipe 0.10+

- Use Python 3.10 + MediaPipe 0.9.1 for full functionality

- Hand detection accuracy depends on lighting and background conditions

### 🖼 Demo Screenshot
- [Webcam feed shows face mesh + hand landmarks + finger counts + info panel]

### 📄 License

- MIT License © 2026 Arron Kian Parejas

### 📬 Contact
📧 Email: parejasarronkian@gmail.com
💻 GitHub: darknecrocities