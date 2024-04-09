import network
import socket
from secrets import secrets
from time import sleep
from picozero import pico_temp_sensor, pico_led
import machine
from imu import MPU6050
from machine import Pin, I2C, ADC
import urequests
import ujson

ssid = secrets['ssid']
password = secrets['pw']

adc = ADC(Pin(28))

url = "API_ENDPOINT"  # change here with IP Address or URL of your API

ax = ay = az = gx = gy = gz = force_value = 0

data = {
    "ax": ax,
    "ay": ay,
    "az": az,
    "gx": gx,
    "gy": gy,
    "gz": gz,
    "force_value" : force_value
}

json_data = None

wlan = None

def read_force_sensor():
    # Read analog value from force sensor
    return adc.read_u16()
def connect():
    # Connect to WLAN
    global wlan
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(ssid, password)
    while wlan.status() == 1:
        print('Waiting for connection...' + str(wlan.status()))
        sleep(1)
    print("connected")
    print(wlan.ifconfig())

try:
    connect()
    # Set up the I2C interface
    i2c = I2C(0, sda=Pin(0), scl=Pin(1), freq=400000)

    # Set up the MPU6050 class
    imu = MPU6050(i2c)

    # Continuously print the data
    while True:
        ax = round(imu.accel.x, 2)
        ay = round(imu.accel.y, 2)
        az = round(imu.accel.z, 2)
        gx = round(imu.gyro.x)
        gy = round(imu.gyro.y)
        gz = round(imu.gyro.z)
        force_value = read_force_sensor()
        
        data["ax"] = ax
        data["ay"] = ay
        data["az"] = az
        data["gx"] = gx
        data["gy"] = gy
        data["gz"] = gz
        data["force_value"] = force_value
        # Remove the sensor key as it's not needed in the final format

        # Initialize an empty list to store the new data
        new_data = []

        # Iterate over the items in the data dictionary
        for key, value in data.items():
            # Create a new dictionary for each item and append it to the list
            new_data.append({
                "sensor": f"{key}",
                "measurement": value
            })

        # Print the new data
        print(new_data)

        for sample in new_data:
            json_data = ujson.dumps(sample)
            response = urequests.post(url, data=json_data, headers={'Content-Type': 'application/json'})
            #print(response)
            if response.status_code == 200:
                #print("Données envoyées avec succès!")
                response.close()
            else:
                print("Erreur lors de l'envoi des données: ", response.status_code)

except KeyboardInterrupt:
    wlan.disconnect()
    print('bye')