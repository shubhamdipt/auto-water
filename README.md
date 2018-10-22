# auto-water
This repo contains scripts to first detect the moisture content in a soil and then send an alert or water the plant.

## Hardware requirements
1. RasberryPi
2. Humidity sensor
3. Tuya smart switch
4. Aquarium water pump
4. Plastic tubes

## Software requirements
1. Python3

### How to:
1. Put the moisture sensor in the soil.
2. Connect the humidity sensor to the Arduino board provided with the sensor.
3. Connect the Ground output of the Arduino board to pin 6 (ground) of GPIO of raspberrypi.
4. Connect the Power input (VCC) of the Arduino board to pin 2 (5V supply) of GPIO of raspberrypi.
5. Connect the digital signal output (DO) of the Arduino board to pin 3 of GPIO of raspberrypi.
6. Attach the tubes to the water pump and the other end of the tube to the plant soil.
7. Connect the power plug of the water pump to the Tuya smart switch.
8. Complete the config.json file with credentials (SMTP server, emails & Tuya account and device info).
9. Create local_config.json file. (for TUYA reference: https://docs.tuya.com/en/cloudapi/index.html)

```
{
  "SMTP_HOST": "",
  "SMTP_LOGIN": "",
  "SMTP_PASSWORD": "",
  "SENDER_EMAIL": "",
  "RECEIVERS_EMAILS": [],
  "TUYA_DEVICE_ID": "",
  "TUYA_USERNAME": "",
  "TUYA_PASSWORD": "",
  "TUYA_LOCATION": ""
}
```
10. Install the python libraries mentioned in requirements.txt file
11. Run soil_status.py as sudo.

```
nohup sh -c "sudo python3 soil_status.py" > /dev/null 2>&1 &
```
