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

def get_guess(show):
    guess = 0
    while guess == 0:
        guess = input('\nGuess a card: ')
        # numeric
        if guess.isnumeric() == False:
            print('\nInvalid input. Please try again.')
            guess = 0
            continue
        
        guess = int(guess)
        # out of bounds
        if guess < 1 or guess > 16:
            print('\nInvalid input. Please try again.')
            guess = 0
            continue
        
        # already matched/chosen
        if show[guess - 1]:
            print('\nInvalid input. Please try again.')
            guess = 0
            continue
    else:
        guess -= 1
        return guess

# intro
print('''\nWelcome to Concentration!\n
This is a memory game in which you guess two cards.
If the faces of the cards match, you win the pair
and they remain face up. Don\'t waste a turn!''')

input('\nEnter any number to CONTINUE: ')

# represents the face of each card
cards = ['1', '1', '2', '2', '3', '3', '4', '4', '5', '5', '6', '6', '7', '7', '8', '8']
# represents whether to display the face of the card
show = [False]*16
# represents the number of matches
matches = 0
# represents the number of turns
turns = 0

while matches != 8:
    # print cards
    print_cards(cards, show)

    # get guess
    guess1 = get_guess(show)
    show[guess1] = True

    # print cards
    print_cards(cards, show)

    # get another guess
    guess2 = get_guess(show)
    show[guess2] = True

    # print cards
    print_cards(cards, show)

    # check guesses
    card1 = cards[guess1]
    card2 = cards[guess2]

    if card1 == card2:
        print('\nMatch! :)')
        matches += 1
    else:
        print('\nNo match. :(')
        show[guess1] = False
        show[guess2] = False

    turns += 1

    reply = input('\nEnter 0 to QUIT. Enter any other number to CONTINUE: ')

    if reply.isnumeric():
        if int(reply) == 0:
            print('\nThanks for playing!\n')
            quit()
else:
    print('\nCongratulations! Well done!')
    print('\nNumber of turns:', turns, '\n')
