from contextlib import contextmanager
from datetime import datetime


@contextmanager
def managed_resource(*args, **kwargs):
    log = ''
    timestamp = datetime.now().timestamp()
    message = '{:<20}|{:^15}| open \n'.format(timestamp, args[0])
    log += message
    file_handler = open(*args, **kwargs)
    try:
        yield file_handler
    finally:
        timestamp_closed = datetime.now().timestamp()
        diff = timestamp_closed - timestamp
        message = '{:<20}|{:^15}| closed {:>15}s \n'.format(timestamp_closed, args[0], diff)
        log += message
        file_handler.close()
        print(log)

with managed_resource('test.txt', 'r') as f:
    print(f.read())