# game.py - A game of concentration.

import concentration

# represents the face of each card
cards = ['☺', '♦', '♥', '☼', '☻', '♫', '☺', '♣', '♠', '☼', '♫', '♥', '♣', '♦', '☻', '♠']
# represents whether to show the face of each card
show = [False]*16
# represents the number of matches made
matches = 0
# represents the number of turns taken
turns = 0

# print the welcome screen and instructions
concentration.intro()

# the game loops until all the matches have been made
while matches != 8:
    # print the 'cards' list based on the 'show' list
    concentration.print_cards(cards, show)

    # get a valid card guess from the user
    guess1 = concentration.guess_card(show)
    # update the 'show' list to show the face of the card when printed
    show[guess1] = True

    concentration.print_cards(cards, show)

    guess2 = concentration.guess_card(show)
    show[guess2] = True

    concentration.print_cards(cards, show)

    # check if the guessed cards are a matching pair
    if cards[guess1] == cards[guess2]:
        print('\nMatch! :)')
        # increment the number of matches made
        matches += 1
    else:
        print('\nNo match. :(')
        # update the 'show' list to hide the face of the card when printed
        show[guess1] = False
        show[guess2] = False

    # increment the number of turns taken
    turns += 1

    # check if all the matches have been made
    # this is to avoid pausing after the game is won
    if matches != 8:
        # pause before starting the next turn and allow the user to quit or continue playing
        concentration.pause()

else: # all the matches have been made
    # print the win screen and the number of turns
    print('\nCongratulations! Well done!')
    print('\nNumber of turns:', turns, '\n')
