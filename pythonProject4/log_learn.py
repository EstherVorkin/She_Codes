from itertools import islice
import sys, re
import os, shutil, string
import logging
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

formatter = logging.Formatter('%(levelname)s:%(name)s:%(message)s')

file_handler = logging.FileHandler('test.log')
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)

#logging.basicConfig(filename = 'test.log', level = logging.INFO,
                   # format = '%(levelname)s:%(name)s:%(message)s')


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    logger.info(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    #print_hi('PyCharm')
    print_hi('PyCharm234')
    spam = input("Insert spam value  ")
    #Write an assert statement that triggers an AssertionError if the variable spam is an integer less than 10.
    assert int(spam) >= 10, 'The spam variable is less than 10.'

    egg = input("Insert egg value  ")
    bacon = input("Insert bacon value  ")
    assert egg.lower() != bacon.lower(), "the same"

    #always false
    assert False
    #disable all logging msg
    logging.disable(logging.CRITICAL)
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
