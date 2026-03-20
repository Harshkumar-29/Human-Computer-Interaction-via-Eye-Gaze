# Human-Computer-Interaction-via-Eye-Gaze
👁️ BlinkClick: Eye-Controlled Mouse using Computer Vision
📌 Overview

BlinkClick is a real-time eye-controlled mouse system that allows users to control the computer cursor using their eye movements and perform clicks using eye blinks. This project leverages Computer Vision and AI-based facial landmark detection to enable hands-free interaction with a computer.

It is especially useful for improving accessibility and creating futuristic human-computer interaction systems.

🚀 Features

🎯 Control mouse cursor using eye movement

👁️ Real-time face and eye tracking

👆 Blink to perform mouse click

⚡ Smooth and responsive cursor movement

🖥️ Works with any standard webcam

🛠️ Tech Stack

Python

OpenCV – for video processing

MediaPipe – for face mesh and eye landmark detection

PyAutoGUI – for controlling mouse actions

⚙️ How It Works

The webcam captures live video feed.

MediaPipe detects facial landmarks (especially eye regions).

Specific eye landmarks are tracked to determine gaze direction.

Cursor moves based on eye position on the screen.

A blink is detected when the distance between eyelid landmarks reduces → triggers a mouse click.

📂 Installation
pip install opencv-python mediapipe pyautogui
▶️ Usage
python main.py

Move your eyes to control the cursor

Blink to perform a click

📸 Demo

(Add screenshots or screen recording here)

💡 Applications

Assistive technology for physically disabled users

Hands-free computer control

Gaming and interactive systems

Research in Human-Computer Interaction (HCI)

🔮 Future Improvements

Add right-click and scroll functionality

Improve blink detection accuracy

Add calibration for better precision

Support multi-monitor setups

🤝 Contributing

Contributions are welcome! Feel free to fork this repo and submit a pull request.

📜 License

This project is open-source and available under the MIT License.

If you want, I can also:

make a cool GitHub banner

add badges (stars, forks, tech icons)

or convert this into a resume project description (ATS-friendly) 🚀

ake a cool GitHub banner
