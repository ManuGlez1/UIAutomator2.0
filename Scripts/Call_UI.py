#!/usr/bin/python

"""
"""
import time
import datetime
import pytz
import re
import Utils.Serial_Utils as Serial
from uiautomator import Device


# ---------------------------------------------------------

def run(number, test_case):
    serial = Serial.read_serial()
    print(test_case)

    try:
        d = Device(serial)
        # Script calling number with adb and uiautomator
        call(d, number)

    except Exception as ex:
        print('Test Failed: ', ex)


def call(device, number):
    if not validate_number(number):
        print('Test Passed: Invalid Number')
    else:
        device.wakeup()
        device.press.home()
        wait()
        device(resourceId='com.sec.android.app.launcher:id/iconview_titleView'
               , className='android.widget.TextView'
               , text='Phone').click()
        wait()
        dial(device, number)
        device(resourceId='com.samsung.android.dialer:id/dialButton'
               , className='android.widget.FrameLayout').click()
        print("Test Passed: Calling " + number)
        wait(2)
        device(resourceId='com.samsung.android.incallui:id/disconnect_button'
               , className='android.widget.ImageButton').click()
        wait(1)


def dial(device, number):
    digits = device(resourceId='com.samsung.android.dialer:id/digits'
                    , className='android.widget.EditText')
    if digits.exists:
        digits.set_text("")
    for i in number:
        if i == '0':
            device(resourceId='com.samsung.android.dialer:id/zero'
                   , className='android.widget.RelativeLayout').click()
        elif i == '1':
            device(resourceId='com.samsung.android.dialer:id/one'
                   , className='android.widget.RelativeLayout').click()
        elif i == '2':
            device(resourceId='com.samsung.android.dialer:id/two'
                   , className='android.widget.RelativeLayout').click()
        elif i == '3':
            device(resourceId='com.samsung.android.dialer:id/three'
                   , className='android.widget.RelativeLayout').click()
        elif i == '4':
            device(resourceId='com.samsung.android.dialer:id/four'
                   , className='android.widget.RelativeLayout').click()
        elif i == '5':
            device(resourceId='com.samsung.android.dialer:id/five'
                   , className='android.widget.RelativeLayout').click()
        elif i == '6':
            device(resourceId='com.samsung.android.dialer:id/six'
                   , className='android.widget.RelativeLayout').click()
        elif i == '7':
            device(resourceId='com.samsung.android.dialer:id/seven'
                   , className='android.widget.RelativeLayout').click()
        elif i == '8':
            device(resourceId='com.samsung.android.dialer:id/eight'
                   , className='android.widget.RelativeLayout').click()
        elif i == '9':
            device(resourceId='com.samsung.android.dialer:id/nine'
                   , className='android.widget.RelativeLayout').click()
        elif i == '*':
            device(resourceId='com.samsung.android.dialer:id/star'
                   , className='android.widget.RelativeLayout').click()
        elif i == '#':
            device(resourceId='com.samsung.android.dialer:id/pound'
                   , className='android.widget.RelativeLayout').click()
        else:
            device(resourceId='com.samsung.android.dialer:id/zero'
                   , className='android.widget.RelativeLayout').long_click()
        wait(0.2)


def validate_number(number):
    return True if 15 > len(number) > 2 and re.match(r'^([\s\d\+\*\+\#]+)$', number) else False


def wait(sec=0.1):
    time.sleep(sec)


# ---------------------------------------------- -----------------------------


if __name__ == "__main__":
    run()
