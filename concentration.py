# concentration.py - The functions for a game of concentration.

# print the welcome screen and instructions
def intro():
    print('\nWelcome to Concentration!')
    print('\nThis is a memory game in which you guess two cards.')
    print('If the faces of the cards match, you win the pair')
    print('and they remain face up. Don\'t waste a turn!')
    input('\nEnter any number to CONTINUE: ')

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

# get a valid card guess from the user
def guess_card(show):
    guess = 0
    while True:
        # get a guess from the user
        guess = input('\nGuess a card: ')
        # validate guess
        # check: non-numeric
        if guess.isnumeric() == False:
            print('\nInvalid input. Please try again.')
            continue
        # convert string into an integer
        guess = int(guess)
        # check: out of bounds
        if guess < 1 or guess > 16:
            print('\nInvalid input. Please try again.')
            continue
        # decrement by 1 for zero-based indexing purposes
        guess -= 1
        # check: already chosen or matched, based on the 'show' list
        if show[guess]:
            print('\nInvalid input. Please try again.')
            continue
        # passed all checks, valid guess
        return guess

# pause before starting the next turn and allow the user to quit or continue playing
def pause():
    # get input from the user
    reply = input('\nEnter 0 to QUIT. Enter any other number to CONTINUE: ')
    # check if the user entered '0'
    if reply == '0':
        print('\nThanks for playing!\n')
        quit()
