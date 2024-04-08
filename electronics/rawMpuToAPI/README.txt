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

Enjoy !