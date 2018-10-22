from tuyapy import TuyaApi
from utils import get_credentials


class TuyaSmartSwitch:

    def __init__(self):
        creds = get_credentials()
        tapi = TuyaApi()
        tapi.init(
            username=creds.get("TUYA_USERNAME"),
            password=creds.get("TUYA_PASSWORD"),
            countryCode=creds.get("TUYA_LOCATION")
        )
        self.device = tapi.get_device_by_id(creds.get("TUYA_DEVICE_ID"))

    def get_status(self):
        return self.device.state()

    def turn_on(self):
        self.device.turn_on()

    def turn_off(self):
        self.device.turn_off()
