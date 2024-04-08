Welcome to rawMpuToAPI !

This program is sending raw MPU-6050 data to your API.

First, you need to connect your MPU-605O to your Pico W :

GND : GND
VCC : 3V3
SDA : GP0
SCL : GP1

Then upload the whole file to your Pico W.

You need to put the SSID and password of your WLAN in /lib/secrets.py.

You also need to change the url of your API in /main.py, line 15.

Once it's done, you can launch /main.py ! 

/!\ WARNING /!\  --------------------------------------

Sometimes, when you're the Pico W to your PC, you have the problem :

"Connection lost -- read failed: [Errno 6] Device not configured

Use Stop/Restart to reconnect.

Process ended with exit code 1."

Don't worry, you can erase flash memory of Pico W by putting "flash_nuke.uf2" in BOOTSEL mode. After that, reinstall MicroPython.

You will lose all your data in the device so don't forget to save your work !

/!\----------/!\ ----------------------------------------

Enjoy !
