# guess_card.py - The function to guess a card.

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
