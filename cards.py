# Cards includes a list of 52 regular cards with no Jokers
import random

whole_deck = ['A of clubs', 'K of clubs', 'Q of clubs', 'J of clubs',
              '10 of clubs', '9 of clubs', '8 of clubs', '7 of clubs',
              '6 of clubs', '5 of clubs', '4 of clubs', '3 of clubs',
              '2 of clubs', 'A of hearts', 'K of hearts', 'Q of hearts',
              'J of hearts', '10 of hearts', '9 of hearts', '8 of hearts',
              '7 of hearts', '6 of hearts', '5 of hearts', '4 of hearts',
              '3 of hearts', '2 of hearts', 'A of diamonds', 'K of diamonds',
              'Q of diamonds', 'J of diamonds', '10 of diamonds',
              '9 of diamonds', '8 of diamonds', '7 of diamonds',
              '6 of diamonds', '5 of diamonds', '4 of diamonds',
              '3 of diamonds', '2 of diamonds', 'A of spades', 'K of spades',
              'Q of spades', 'J of spades', '10 of spades', '9 of spades',
              '8 of spades', '7 of spades', '6 of spades', '5 of spades',
              '4 of spades', '3 of spades', '2 of spades']

deck = whole_deck
random.shuffle(deck)

live_card = deck.pop()
print(live_card)
print("{} cards left in deck".format(len(deck)))
# random.shuffle(lst)

# random.shuffle(deck)
# print(deck)
# print(live_card)


live_card not in deck == True
