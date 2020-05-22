from uiautomator import Device
from Utils import Calculator_Utils as Calculator
from Utils import Serial_Utils as Serial
import sys


def run():
    reload(sys)
    sys.setdefaultencoding('utf8')
    serial = Serial.read_serial()
    f = open("../Scripts/Operations.txt", "r")

    # Calculator Script
    d = Device(serial)
    Calculator.open_calc(d)
    for x in f:
        operation = x.split()[0]
        result = x.split()[1]
        test_case = x.split()[2]
        print(test_case)
        try:
            local_result = Calculator.make_operation(d, operation)
            if local_result == result:
                print("Test Passed:\n\tOperation: {0}\n\tExpected Result: {1}\n\tActual Result: {2}"
                      .format(operation, result, local_result))
            else:
                print("Test Failed: Wrong Result\n\tOperation: {0}\n\tExpected Result: {1}\n\tActual Result: {2}"
                      .format(operation, result, local_result))
        except Exception as ex:
            print('Test Failed ', ex)
        Calculator.wait(0.5)


# ---------------------------------------------------------------------------


if __name__ == "__main__":
    run()
