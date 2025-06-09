# Auto Fisher for Minecraft
This Auto fisher is made for automatic fishing in minecraft.  
It scans the area around the crosshair.   

## Features  
- **Resolution Selection:**  
Supports 1920x1080 (Full HD), 2560x1440 (WQHD), and 3840x2160 (4k) to center the screen.

- **Automated casting and reeling:**  
Automatically casts the fishing line and reels it in when a fish is detected.

- **Color Detection:**  
Utilizes OpenCV to detect a specific red color within a defined area around the crosshair, indicating a fish bite.

- **Toggleable Operation:**  
Start and stop the bot with a hotkey (F8 by default)  


## How it works
1. **Selecting Resolution:**  
   Upon starting, it prompts the user to select their screen resolution to correctly calculate the screen center

2. **Casting the line:**  
   It performs a right-click to cast the fishing line.

3. **Monitoring:**  
   It continuously captures a small region around the screen's center for color detection.

4. **Detecting Red:**  
   It then checks for the bobber's red part within crosshair's region.

5. **Reeling in:**  
    If the red part is no longer detected, it assumes a fish has bitten and performs a right-click to reel in the line.

6. **Looping:**  
    The process repeats, allowing automated fishing until bot is stopped by the user.  


## Getting Started
### Prerequisites 
- Python 3.13  
- pyautogui  
- numpy  
- opencv-python  
- Pillow (for ImageGrab)  
- keyboard  
  
You can install these libraries using pip:  
`pip install pyautogui numpy opencv-python pillow keyboard`  

### Installation
1. Clone this repository or download the fisher.py and main.py files.  
    `git clone https://github.com/jojoanaa/AutoFish.git`  
   
3. Place both fisher.py and main.py in the same directory.

### Usage
1. **Run the main.py script in terminal:**  
    `python main.py`  

2. **Once the script is running, you will see a message in your console:**  
    > Bot ready. Press F8 to start/stop it.
    > Press ESC to exit the script.

3. **To start fishing:**  
    Press the F8 key. You will then be asked to select your screen resolution by pressing 1, 2, or 3.
    After selecting the resolution, the bot will begin fishing.

4. **To stop fishing:**  
    Press the F8 key again.

5. **To exit the script:**  
    Press the ESC key.

  
## Important Notes  
- This script is designed for **Minecraft 1.21.x** with **default resource pack**.  

- You'll need the **perfect angle to look at**: when casting the line, the **bobber and your crosshair must kiss**. Otherwise it won't work.  

- Your game must be in **bordered** full screen.  

- Please note that using this script **on public servers might result in a ban**. Make sure to read the server's rules first.  

- If there are problems with the fish bite detection, **try running this in F1 mode and/or set particles to "minimum".**  


