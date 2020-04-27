#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:
#
# Created:     12-01-2015
# Copyright:   (c) Papa 2015
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import random

class Player(object):
    def __init__(self, name):
        self.name = name
        self.list_of_cards = []
        self.money = 0
        self.points = 0
        self.bet = 0
        self.take_hit = True
        self.continue_game = True

    def collect_cards(index, deck):
        deck.deal()

    def calculate_total_points(list_of_cards):
        l = len(list_of_cards)
        points = 0
        while i in list_of_cards:
            card_info = list_of_cards.index(i)
            card_value = card_info.index(i)
            points += card_value
        return points

    def take_card_hit():
        Cards.deal(1, list_of_cards)

    def print_cards(self):
        print self.name, "has these cards:"
        for c in self.list_of_cards:
            print c[0], c[2]

    def take_next_card(self, myCard):
        self.list_of_cards.append(myCard)

    def Initialize(self):
        self.list_of_cards = []
        self.points = 0
        self.bet = 0
        self.take_hit = True
        self.continue_game = True


class Deck_of_cards(object):
    random_Deck = []
    Suits = ['spades', 'clubs', 'diamonds', 'hearts']
    Cards = ['A','K','Q','J','10','9','8','7','6','5','4','3','2']
    Card_values = [1,10,10,10,10,9,8,7,6,5,4,3,2]
    ordered_deck = []

    def construct_ordered_deck(self):
        del self.ordered_deck[:]
        i1 = 0
        j1 = len(self.Cards)
        j2 = len(self.Suits)
        while i1 < j1:
            i2 = 0
            while i2 < j2:
                self.ordered_deck.append([self.Cards[i1], self.Card_values[i1], self.Suits[i2]])
                i2 += 1
            i1 += 1

    def construct_random_deck(self):
        del self.random_Deck[:]
        i = 0
        max = 52
        while i < max:
            j = random.randint(0, len(self.ordered_deck)-1)
            random_card = self.ordered_deck[j]
            self.random_Deck.append(random_card)
            del self.ordered_deck[j]
            i += 1

    def print_ordered_deck(self):
        print self.ordered_deck

    def print_random_deck(self):
        print self.random_Deck

    def deal_cards(self, number_of_cards, player):
        i = 0
        while i < number_of_cards:
            newCard = self.random_Deck[0]
            player.take_next_card(newCard)
            del self.random_Deck[0]
            i += 1


player1 = Player("Michael")
player2 = Player("Christopher")
player1.print_cards()
player2.print_cards()

theDeck = Deck_of_cards()
theDeck.construct_ordered_deck()
#theDeck.print_ordered_deck()
theDeck.construct_random_deck()
theDeck.print_random_deck()

theDeck.deal_cards(2, player1)
theDeck.deal_cards(2, player2)

player1.print_cards()
player2.print_cards()

player1.Initialize()
player2.Initialize()

player1.print_cards()
player2.print_cards()

print"redeal"

theDeck.construct_ordered_deck()
#theDeck.print_ordered_deck()
theDeck.construct_random_deck()
theDeck.print_random_deck()

theDeck.deal_cards(2, player1)
theDeck.deal_cards(2, player2)

player1.print_cards()
player2.print_cards()
