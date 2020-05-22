import datetime
import pytz
from Scripts import Call_Adb
from Scripts import Call_UI


def run_suite(print_time=True):
    if print_time:
        start_ts_pst = str(datetime.datetime.now(pytz.timezone('US/Pacific')).strftime('"%m-%d-%y %H:%M:%S.%f"'))

    Call_Adb.run('1', 'TC01')
    Call_Adb.run('4491234312', 'TC02')
    Call_Adb.run('11111111111', 'TC03')
    Call_Adb.run('*666', 'TC04')
    Call_Adb.run('449testing', 'TC05')
    Call_UI.run('1', 'TC06')
    Call_UI.run('4491234312', 'TC07')
    Call_UI.run('11111111111', 'TC08')
    Call_UI.run('*666', 'TC09')
    Call_UI.run('449testing', 'TC10')

    if print_time:
        stop_ts_pst = str(datetime.datetime.now(pytz.timezone('US/Pacific')).strftime('"%m-%d-%y %H:%M:%S.%f"'))

        print("--------------- RESULTS ---------------")
        print('test start:  %s ' % start_ts_pst)
        print('test end  :  %s' % stop_ts_pst)


# ---------------------------------------------------------------------------


if __name__ == "__main__":
    run_suite()
