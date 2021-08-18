import memory

memory.intro()

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
    memory.print_cards(cards, show)

    # get guess
    guess1 = memory.guess_card(show)
    show[guess1] = True

    # print cards
    memory.print_cards(cards, show)

    # get another guess
    guess2 = memory.guess_card(show)
    show[guess2] = True

    # print cards
    memory.print_cards(cards, show)

    # check guesses
    if cards[guess1] == cards[guess2]:
        print('\nMatch! :)')
        matches += 1
    else:
        print('\nNo match. :(')
        show[guess1] = False
        show[guess2] = False

    turns += 1

    memory.pause()
else:
    print('\nCongratulations! Well done!')
    print('\nNumber of turns:', turns, '\n')
