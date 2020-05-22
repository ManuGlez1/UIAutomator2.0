import datetime

import pytz

from Scripts import Twilio_Call


def run_suite(print_time=True):
    if print_time:
        start_ts_pst = str(datetime.datetime.now(pytz.timezone('US/Pacific')).strftime('"%m-%d-%y %H:%M:%S.%f"'))

    Twilio_Call.run('TC27')

    if print_time:
        stop_ts_pst = str(datetime.datetime.now(pytz.timezone('US/Pacific')).strftime('"%m-%d-%y %H:%M:%S.%f"'))
        print("--------------- RESULTS ---------------")
        print('Test start: %s ' % start_ts_pst)
        print('Test end: %s' % stop_ts_pst)


# ---------------------------------------------------------------------------


if __name__ == "__main__":
    run_suite()
