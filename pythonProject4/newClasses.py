# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from itertools import islice
import sys, re
import os, shutil, string
import random

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

class Employee:
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

    def fullName(self):
        return '{} {}'.format(self.first, self.last)

class Card(object):
    def __init__(self, suit, val):
        self.suit = suit
        self.value = val

    def show(self):
        print("{} of {}".format(self.value, self.suit))

class Deck(object):
    def __init__(self):
        self.cards = []
        self.build() #build deck

    def build(self):
        #create 52 cards
        for s in ["Spades", "Clubs", "Diamonds", "Hearts"]:
            for v in range(1, 14):
                self.cards.append(Card(s,v))

    def show(self):
        for c in self.cards:
            c.show()

    def shuffle(self):
        for i in range(len(self.cards) - 1, 0, -1):
            r = random.randint(0, i)
            self.cards[i], self.cards[r] = self.cards[r], self.cards[i]

    def drawCard(self):
        return self.cards.pop()

class Player(object):
    def __init__(self, name):
        self.hand = []
        self.name = name

    def draw(self, deck):
        self.hand.append(deck.drawCard())
        return self

    def showHand(self):
        for c in self.hand:
            c.show()

    def discard(self):
        return self.hand.pop()



if __name__ == '__main__':
    print_hi('PyCharm')
    deck = Deck()
    deck.shuffle()

    bob = Player("Bob")
    bob.draw(deck).draw(deck)
    bob.showHand()
    bob.discard()

    #card = deck.drawCard()
    #card.show()
    #different instance of employers
    #emp1 = Employee('Esther', 'Vorkin', 50000)
    #emp2 = Employee('Stas', 'Chorny', 3000)

    #print(emp1.email)
    #print(emp2.first)
    #print(emp1.fullName())
    #print(Employee.fullName(emp2))


