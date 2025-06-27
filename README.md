# ai_mouse

AI Virtual Mouse with Gesture Control
Control your computer's mouse using hand gestures through your webcam. This project leverages the power of computer vision to create a futuristic and touchless way to interact with your PC.
(Suggestion: You should create and add a GIF of your own project in action here!)

🌟 Key Features
Real-time Cursor Control: Smoothly move the mouse cursor by pointing your index finger.
Clicking Functionality: Perform a left-click by pinching your index and middle fingers together.
Scrolling Capability: Scroll up and down pages by making a "call me" gesture.
Visual Feedback: The application provides real-time visual cues, drawing landmarks on your hand and highlighting active fingers.
Actionable Area: A defined rectangle on the screen acts as the active zone for mouse control, preventing accidental movements.

🛠️ Technology Stack
This project is built with Python and relies on the following core libraries:
OpenCV: For capturing the video feed from the webcam and rendering the visual output.
MediaPipe: For its incredible high-fidelity hand and finger tracking capabilities, which form the backbone of the gesture recognition.
Autopy: For programmatically controlling the mouse (moving, clicking, and scrolling) at the operating system level.
NumPy: For handling the numerical calculations required to map hand coordinates to screen coordinates.

🤙 Gestures

The following hand gestures are used to control the mouse:
Action	Gesture	Visual Cue
Move Cursor	Raise only your index finger.	👆

Left Click	Raise your index and middle fingers and bring their tips together.	🤏

Scroll	Raise only your thumb and pinky finger ("Call me" sign). Move your hand up or down.	🤙


⚙️ Setup and Installation
To run this project on your local machine, follow these steps:
1. Prerequisites
Python 3.8 or higher
A webcam connected to your computer
2. Clone the Repository
Generated bash
AI Virtual Mouse with Gesture Control
Control your computer's mouse using hand gestures through your webcam. This project leverages the power of computer vision to create a futuristic and touchless way to interact with your PC.
(Suggestion: You should create and add a GIF of your own project in action here!)
🌟 Key Features
Real-time Cursor Control: Smoothly move the mouse cursor by pointing your index finger.
Clicking Functionality: Perform a left-click by pinching your index and middle fingers together.
Scrolling Capability: Scroll up and down pages by making a "call me" gesture.
Visual Feedback: The application provides real-time visual cues, drawing landmarks on your hand and highlighting active fingers.
Actionable Area: A defined rectangle on the screen acts as the active zone for mouse control, preventing accidental movements.
🛠️ Technology Stack
This project is built with Python and relies on the following core libraries:
OpenCV: For capturing the video feed from the webcam and rendering the visual output.
MediaPipe: For its incredible high-fidelity hand and finger tracking capabilities, which form the backbone of the gesture recognition.
Autopy: For programmatically controlling the mouse (moving, clicking, and scrolling) at the operating system level.
NumPy: For handling the numerical calculations required to map hand coordinates to screen coordinates.
🤙 Gestures
The following hand gestures are used to control the mouse:
Action	Gesture	Visual Cue
Move Cursor	Raise only your index finger.	👆
Left Click	Raise your index and middle fingers and bring their tips together.	🤏
Scroll	Raise only your thumb and pinky finger ("Call me" sign). Move your hand up or down.	🤙
⚙️ Setup and Installation
To run this project on your local machine, follow these steps:
1. Prerequisites
Python 3.8 or higher
A webcam connected to your computer
2. Clone the Repository
Generated bash
git clone https://github.com/your-username/your-repository-name.git
cd your-repository-name
Use code with caution.
Bash
3. Create a Virtual Environment (Recommended)
On Windows:
Generated bash
python -m venv venv
.\venv\Scripts\activate
Use code with caution.
Bash
On macOS/Linux:
Generated bash
python3 -m venv venv
source venv/bin/activate
Use code with caution.
Bash
4. Install Dependencies
Create a file named requirements.txt in the project directory and add the following lines to it:
Generated code
# requirements.txt
opencv-python
mediapipe
autopy
numpy
Use code with caution.
Now, install these libraries by running:
Generated bash
pip install -r requirements.txt
Use code with caution.
Bash
▶️ How to Run
With the setup complete, run the main script from your terminal:
Generated bash
python mouse.py
Use code with caution.
Bash
A window will open showing your webcam feed. Perform the gestures to control your mouse. Press the 'q' key on your keyboard while the webcam window is active to quit the application.
🚀 Future Improvements
This project is a great starting point. Here are some ideas for future development:
Implement Drag and Drop functionality.
Add a Right-Click gesture (e.g., pinching with the ring finger).
Add a Double-Click gesture.
Create a simple UI for adjusting settings like sensitivity and smoothening.

cd your-repository-name
Use code with caution.
Bash
3. Create a Virtual Environment (Recommended)
On Windows:
Generated bash
python -m venv venv
.\venv\Scripts\activate
Use code with caution.
Bash
On macOS/Linux:
Generated bash
python3 -m venv venv
source venv/bin/activate
Use code with caution.
Bash
4. Install Dependencies
Create a file named requirements.txt in the project directory and add the following lines to it:
Generated code


# requirements.txt
opencv-python
mediapipe
autopy
numpy
Use code with caution.

Now, install these libraries by running:
Generated bash
pip install -r requirements.txt
Use code with caution.
Bash

▶️ How to Run

With the setup complete, run the main script from your terminal:
Generated bash
python mouse.py
Use code with caution.
Bash
A window will open showing your webcam feed. Perform the gestures to control your mouse. Press the 'q' key on your keyboard while the webcam window is active to quit the application.

🚀 Future Improvements

This project is a great starting point. Here are some ideas for future development:
Implement Drag and Drop functionality.
Add a Right-Click gesture (e.g., pinching with the ring finger).
Add a Double-Click gesture.
Create a simple UI for adjusting settings like sensitivity and smoothening.
