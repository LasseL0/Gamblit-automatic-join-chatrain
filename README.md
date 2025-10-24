
# Rain Clicker Bot — Simple Image-Based Auto Clicker with Python

This project is a basic automation script that continuously searches for specific buttons on your screen (provided as images) and clicks them automatically. It’s designed for Windows and uses Python with the PyAutoGUI library.

WORKS ON GAMBLIT.NET AND GROWDICE.NET
if you wanna farm both site chatrains u have to use split screen (windows by side windows)

---

## Features

* Detects images (`join.png` and `join2.png`) on screen. (you can download images that are already tested or take your own SS and name it join, join2...)
* Clicks each button when found.
* Runs continuously in a loop until manually stopped.
* Adjustable detection confidence.
* Simple to set up and customize.

---

## Requirements

* Python 3.x installed ([python.org](https://www.python.org/))
* Python packages: `pyautogui`, `opencv-python`, `pillow`
* Windows OS (tested on Windows 10)
* Screen scaling set to 100% for best image recognition accuracy.

---

## Installation

1. **Install Python packages**

   Open Command Prompt and run:

   ```bash
   python -m pip install pyautogui opencv-python pillow
   ```

2. **Prepare your images**

   Place your `join.png` and `join2.png` screenshots in the same directory as the Python script. These images should be cropped exactly to the buttons you want to detect.

---

## Usage

1. Open Command Prompt.

2. Navigate to the folder containing the script and images:

   ```bash
   cd path\to\your\folder
   (example mine " cd C:\Users\lasse\Documents\botit "
   ```

3. Run the script:

   ```bash
   python rain_clicker.py
   ```

4. The bot will start searching for `join.png` and `join2.png """"` on your screen and click them when found.

5. To stop the bot, press `Ctrl + C` in the Command Prompt.

---


## Troubleshooting Tips

* **Image not found errors:**

  * Make sure images are exact screenshots of the buttons.
  * Set your Windows display scaling to 100%.
  * Adjust the `CONFIDENCE` value (try values between 0.5 and 0.8).
  * Ensure the buttons are visible on your screen.

* **Python or pip not recognized:**

  * Make sure Python is properly installed and added to your system PATH.
  * Use full path to Python if necessary, e.g., `C:\Users\YourName\AppData\Local\Programs\Python\Python39\python.exe -m pip install ...`

---
