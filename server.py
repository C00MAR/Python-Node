import network 
import urequests
import utime
import ujson
import machine
from machine import Pin, I2C
from lcd_api import LcdApi
from pico_i2c_lcd import I2cLcd

wlan = network.WLAN(network.STA_IF)
wlan.active(True) 

ssid = 'iPhone J'
password = 'ZZZZZZZZ'
wlan.connect(ssid, password)
url = "http://172.20.10.2:3000/score"
print(wlan.isconnected())

I2C_ADDR = 0x27
I2C_NUM_ROWS = 2
I2C_NUM_COLS = 16

i2c = machine.I2C(0, sda=machine.Pin(0), scl=machine.Pin(1), freq=400000)
lcd = I2cLcd(i2c, I2C_ADDR, I2C_NUM_ROWS, I2C_NUM_COLS)

lcd.backlight_on()

devices = i2c.scan()


# ============ BOUTON =============

# droite = Pin(18, mode=Pin.IN, pull=Pin.PULL_UP)
# gauche = Pin(14, mode=Pin.IN, pull=Pin.PULL_UP)

# while True:
#     try:
#         if gauche.value() == 0:
#             print("gauche :"+str(gauche.value()))
#             data = { "text": "ArrowLeft" }
#             headers = { "Content-Type": "application/json" }
#             print(data)
#             print(headers)
#             r = urequests.post(url, json=data, headers=headers)
#             print(r.json())
#             r.close()
#         if droite.value() == 0:
#             print("droite :"+str(droite.value()))
#         utime.sleep(.1)
#     except Exception as e:
#         print(e)


# ============ TEST ECRAN =============

# while wlan.isconnected(): # or TRUE si pas de co
#     if len(devices) == 0:
#      print("No i2c device !")
#     else:
#      print('i2c devices found:',len(devices))
#     lcd.clear()
#     lcd.move_to(5,0)
#     lcd.putstr("Howdy")
#     utime.sleep(1)
#     lcd.clear()
#     lcd.move_to(2,1)
#     lcd.putstr("Tinkernerdz!")
#     utime.sleep(1)


while wlan.isconnected():
    try:
        r = urequests.get(url)
        json_response = r.json() # Décompressez la réponse en JSON
        tableau = json_response["score"]
        print(tableau)
        if r.status_code == 200:
            data = r.json()
            lcd.clear()
            lcd.move_to(2,0)
            lcd.putstr("== Pacman ==")
            lcd.move_to(3,1)
            lcd.putstr("Score : "+str(tableau))
        else:
            print("Request failed with status code {}".format(r.status_code))
        r.close()
        utime.sleep(.3)
    except Exception as e:
        print("Error: {}".format(e))
        lcd.clear()
        lcd.putstr("Error")
        # retry after a certain amount of time
        utime.sleep(5)