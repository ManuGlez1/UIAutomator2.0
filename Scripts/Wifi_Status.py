#!/usr/bin/python

"""

"""
import time
from uiautomator import Device
import Utils.Serial_Utils as Serial


# ---------------------------------------------------------

def run(status, test_case):
    serial = Serial.read_serial()
    print(test_case)

    try:
        d = Device(serial)
        
        # Script to change the wif status
        wifi_status(d, status)

    except Exception as ex:
        print('Test Failed ', ex)


def wifi_status(device, status):
    device.wakeup()
    device.press.home()
    device.open.quick_settings()
    wait()
    device(resourceId='com.android.systemui:id/settings_button', className='android.widget.ImageButton').click()
    wait()
    device(text='Connections').click()
    wait()
    wifi_opt = device(resourceId='android:id/switch_widget', className='android.widget.Switch')
    if wifi_opt.__getattr__('text') == status:
        print('Test Passed: Wifi is already turned ' + status)
    else:
        wifi_opt.click()
        print('Test Passed: Wifi has been turned ' + status + ' successfully')
    device.press.home()
    return


def wait(sec=0.1):
    time.sleep(sec)


# ---------------------------------------------------------------------------


if __name__ == "__main__":
    run('On', 'testing')
