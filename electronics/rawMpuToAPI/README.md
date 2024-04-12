# rawMpuToAPI

Welcome to rawMpuToAPI! This program sends raw MPU-6050 data to your API.

## Connection

First, you need to connect your MPU-6050 to your Pico W as follows:

- GND : GND
- VCC : 3V3
- SDA : GP0
- SCL : GP1

## Uploading the File

Upload the whole file to your Pico W.

## Configuration

1. **WLAN Credentials**: You need to put the SSID and password of your WLAN in `/lib/secrets.py`.

2. **API URL**: You also need to change the URL of your API in `/main.py`, line 15.

## Running the Program

Once everything is set up, you can run `/main.py`!

## Warning

Sometimes, when you connect the Pico W to your PC, you may encounter the following problem:

```
Connection lost -- read failed: [Errno 6] Device not configured
Use Stop/Restart to reconnect.
Process ended with exit code 1.
```

Don't worry! You can erase the flash memory of Pico W by putting `/Rhythmic-Ranker//electronics/flash_nuke.uf2` in your device in BOOTSEL mode. After that, reinstall MicroPython.

Please note that you will lose all your data in the device, so don't forget to save your work!

Enjoy!
