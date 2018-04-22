import time
from selenium.common.exceptions import TimeoutException


def wait_until(predicate, timeout=10, period=0.25, *args, **kwargs):
    must_end = time.time() + timeout
    while time.time() < must_end:
        if predicate(*args, **kwargs):
            return True
        time.sleep(period)
    return False
