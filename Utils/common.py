import datetime
import time
from functools import wraps


def run_time(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        func_start_time = time.time()
        # print(f'{func.__name__} start ...')
        ret = func(*args, **kwargs)
        # print(f'{func.__name__} end ...')
        print(f'Run Time Of Func -> {func.__name__} is : {format_runtime(time.time() - func_start_time)}')

        return ret

    return wrapper


def format_runtime(t) -> str:
    return f"{datetime.timedelta(seconds=t)}"
