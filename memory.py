def print_cards(cards, show):
    print()

    for index, card in enumerate(cards):
        if show[index] == False:
            print(' ■', end='')
        else:
            print(' ' + card, end='')

        if (index + 1) % 4 == 0:
            print()

# intro
print('''\nWelcome to Concentration!\n
This is a memory game in which you guess two cards.
If the faces of the cards match, you win the pair
and they remain face up. Don\'t waste a turn!\n''')

input('Enter any number to CONTINUE: ')

# represents the face of each card
cards = ['1', '1', '2', '2', '3', '3', '4', '4', '5', '5', '6', '6', '7', '7', '8', '8']
# represents whether to display the face of the card
show = [False]*16
# represents the number of matches
matches = 0
# represents the number of turns
turns = 0

# print cards
print_cards(cards, show)
