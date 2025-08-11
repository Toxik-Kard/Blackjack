from random import choice

cards = [1,2,3,4,5,6,7,8,9,10,10,10,10,11]

def select_card():
    card_chosen = choice(cards)
    return card_chosen