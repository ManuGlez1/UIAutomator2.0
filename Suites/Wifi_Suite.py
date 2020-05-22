from Scripts import Wifi_Status
import datetime
import pytz


def run_suite(print_time=True):
    if print_time:
        start_ts_pst = str(datetime.datetime.now(pytz.timezone('US/Pacific')).strftime('"%m-%d-%y %H:%M:%S.%f"'))

    Wifi_Status.run('On', 'TC11')
    Wifi_Status.run('Off', 'TC12')
    Wifi_Status.run('Off', 'TC13')
    Wifi_Status.run('On', 'TC14')

    if print_time:
        stop_ts_pst = str(datetime.datetime.now(pytz.timezone('US/Pacific')).strftime('"%m-%d-%y %H:%M:%S.%f"'))
        print("--------------- RESULTS ---------------")
        print('Test start: %s ' % start_ts_pst)
        print('Test end: %s' % stop_ts_pst)


# ---------------------------------------------------------------------------


if __name__ == "__main__":
    run_suite()
