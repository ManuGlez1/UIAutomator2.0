#!/usr/bin/python

"""

"""
from subprocess import check_output
import time
import re
import Utils.Serial_Utils as Serial


# ---------------------------------------------------------

def run(number, test_case):
    serial = Serial.read_serial()
    print(test_case)

    try:
        # Script calling number with adb
        call_adb(serial, number)

    except Exception as ex:
        print('Test Failed: ', ex)


def call_adb(s, n):
    if not validate_number(n):
        print('Test Passed: Invalid number')
    else:
        check_output(['adb', '-s', s, 'shell', 'input keyevent', 'KEYCODE_WAKEUP'])
        check_output(['adb', '-s', s, 'shell', 'am', 'start', '-a', 'android.intent.action.CALL', '-d', 'tel:' + n])
        print("Test Passed: Calling " + n)
        time.sleep(2)
        check_output(['adb', 'shell', 'input keyevent', 'KEYCODE_ENDCALL'])
        time.sleep(1)


def validate_number(number):
    return True if 15 > len(number) > 2 and re.match(r'^([\s\d\+\*\+\#]+)$', number) else False


# ---------------------------------------------------------------------------

if __name__ == "__main__":
    run('4491234123', 'testing')
