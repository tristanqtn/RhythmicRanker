import network
import socket
from secrets import secrets
from time import sleep
from picozero import pico_temp_sensor, pico_led
import machine
from imu import MPU6050
from machine import Pin, I2C
import urequests
import ujson

ssid = secrets['ssid']
password = secrets['pw']

url = "your-API-here" #change here with IP Address or URL of your API

ax = ay = az = gx = gy = gz = 0

data = {
    "sensor" : "mpu",
    "ax": ax,
    "ay": ay,
    "az": az,
    "gx": gx,
    "gy": gy,
    "gz": gz,
    }

json_data = None

def connect():
    #Connect to WLAN
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(ssid, password)
    while wlan.isconnected() == False:
        print('Waiting for connection...')
        sleep(1)
    print("connected")
    print(wlan.ifconfig())

try:
    connect()
    # Set up the I2C interface
    i2c = I2C(0, sda=Pin(0), scl=Pin(1), freq=400000)

    # Set up the MPU6050 class 
    imu = MPU6050(i2c)

    # continuously print the data
    while True:
        ax=round(imu.accel.x,2)
        ay=round(imu.accel.y,2)
        az=round(imu.accel.z,2)
        gx=round(imu.gyro.x)
        gy=round(imu.gyro.y)
        gz=round(imu.gyro.z)
        
        data["ax"] = ax
        data["ay"] = ay
        data["az"] = az
        data["gx"] = gx
        data["gy"] = gy
        data["gz"] = gz
        
        print(data)
        
        json_data = ujson.dumps(data)
        response = urequests.post(url, data=json_data, headers={'Content-Type': 'application/json'})
        
        if response.status_code == 200:
            print("Données envoyées avec succès!")
            response.close()
        else:
            print("Erreur lors de l'envoi des données: ", response.status_code)
            
        json_data = None
            
        sleep(2)

except KeyboardInterrupt:
    machine.reset()
    