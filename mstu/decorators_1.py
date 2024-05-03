import time
from functools import wraps


def time_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(round(end_time - start_time))
        return result

    return wrapper


@time_decorator
def sleep_1_sec():
    time.sleep(1)
    print("function")
    return 25


res = sleep_1_sec()

print(res)
