import time

from .config import TIME_LOG_PATH

def timer(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        with TIME_LOG_PATH.open('a') as f:
            f.write(f'{func.__name__} took {end_time - start_time} seconds to execute\n')
        return result
    return wrapper
