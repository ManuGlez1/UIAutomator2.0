import datetime
import pytz
import Calls_Suite
import Wifi_Suite
import Calculator_Suite
import Twilio_Suite


def run_suites():
    start_ts_pst = str(datetime.datetime.now(pytz.timezone('US/Pacific')).strftime('"%m-%d-%y %H:%M:%S.%f"'))

    Calls_Suite.run_suite(False)
    Wifi_Suite.run_suite(False)
    Calculator_Suite.run_suite(False)
    Twilio_Suite.run_suite(False)

    stop_ts_pst = str(datetime.datetime.now(pytz.timezone('US/Pacific')).strftime('"%m-%d-%y %H:%M:%S.%f"'))
    print("--------------- RESULTS ---------------")
    print('test start:  %s ' % start_ts_pst)
    print('test end  :  %s' % stop_ts_pst)


# ---------------------------------------------------------------------------


if __name__ == "__main__":
    run_suites()
