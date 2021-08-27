# pause.py - The function to pause the game.

# pause before starting the next turn and allow the user to quit or continue playing
def pause():
    # get input from the user
    reply = input('\nEnter 0 to QUIT. Enter any other number to CONTINUE: ')
    # check if the user entered '0'
    if reply == '0':
        print('\nThanks for playing!\n')
        quit()
