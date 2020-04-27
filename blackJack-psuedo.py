#class BlackjackError(Exception):
	# Do nothing on BlackJack Error
    pass

# class Player(object):

    # Variable: number of players under 21 points - used for dealer card calculations
    number_of_players_under_21_points = 0

    #A function that initializes the class
    def __init__(self, name):
        self.name = name  # Variable: player's name as an argument
        self.list_of_cards = []  # Variable: player's list of cards
        self.money = 100  # Variable: player's money
        self.bet = 0   # Variable: player's current bet
        self.hasBlackJack = False # Variable: player has blackjack pair

    #A function that calculates dealer cards
    # def calculate_dealer_cards(self):
        if self.calculate_card_points() == 21:
           self.hasBlackJack = True # player has blackjack pair
           print self.name, "has BLACKJACK"
        # if some players are still in the game
        if self.number_of_players_under_21_points > 0:
            cardPoints = self.calculate_card_points()
             # keep collecting cards until 17 points is reached
            while cardPoints < 17:
                theDeck.deal_cards(1, dealer)
                cardPoints = self.calculate_card_points()

    #A function that calculate player card points
    # def calculate_card_points(self):
        cardPoints = 0
        numberAces = 0
		# go through all cards in list
        for c in self.list_of_cards:
            # add the value of cards from the card_value list
            cardPoints += c[1]
            # count the number of aces in the hand
            if c[0] == 'A':
                numberAces += 1
        # Aces are worth 11 point unless you went over 21
        # while cardPoints > 21 and numberAces > 0:
		# fix Ace value
            cardPoints -= 10
            numberAces -= 1
        return cardPoints


    #A function that prints card and info to screen
    # def print_cards(self):
        # print special line if player has no cards
        if len(self.list_of_cards) == 0:
            print self.name, "has no cards"

        # else print all cards, points, bet, and total money
            print self.name, "has these cards:"
            for c in self.list_of_cards:
                print c[0], c[2]
            print "Points =", self.calculate_card_points()
            print "Bet =", self.bet
            print "Total money =", self.money

    #A function that sets player's bet for the round
    # def do_betting(self):
        print self.name, "is now playing"
        print 'He has' ,self.money, 'dollars'
        bet_valid = False
        # repeat input until bet meets specifications
        while not bet_valid:
            try:
                input_bet = raw_input('Enter amount of bet: ')
                self.bet = int(input_bet)

                if self.bet > self.money or self.bet < 1:
                    raise BlackjackError

                bet_valid = True
            except ValueError:
                print 'please enter a valid integer as the bet'

            except BlackjackError:
                print 'please bet between 1 and your total money'

    #A function that deals and hits cards
    # def play_round_of_cards(self):
        #Deal for the start of the round.
        theDeck.deal_cards(2, self)

        #print cards and info to the screen
        self.print_cards()

		# Check if players cards are blackjack
        if self.calculate_card_points() == 21:
           self.hasBlackJack = True # player has blackjack pair
           print self.name, "has BLACKJACK"

        #start asking user for card hits
        continue_string = raw_input('Enter Y or y if you want another card: ').lower()

        while continue_string == 'y' or continue_string == 'Y':

            #Deal card to the player
            theDeck.deal_cards(1, self)
            self.print_cards()

			# if player went over 21
            if self.calculate_card_points() > 21:
                print self.name, "went over 21"

                #Exit the loop -- stop hitting
                continue_string = 'n'
            else:
                continue_string = raw_input('Enter Y or y if you want another card: ')

    #A function that prints the dealers cards
    # def print_dealer_cards(self):
	# print all cards that the dealer has
        if len(self.list_of_cards) == 0:
            print self.name, "has no cards"
        else:
            print self.name, "has these cards:"
            for c in self.list_of_cards:
                print c[0], c[2]

    #A function that reinitializes
    # def Initialize(self):
	# reset player's card list, bet, and BlackJack flag


