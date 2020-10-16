import contextlib
import time

class Timer(object):
    def __init__(self, msg):
        self._msg = msg

    def __enter__(self):
        # time functions require Python >= 3.3
        self._start = time.monotonic()
        return time.perf_counter()
        #return time.clock_getres(time.CLOCK_MONOTONIC)

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type:
            print('Failed: {}: {}'.format(self._msg, exc_val))
            self.close()
        else:
            print("{}: {} s".format(self._msg, time.monotonic() - self._start))

#instead of a class:
@contextlib.contextmanager
def Timerr(msg):
    start = time.monotonic()
    try:
        yield time.perf_counter()
    except BaseException as e:
        print('Failed: {}: {}'.format(msg, e))
        raise
    else:
        print('{}: {} s'.format(msg, time.monotonic() - start))

if __name__ == '__main__':
    #with Timer("doing stuff"):
    #    for i in range(1000000):
    #        pass

    with Timer("doing stuff") as resolution:
        print('Resolution: {}'.format(resolution))
        for i in range(1000000):
            pass

    with Timerr("doing stuff") as resolution:
        print('Resolution: {}'.format(resolution))
        for i in range(1000000):
            pass

    #handle exceptions
    #with Timer("doing stuff"):
    #    raise ValueError('ack')