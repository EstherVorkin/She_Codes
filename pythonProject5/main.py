# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from functools import reduce
import pymongo
from pymongo import MongoClient

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

def f1(str):
    for c in str:
        if c != 'a' and c != 'A':
            return False
        return True

def f2(str):
    f = lambda str: not False in [char in 'Aa' for char in str]

def problem1():
    a = 10 + 10
    pb = lambda a: a+a
    return pb(1)

def f(x):
    return x*4

def readFiles(fname):
    for f in fname:
        for l in open(f):
            yield l
def grep(pattern, lines):
    return (l for l in lines if pattern in l)

def printLines(lines):
    for l in lines:
        print(l, end="")


#chain of decorators
def make_bold(f1):
    def inside():
        return "<b>" + f1() + "</b>"
    return inside

def make_italic(f2):
    def inside():
        return "<i>" + f2() + "</i>"
    return inside

def make_underline(f3):
    def inside():
        return "<u>" + f3() + "</u>"
    return inside

@make_bold
@make_italic
@make_underline
def hello():
    return "Ciao a tutti"


# Python program creating a
# context manager
class ContextManager():
    def __init__(self):
        print('init method called')

    def __enter__(self):
        print('enter method called')
        return self

    def __exit__(self, exc_type, exc_value, exc_traceback):
        print('exit method called')


# Python program showing
# file management using
# context manager

class FileManager():
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        self.file = None

    def __enter__(self):
        self.file = open(self.filename, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_value, exc_traceback):
        self.file.close()





class MongoDBConnectionManager():
    def __init__(self, hostname, port):
        self.hostname = hostname
        self.port = port
        self.connection = None

    def __enter__(self):
        self.connection = MongoClient(self.hostname, self.port)
        return self

    def __exit__(self, exc_type, exc_value, exc_traceback):
        self.connection.close()


    # Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

    # connecting with a localhost
    with MongoDBConnectionManager('localhost', '27017') as mongo:
        collection = mongo.connection.SampleDb.test
        data = collection.find({'_id': 1})
        print(data.get('name'))


    with ContextManager() as manager:
        print('with statement block')

    # loading a file
    with FileManager('test.txt', 'w') as f:
        f.write('Test')

    print(f.closed)

    #wrong way
        #with open("text.txt") as f:
        #    data = f.read()
        #file_desc = []
        #for x in range(1000000):
        #    file_desc.append(open('text.txt', 'w'))

    print(hello())

    res = [2**n for n in range(1,6)]
    print(res)

    squared = list(map(lambda x: x ** 2, [1,2,3,4]))
    print(squared)

    a = f1("asdffgh")
    b = "aaaA"
    mx = lambda x,y : x if x > y else y
    print(mx(8,5))

    n = [4, 3, 2, 1]
    print(list(map(lambda x: x**2, n)))
    print(list(filter(lambda x: x > 2, n)))
    print(reduce(lambda x,y: x*y, n))
    phrase = "absba"
    print(phrase.find(phrase[::-1]))

    #swap 2 var
    #a = 2
    #b = 1
    #a, b = b, a
    #print(a)
    #print(b)

    # Read File Python One-Liner
    #[line.strip() for line in open('abs.txt')]

    # Factorial Python One-Liner
    #n = 10
    #reduce(lambda x, y: x * y, range(1, n + 1))

    # Fibonacci Python One-Liner
    #lambda x: x if x <= 1 else fib(x - 1) + fib(x - 2)
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
