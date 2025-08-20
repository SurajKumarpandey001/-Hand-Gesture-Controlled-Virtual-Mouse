# 🖱️ Hand Gesture Controlled Virtual Mouse

This project allows you to control your computer's mouse using hand gestures detected via your webcam, using **MediaPipe** and **OpenCV**. When the index finger moves, the cursor moves accordingly. A mouse click is triggered when the thumb and index finger come close together.


## 🔧 Features

- Cursor movement controlled by your index finger
- Click simulation by pinching index and thumb fingers together
- Smooth cursor motion using exponential smoothing
- Real-time hand tracking using MediaPipe
- Works with any webcam

## 🛠️ Technologies Used

- Python 🐍
- OpenCV 🎥
- MediaPipe 🖐️
- PyAutoGUI 🖱️

## 📦 Installation

1. **Clone the repository**
   git clone https://github.com/SurajKumarpandey001/-Hand-Gesture-Controlled-Virtual-Mouse.git
   cd gesture-controlled-mouse


Install dependencies
pip install opencv-python mediapipe pyautogui


🚀 How to Run
python virtual_mouse.py

A window will open showing your webcam feed.
Move your index finger to control the mouse cursor.
Pinch your thumb and index finger to simulate a mouse click.
Press q to quit the application.

📝 Notes
Make sure your camera is connected and has a clear view of your hand.
You may need to adjust lighting for better hand detection.
This program disables PyAutoGUI's fail-safe feature, so be careful with full-screen apps.

📁 File Structure
.
├── virtual_mouse.py     # Main Python script
└── README.md            # Project documentation

🙌 Credits
MediaPipe by Google
PyAutoGUI
OpenCV

You can save this as `README.md` in the root directory of your project folder. If you want, I can also help you write the `LICENSE` file or add your name, GitHub profile, or YouTube demo link to the README!
