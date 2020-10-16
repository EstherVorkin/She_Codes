# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import datetime
from itertools import islice
import sys, re, random
import os, shutil, string

try:
    import fox
except ImportError:
    print("This import does not exist")

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


class YourBaseError(Exception):
    pass

class YourPreciseError(YourBaseError):
    pass

class YourCustomValueError(ValueError, YourBaseError):
    pass

class ExceptionWithParamsError(YourBaseError):
    def __init__(self, msg):
        msg = "{}: {}".format(datetime.datetime.now(), msg)
        super().__init__(msg)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    try:
        1 / 0  # Operation that can fail
    except ZeroDivisionError:  # React specifically to this error
        print('Something failed')

    try:
        # This code can fail in many ways
        res = str(1 / random.choice([1, "1", 0]))
        print(float(random.choice([res, 'a'])))

    except ZeroDivisionError as e:  # You can capture the exception in a variable
        print('Something failed:', e)

    # You can use several "except" blocks
    except (TypeError, ValueError):  # You can capture several exceptions at once
        print('Something else failed')

    else:  # You can execute code if there is NO error
        print("It's all good")

    finally:  # This will be executed in all cases, error or not
        print("Good bye")

    raise ExceptionWithParamsError('Custom error !')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
