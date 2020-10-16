# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import random
import sys

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

def func1(x):
    for i in range(x):
        for j in range(i):
            print("* ", end = "")
        print('')

    for i in range(x,0,-1):
        for j in range(i):
            print('* ', end = "")
        print('')

def func2():
    word = input("Enter word:  ")
    for i in range(len(word) -1, -1, -1):
        print(word[i], end = "")
    print("\n")

def func3(m, n):
    new_mat = [[0 for col in range(n)] for row in range(m)]
    for i in range(m):
        for j in range(n):
            new_mat[i][j] = i*j

    print(new_mat)

def func4(number):
    print("{", end="")
    for i in range(number + 1):
        if i != 0:

            print(i,end = "")
            print(":", end = "")
            print(i**2, end = "")
            if i != number:
                print("  ,  ", end="")
    print("}")


def Guess_game():
    count = 0
    n = int(random.randint(1, 9))
    print("Rand number is: ")
    print(n)
    guess = input("Guess a number:  ")
    while(guess != "exit" and guess != n):
        guess = int(guess)
        count += 1
        if guess == n:
            print("Correct")
            break
        elif guess < n:
            print("too low")
        else:
            print("too high")
        guess = input("Guess a number:  ")
    print(count)

def hundred():
    name = input("Give me your name: ")
    age = input("Give me your age: ")
    this_year = input("What year it is now: ")
    one_hundred = int(this_year) - int(age) + 100

    print("Hi there " + name + "!\n")
    print("You will be a 100 year old in year " + str(one_hundred))

def game():
    user1 = input("What's your name?")
    user2 = input("And your name?")
    player1 = input("%s, do yo want to choose rock, paper or scissors?" % user1)
    player2 = input("%s, do you want to choose rock, paper or scissors?" % user2)

    while player1 != 'end game' or player2 != 'end game':
        if player1 == player2:
            print("It's a tie!")
            return
        elif player1 == 'rock':
            if player2 == 'paper':
                print(user2 + " wins!")
            else:
                print(user1 + " wins!")
        elif player1 == 'paper':
            if player2 == 'scissors':
                print(user2 + " wins!")
            else:
                print(user1 + " wins!")
        elif player1 == 'scissors':
            if player2 == 'rock':
                print(user2 + " wins!")
            else:
                print(user1 + " wins!")
        else:
            print('Bad choice')

        player1 = input("%s, do yo want to choose rock, paper or scissors?" % user1)
        player2 = input("%s, do you want to choose rock, paper or scissors?" % user2)




# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    func4(8)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/


