# intro
print('''\nWelcome to Concentration!\n
This is a memory game in which you guess two cards.
If the faces of the cards match, you win the pair
and they remain face up. Don\'t waste a turn!\n''')

input('Press ENTER to continue: ')

# represents the face of each card
cards = ['1', '1', '2', '2', '3', '3', '4', '4', '5', '5', '6', '6', '7', '7', '8', '8']
# represents whether to display the face of the card
show = [True]*16
# represents the number of matches
matches = 0
# represents the number of turns
turns = 0

# print cards
print()
for index, card in enumerate(cards):
    if show[index] == False:
        print(' ■', end='')
    else:
        print(' ' + card, end='')
    
    if (index + 1) % 4 == 0:
        print()
    
print()
