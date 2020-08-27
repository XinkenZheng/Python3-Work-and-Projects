#!/usr/bin/env python
# coding: utf-8

# In[286]:


import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 
            'Nine':9, 'Ten':10, 'Jack':10, 'Queen':10, 'King':10, 'Ace':11}


class Card:
    
    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
        self.values = values[rank]
        
    def __str__(self):
        return self.rank + " of " + self.suit
    


# In[287]:


class Deck:
    def __init__(self):
        
        self.all_cards= []
        
        for suit in suits:
            for rank in ranks:
                #create the card object
                created_card = Card(suit,rank)
                self.all_cards.append(created_card)
    
    def shuffle(self):
        random.shuffle(self.all_cards)
        
    def deal_one(self):
        return self.all_cards.pop()


# In[288]:


class Player:
    
    def __init__(self,name):
        self.name = name
        self.all_cards = []
        self.values = values
        
    def add_one(self, new_card):
            self.all_cards.append(new_card)
    
    def __str__(self):
        return f'Player {self.name} has {len(self.all_cards)} cards and a balance of {self.balance}'


# In[302]:


class Hand:
    def __init__(self):
        self.cards =[]
        self.value = 0
        self.aces = 0
        
    def add_card(self,card):
        self.cards.append(card)
        self.value = self.value + values[card.rank]
        if card.rank == 'Ace':
            self.aces += 1
    def adjust_ace(self):
        while self.value > 21 and self.aces:
            self.value -=10
            self.aces -=1
    
    def check_bust(self):
        if self.value <= 21:
            return False
        return True
            
    def my_hand(self):
        for c in self.cards:
            print(c)


# In[303]:


class Chips:
    def __init__(self,total = 100):
        self.total = total
        self.bet = 0
    
    def win_bet(self):
        self.bet +=self.bet
        
    def lose_bet(self):
        self.bet -= self.bet


# In[314]:


print("Welcome to Ken's Black Jack\n\n\n\n")

new_deck = Deck()
new_deck.shuffle()


myplayer = Player("ken")
mychips = Chips()


dealer = Player("Dealer")
dealer_chips = Chips()



playing = True
while playing:
    mycards = Hand()
    dealer_hand = Hand()
    
    
    mycards.add_card(new_deck.deal_one())
    mycards.add_card(new_deck.deal_one())
    print("\nYour Current Hand is:")
    mycards.my_hand()
    print('\n')

    choice = 'Y'
    while choice != 'N':
        choice = input("\nDo you want to hit? Type Y for yes and N for no ")
        if choice == 'Y':
            mycards.add_card(new_deck.deal_one())
            mycards.my_hand()
            if mycards.value > 21:
                mycards.adjust_ace()
                print("you have adjusted the value for Ace, your total new total is {} ".format(mycards.value))
            if mycards.check_bust():
                print("You have bust, Dealer wins.")
                print(f'Your total value is {mycards.value}')
                break

    print("Your total value is {}" .format(mycards.value))
    
    
    print("\n\nIt is dealer'turn now.")
       
    
    
    dealer_hand.add_card(new_deck.deal_one())
    print("one card is hidden")
    dealer_hand.add_card(new_deck.deal_one())
    print(dealer_hand.cards[1])
    while dealer_hand.value < mycards.value or not dealer_hand.check_bust():
        new_card = new_deck.deal_one()
        dealer_hand.add_card(new_card)
        print(new_card)
        
        if dealer_hand.value > mycards.value and not dealer_hand.check_bust():
            print("\nThe dealer has won, his total value is {}".format(dealer_hand.value))
            print(f'The hidden card is {dealer_hand.cards[0]}')
            break
        if dealer_hand.value > 21:
            dealer_hand.adjust_ace()
        if dealer_hand.check_bust():
            print(f'myPlayer has won the game, Dealer has bust with a value of {dealer_hand.value}')
            print(f'The hidden card is {dealer_hand.cards[0]}')
            break
                  
    
    newGame = input("Do you wish to play a new game? Type Y for yes, N for no .")
    if newGame == 'Y':
        playing = True
    else:
        playing = False
        

    
        
        
        
    
    
    



        
        
        








# In[ ]:





# In[ ]:




