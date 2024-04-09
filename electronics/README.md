# SE README
## Overview
This embedded system sends data in JSON format to the software application. The data is collected by a Raspberry Pi Pico W from two sensors: an MPU-6050 and a Drucksensor ZD10.

## Prerequisites
Before using the connected device you will need:
- A Raspberry Pi Pico W
- An MPU-6050
- A Drucksensor ZD10
- Thonny IDE installed

## Installation


1. Clone this repository to your local machine:

   ```bash
   git clone https://github.com/tristanqtn/RhythmicRanker
   ```

   ```bash
   cd RhythmicRanker
   ```

2. [Thonny IDE](https://thonny.org/)
3. Connect the Raspberry Pi Pico to your device following these steps:
    - Plug your Micro USB cable into the Raspberry and hold the BOOSTSEL button.
    - Then connect your Raspberry to your computer without releasing the BOOSTSEL button.
    - Once your Raspberry Pico has been detected, an explorer window should open. You don’t need to do anything.
    - Now, open Thonny IDE. At the bottom right of the window, you should see python3. Click there and select the option Configure Interpreter. It should open a new window.
    - In the Configure Interpreter window, you may click at the bottom right corner on the Install or Update MicroPython link. It will open a new window where you will need to select which version of MicroPython you want to install. Choose Raspberry Pi Pico W / Pico WH as the device and the latest version of MicroPython.
    - In case it didn’t appear yet, you may go to the View tab and activate the Files option.
    - Now you should see all the repositories from your computer and the Raspberry.
    - You now just need to find the repository "Rhythmic Ranker," go into the electronics, and rawMpuToAPI directories and upload all the .py files to the Raspberry. Right-click on the file name and select “Upload to/”.

## Configuration
To ensure that the device works correctly, make sure to connect your Raspberry to a 2.4GHz connection.

## Usage
In the Thonny IDE, you can now click on the Run button, and the script should run on its own. If you leave the files at the root of the Raspberry, you won’t have to upload the code from Thonny. If you unplug your Raspberry and reconnect it, the main.py should start automatically.

## Contributing
Feel free to contribute to this project by opening issues or pull requests. Any feedback or contributions are highly appreciated! This project is part of an open-innovation project.

## Author
Martial OWCZARUK : martial.owczaruk@edu.ece.fr
