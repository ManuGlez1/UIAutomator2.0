from Utils import Twilio_Utils
from uiautomator import Device
import time
import datetime
import pytz
import Utils.Serial_Utils as Serial


def run(test_case):
    serial = Serial.read_serial()
    print(test_case)

    try:
        d = Device(serial)
        # Script to leave a voice message
        call(d)

    except Exception as ex:
        print('Test Failed: ', ex)


def call(device):
    call_res = Twilio_Utils.call()
    print('Calling from ' + call_res.from_ + ' to ' + call_res.to)
    time.sleep(80)
    device.open.notification()
    time.sleep(.2)
    voice_mail_msg = device(text='New voicemail')
    if voice_mail_msg.exists:
        print('Test Passed: New voice mail successfully left')
    else:
        print('Test Failed: No voice mail left')


# ---------------------------------------------------------------------------


if __name__ == "__main__":
    run()
