# print_cards.py - The function to print the cards.

# print the 'cards' list based on the 'show' list
def print_cards(cards, show):
    print()
    for index, card in enumerate(cards):
        # check whether to hide or show each card using the 'show' list
        if show[index] == False:
            print('■', end=' ') # hide
        else:
            print(card, end=' ') # show
        # print a new line every 4 cards
        if (index + 1) % 4 == 0:
            print() # new line
