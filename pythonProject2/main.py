# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import itertools
import random


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

def list1(_l):
    sum = 0
    for i in _l:
        sum += i
    return sum

def list2(_l):
    mul = 1
    for i in _l:
        mul *= i
    return mul

def list3(_l):
    max = 0
    for i in _l:
        if max < i:
            max = i
    return max

def list4(_l):
    min = 10000
    for i in _l:
        if min > i:
            min = i
    return min

def list5(_l):
    count = 0
    for i in _l:
        if len(i) >= 2:
            if i[0] == i[len(i)-1]:
                count += 1
    return count

def list6():
    new_list = list()
    for i in range(1,31):
        new_list.append(i**2)
    print(new_list[5:])

def list7():
    str1 = ['e', 's', 't', 'h', 'e', 'r']
    str2 = ''.join(str1)
    print(str2)

def list8():
    original_list = [[2, 4, 3], [1, 5, 6], [9], [7, 9, 0]]
    new_merged_list = list(itertools.chain(*original_list))
    print(new_merged_list)



bill_items = [
    ['Tom', 'Calamari', 6.00],
    ['Tom', 'American Hot', 11.50],
    ['Tom', 'Chocolate Fudge Cake', 4.45],
    ['Clare', 'Bruschetta Originale', 5.35],
    ['Clare', 'Fiorentina', 10.65],
    ['Clare', 'Tiramasu', 4.90],
    ['Rich', 'Bruschetta Originale', 5.35],
    ['Rich', 'La Reine', 10.65],
    ['Rich', 'Honeycomb Cream Slice', 4.90],
    ['Rosie', 'Garlic Bread', 4.35],
    ['Rosie', 'Veneziana', 9.40],
    ['Rosie', 'Tiramasu', 4.90],
]

def bill_splitting(name):
    sum = 0
    check_name = 0
    food_list = []
    for n in range(len(bill_items)):
        if name == bill_items[n][0]:
            sum += bill_items[n][2]
            check_name = 1
            food_list.append(bill_items[n][1])
    if check_name == 0:
        print(name + " didn't have dinner")
    else:
        print(name + ' should pay', sum, "." + name + " ate: ")
        for i in food_list:
            print(i)

def bill_splitting():
    name_list = []
    name_list.append((bill_items[0][0]))
    for n in range(len(bill_items)):
        if bill_items[n][0] not in name_list:
            name_list.append(bill_items[n][0])

    sum_list = []
    for i in name_list:
        sum = 0
        for n in range(len(bill_items)):
            if i == bill_items[n][0]:
                sum += bill_items[n][2]
        print(i + ' should pay', sum)

def random_list():
    rand_list = []
    for i in range(10):
        rand_list.append(random.randrange(1, 100, 1, int))
    print("\nRandomly-Generated List:\n" + str(rand_list))

    even_list = []
    even_list = [rand_list[x] for x in range(len(rand_list)) if rand_list[x]%2 == 0]
    return even_list

def tuple1():
    x = () #create empty tuple
    y = tuple() #create empty tuple
    z = ("tuple", True, 10, "Stas", 5.5) #create diff tuple data types
    print(z)
    w = 1,2,3,4,5
    print(w[0])
    print(w)
    ww = 10,
    print(ww)
    #unpacking a tuple
    a,b,c,d,e = w
    w = w + (9,)
    print(w)
    # adding items in a specific index
    w = w[:2] + (15, 20, 25) + w[3:]
    print(w)
    # converting the tuple to list
    listd = list(w)
    # use different ways to add items in list
    listd.append(30)
    w = tuple(listd)
    print(w)
    #tuple to string with join function
    tup = ('e', 'x', 'e', 'r', 'c', 'i', 's', 'e', 's')
    str = ''.join(tup)
    print(str)

    #count number of appearences in tuple
    tuplex = 2,3,4,4,4,4,5,5,5,5,5,1,2,1,9,0
    print(tuplex.count(5))

    #removing item from tuple
    tuplex = tuplex[:1] + tuplex[6:]
    print(tuplex)
    listx = list(tuplex)
    listx.remove(5)
    tuplex = tuple(listx)
    print(tuplex)
    print(tuplex.index(1,3))
    #convert tuple to dict
    tuplex = ((2, "w"), (3, "r"))
    print(dict((y, x) for x, y in tuplex))
    #print formatting
    t = (100, 200, 300)
    print('This is a tuple {0}'.format(t))

    #find the first tuple and exit
    num = [10, 20, 30, (10, 20), 40]
    ctr = 0
    for n in num:
        if isinstance(n, tuple):
            break
        ctr += 1
    print(ctr)

def set1():
    x = set()
    y = set([1,2,3,4,5]) #create set
    for i in y: #iterate over set
        print(i)
    x.add(100)
    print(x)
    x.update([200,6])
    print(x)
    y.pop()
    print(y)
    y.remove(3)
    print(y)

    setx = set(["green", "blue"])
    sety = set(["blue", "yellow"])
    setz = setx & sety #intersection
    setw = setx | sety #union
    setc = setx ^ sety #symetric diff
    print(setc)

    #frozen sets
    x = frozenset([1, 2, 3, 4, 5])
    y = frozenset([3, 4, 5, 6, 7])
    print(x.isdisjoint(y))# True: no elements in common with other.
    print(x.difference(y)) #return elements in x that are not in y
    print(x | y) #both x + y
    print(max(x))
    print(min(y))
    print(8 in x)
    print(3 in x)

    #superset
    nums = {10, 20, 30, 40, 50}
    print("Original set: ", nums)
    print("If nums is superset of itself?")
    print(nums.issuperset(nums)) #bigger and has the same elements

phonebook_dict = {
    'Alice': '703-493-1834',
    'Bob': '857-384-1234',
    'Elizabeth': '484-584-2923'
}

def exercise1():
    # Print Elizabeth's phone number.
    print(phonebook_dict['Elizabeth'])
    # Add an entry to the dictionary: Kareem's number is 938-489-1234.
    phonebook_dict['Kareem'] = '938-486-1234'
    # Delete Alice's phone entry.
    del phonebook_dict['Alice']
    # Change Bob's phone number to '968-345-2345'.
    phonebook_dict['Bob'] = '968-489-1234'
    # Print all the phone entries
    for n,p in phonebook_dict.items():
        print(n,p)

def letter_hist():
    # Write a letter_histogram program that asks the user for input,
    # and prints a dictionary containing the tally of how many times
    # each letter in the alphabet was used in the word.

    user_string = input("Please enter a word: ")

    char_dict = {}

    for char in user_string:
        char_dict[char] = 0

    for char in user_string:
        char_dict[char] += 1

    print(char_dict)

def word_histogram():
    # Write a word_histogram program that asks the user for a
    # sentence as its input, and prints a dictionary containing the
    # tally of how many times each word in the alphabet was used in
    # the text.

    user_string = input("Please enter a sentence: ")
    user_string = user_string + " "

    word_list = []
    temp_string = ""
    for char in user_string:
        if char == " ":
            word_list.append(temp_string)
            temp_string = ""
        else:
            temp_string = temp_string + char

    # create dictionary of words as keys and count as value
    # iterate over list of words, if word is not in dictionary
    # add word as key and give it count of 1. if word is in
    # dictionary, increment count

    word_dict = {}
    for word in word_list:
        if word.lower() not in word_dict:
            word_dict[word.lower()] = 1
        else:
            word_dict[word.lower()] += 1

    for word in word_dict:
        print("%s: %s" % (word, word_dict[word]))


if __name__ == '__main__':
    print_hi('PyCharm')
    word_histogram()


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