# class Deck_of_cards(object):
    # constructors for the deck
    # Variable: random_Deck = []
	# Variable: Suits = ['spades', 'clubs', 'diamonds', 'hearts']
	# Variable: Cards = ['A','K','Q','J','10','9','8','7','6','5','4','3','2']
	# Variable: Card_values = [11,10,10,10,10,9,8,7,6,5,4,3,2]
	# Variable: ordered_deck = []

    #A function that does the initial construction of the deck
    # def construct_ordered_deck(self):
        del self.ordered_deck[:]
        i1 = 0
        j1 = len(self.Cards)
        j2 = len(self.Suits)
        while i1 < j1:
            i2 = 0
            while i2 < j2:
                # From the suit, value, and card lists, assemble are new card and appended to the ordered deck
                self.ordered_deck.append([self.Cards[i1], self.Card_values[i1], self.Suits[i2]])
                i2 += 1
            i1 += 1

    #A function that does the final construction of the deck
    # def construct_random_deck(self):
        del self.random_Deck[:]
        i = 0
        max = 52
        # randomly pick a card from the order deck and append to the random deck
        while i < max:
            # select a random card from the ordered deck
            j = random.randint(0, len(self.ordered_deck)-1)
            random_card = self.ordered_deck[j]
            self.random_Deck.append(random_card)
            # deleted card so that it does not get assigned more than once in random deck
            del self.ordered_deck[j]
            i += 1

    #A function that deals the specified number of cards to the player
    # def deal_cards(self, number_of_cards, player):
        i = 0
        while i < number_of_cards:
            # select the first cards on the deck
            newCard = self.random_Deck[0]
            # assign the cards to the player
            player.list_of_cards.append(newCard)
			# delete assigned cards from the random deck
            del self.random_Deck[0]

            i += 1


# this function calculates the winnings of a player and a dealer,
# and prints a statement about the player's current state.
# def calculate_winnings(p1, D):
    p1_card_points = p1.calculate_card_points()
    D_card_points = D.calculate_card_points()

    # If player has blackjack and dealer does not.  Player wins the round
    if p1.hasBlackJack == True and D.hasBlackJack == False:
        p1.money += int(p1.bet*1.5)
        print p1.name, "won 1.5 times the bet of", p1.bet, "dollars"

    # If player and dealer have blackjack.  Bet is pushed
    elif p1.hasBlackJack == True and D.hasBlackJack == False:
        print p1.name, "push bet with dealer"

    # Player loses the round if the value of its cards are over 21
    elif p1_card_points > 21:
        p1.money -= p1.bet
        print p1.name, "lost", p1.bet, "dollars"

    #Player wins the round if the value of the dealer's cards is over 21
    elif D_card_points > 21:
        print "Dealer went over 21"
        p1.money += p1.bet
        print p1.name, "won", p1.bet, "dollars"

    #Player wins the round if the value of its cards is greater than the dealers
    elif p1_card_points > D_card_points:
        p1.money += p1.bet
        print p1.name, "won", p1.bet, "dollars"

    #Player loses the round if the value of its cards is lower than the dealers
    elif p1_card_points < D_card_points:
        p1.money -= p1.bet
        print p1.name, "lost", p1.bet, "dollars"
    else:
        print p1.name, "push bet with dealer"

    # If player money is 0, add 25 dollars
    if p1.money < 1:
        p1.money = 25
        print str(p1.name)+ "'s mother sends 25 dollar to continue playing"

# Main code
#Create players.
player1 = Player("Michael")
player2 = Player("Christopher")
dealer = Player("Dealer")

#create the deck of cards and shuffle
theDeck = Deck_of_cards()
theDeck.construct_ordered_deck()
theDeck.construct_random_deck()

#Initialize players variables for the round
continue_playing = 'y'
while continue_playing == 'y' or continue_playing == 'Y':
    print ""
    player1.Initialize()
    player2.Initialize()
    dealer.Initialize()
    theDeck.construct_ordered_deck()
    theDeck.construct_random_deck()

    # start the betting round
    player1.do_betting()
    player2.do_betting()
    theDeck.deal_cards(2, dealer)
    print "Dealer's face-up card is", dealer.list_of_cards[0][0], dealer.list_of_cards[0][2]

    # play the card rounds
    player1.play_round_of_cards()
    if player1.calculate_card_points() < 22:
        dealer.number_of_players_under_21_points += 1

    player2.play_round_of_cards()
    if player2.calculate_card_points() < 22:
        dealer.number_of_players_under_21_points += 1

    if dealer.number_of_players_under_21_points > 0:
        dealer.calculate_dealer_cards()
        dealer.print_dealer_cards()
    else:
        dealer.print_dealer_cards()

    # see who won
    calculate_winnings(player1, dealer)
    calculate_winnings(player2, dealer)
	# check if player wants to play another round
    continue_playing = raw_input('Enter Y or y if you want to play another round: ')
