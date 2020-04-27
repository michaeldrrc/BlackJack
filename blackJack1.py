#-------------------------------------------------------------------------------
# Name:        BlackJack.py
# Purpose:
#
# Author:      Michael
#
# Created:
# Copyright:   (c) Michael 2015
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import random

class Player(object):
    people_under_21 = 0

    def __init__(self, name):
        self.name = name
        self.list_of_cards = []
        self.money = 100
        self.points = 0
        self.bet = 0

    def calculate_dealer_cards(self):
        if self.people_under_21 > 0:
            cardPoints = self.calculate_card_points()
            while cardPoints < 17:
                theDeck.deal_cards(1, dealer)
                cardPoints = self.calculate_card_points()

    def calculate_card_points(self):
        cardPoints = 0
        numberAces = 0
        for c in self.list_of_cards:
            cardPoints += c[1]
            if c[0] == 'A':
                numberAces += 1
        while cardPoints > 21 and numberAces > 0:
            cardPoints -= 10
            numberAces -= 1
        return cardPoints

    def play_round_of_cards(self):
        print self.name, "is now playing"
        nb = raw_input('Enter amount of bet: ')
        try:
            self.bet = int(nb)
        except ValueError:
            print("Invalid number, bet is now 10")
            self.bet = 10
        theDeck.deal_cards(2, self)
        self.print_cards()
        continue_string = raw_input('Enter Y or y if you want another card: ')
        while continue_string == 'y' or continue_string == 'Y':
            theDeck.deal_cards(1, self)
            self.print_cards()
            if self.calculate_card_points() > 21:
                print self.name, "went over 21"
                continue_string = 'n'
            else:
                continue_string = raw_input('Enter Y or y if you want another card: ')

    def print_cards(self):
        if len(self.list_of_cards) == 0:
            print self.name, "has no cards"
        else:
            print self.name, "has these cards:"
            for c in self.list_of_cards:
                print c[0], c[2]
            print "Points =", self.calculate_card_points()
            print "Bet =", self.bet
            print "Total money =", self.money

    def print_dealer_cards(self):
        if len(self.list_of_cards) == 0:
            print self.name, "has no cards"
        else:
            print self.name, "has these cards:"
            for c in self.list_of_cards:
                print c[0], c[2]

    def Initialize(self):
        self.list_of_cards = []
        self.points = 0
        self.bet = 0
        self.people_under_21 = 0


class Deck_of_cards(object):
    random_Deck = []
    Suits = ['spades', 'clubs', 'diamonds', 'hearts']
    Cards = ['A','K','Q','J','10','9','8','7','6','5','4','3','2']
    Card_values = [11,10,10,10,10,9,8,7,6,5,4,3,2]
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

    def take_next_card(self, myCard):
        self.list_of_cards.append(myCard)

    def deal_cards(self, number_of_cards, player):
        i = 0
        while i < number_of_cards:
            newCard = self.random_Deck[0]
            player.list_of_cards.append(newCard)
            del self.random_Deck[0]
            i += 1


def calculate_winnings(p1, D):
    if p1.calculate_card_points() > 21:
        p1.money -= p1.bet
        print p1.name, "lost", p1.bet, "dollars"
    else:
        if D.calculate_card_points() > 21:
            print "Dealer went over 21"
            p1.money += p1.bet
            print p1.name, "won", p1.bet, "dollars"
        elif p1.calculate_card_points() > D.calculate_card_points():
            p1.money += p1.bet
            print p1.name, "won", p1.bet, "dollars"
        elif p1.calculate_card_points() < D.calculate_card_points():
            p1.money -= p1.bet
            print p1.name, "lost", p1.bet, "dollars"
        else:
            print p1.name, "push bet with dealer"


player1 = Player("Michael")
player2 = Player("Christopher")
dealer = Player("Dealer")


dealer.people_under_21 = 0

theDeck = Deck_of_cards()
theDeck.construct_ordered_deck()
theDeck.construct_random_deck()

player1.Initialize()
player2.Initialize()
dealer.Initialize()
theDeck.construct_ordered_deck()
theDeck.construct_random_deck()

player1.play_round_of_cards()
if player1.calculate_card_points() < 22:
    dealer.people_under_21 += 1

player2.play_round_of_cards()
if player2.calculate_card_points() < 22:
    dealer.people_under_21 += 1

if dealer.people_under_21 > 0:
    dealer.calculate_dealer_cards()
    dealer.print_dealer_cards()
else:
    theDeck.deal_cards(2, dealer)
    dealer.print_dealer_cards()

calculate_winnings(player1, dealer)
calculate_winnings(player2, dealer)

continue_playing = raw_input('Enter Y or y if you want to continue playing: ')
while continue_playing == 'y' or continue_playing == 'Y':
    print "NEW GAME"
    player1.Initialize()
    player2.Initialize()
    dealer.Initialize()
    theDeck.construct_ordered_deck()
    theDeck.construct_random_deck()

    player1.play_round_of_cards()
    if player1.calculate_card_points() < 22:
        dealer.people_under_21 += 1

    player2.play_round_of_cards()
    if player2.calculate_card_points() < 22:
        dealer.people_under_21 += 1

    if dealer.people_under_21 > 0:
        dealer.calculate_dealer_cards()
        dealer.print_dealer_cards()
    else:
        theDeck.deal_cards(2, dealer)
        dealer.print_dealer_cards()

    calculate_winnings(player1, dealer)
    calculate_winnings(player2, dealer)
    continue_playing = raw_input('Enter Y or y if you want to continue playing: ')
