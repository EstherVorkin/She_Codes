# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from itertools import islice
import sys, re
import os, shutil, string


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

def append_text(fname):
    with open(fname,"w") as f:
        f.write("Exercise python 4 \n")
        f.write("smth else \n")
        f.write("smth else2 \n")
        f.write("smth else3 \n")
        f.write("smth else4 \n")
        f.write("smth else5 \n")
    txt = open(fname)
    print(txt.read())

def file_read_from_tail(fname, lines):
    bufsize = 8192
    fsize = os.stat(fname).st_size
    iter = 0
    with open(fname) as f:
        if bufsize > fsize:
            bufsize = fsize - 1
            data = []
            while True:
                iter += 1
                f.seek(fsize - bufsize * iter)
                data.extend(f.readlines())
                if len(data) >= lines or f.tell() == 0:
                    print(''.join(data[-lines:]))
                    break

def longest_words(fname):
    with open(fname, 'r') as f:
        words = f.read().split() #making an arr of words
    max_len = len(max(words, key=len))

    return [word for word in words if len(word) == max_len]

def file_size(fname):
    import os
    statinfo = os.stat(fname)
    return statinfo.st_size

def combine_files(fname1, fname2):
    with open(fname1) as fh1, open(fname2) as fh2:
        for line1, line2 in zip(fh1, fh2):
            print(line1 + line2)

def generate26():
    if not os.path.exists("letters"):
        os.makedirs("letters")
    for l in string.ascii_uppercase:
        with open(l + ".txt","w") as f:
            f.writelines(l)
        newPth = shutil.move('%s.txt' % l, './letters/%s.txt' % l)

def change_date_format():
    datePattern = re.compile(r"""^(.*?)
           ((0|1)?\d)-                     # one or two digits for the month
           ((0|1|2|3)?\d)-                 # one or two digits for the day
           ((19|20)\d\d)                   # four digits for the year
           (.*?)$                          # all text after the date
          """, re.VERBOSE)
    for american in os.listdir('.'):
        month = datePattern.search(american)
        if month == None:
            continue

        befPart = month.group(1)
        moPart = month.group(2)
        dPart = month.group(4)
        yPart = month.group(6)
        aftPart = month.group(8)

    datePattern = re.compile(r"""^(1) # all text before the date
        (2 (3) )-                     # one or two digits for the month
        (4 (5) )-                     # one or two digits for the day
        (6 (7) )                      # four digits for the year
        (8)$                          # all text after the date
        """, re.VERBOSE)

    europian = befPart + dPart + '-' + moPart + '-' + yPart + aftPart
    absWorkingDir = os.path.abspath('.')
    americanname = os.path.join(absWorkingDir, american)
    europianname = os.path.join(absWorkingDir, europian)
    print('Renaming "%s" to "%s"...' % (americanname, europianname))
    # shutil.move(americanname, europianname)   # uncomment after testing



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    append_text('abc.txt')
    file_read_from_tail('abc.txt', 3)
    print(longest_words('abc.txt'))
    print(file_size('abc.txt'))
    combine_files('abc.txt', 'abc.txt')
    generate26()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
