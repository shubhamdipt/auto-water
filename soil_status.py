import RPi.GPIO as GPIO
import time
from email_alert import send_email
from tuya_smart_plug import TuyaSmartSwitch

GPIO.setmode(GPIO.BOARD) # Broadcom pin-numbering scheme
GPIO.setwarnings(True)

HIGH = GPIO.HIGH
LOW = GPIO.LOW

DELAY = 5

WATER_SENSOR_PIN = 3
#WET_STATUS = LOW


def get_status(pin):
    GPIO.setup(pin, GPIO.IN) 
    return GPIO.input(pin)


def set_status(pin, status):
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, status)


def save_soil_state(status):
    file_object = open("soil_state.txt", "w")
    file_object.write(status)
    file_object.close()


def change_in_state(status):
    file_object = open("soil_state.txt", "r")
    last_state = file_object.readline()
    file_object.close()
    return status != last_state


if __name__ == "__main__":
    try:
        switch = TuyaSmartSwitch()
        status = ""
        save_soil_state(status)
        while True:
            time.sleep(DELAY)
            wet_status = get_status(pin=WATER_SENSOR_PIN)
            if wet_status:
                status = "DRY"
            else:
                status = "WET"

            if status == "DRY":
                # Switches on the Tuya smart switch
                switch.turn_on()
            else:
                switch.turn_off()
            if change_in_state(status):
                send_email(status)
                save_soil_state(status)

    except KeyboardInterrupt: # If CTRL+C is pressed, exit cleanly:
        GPIO.cleanup() # cleanup all GPI

