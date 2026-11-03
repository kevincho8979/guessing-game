import random
from analyticskit import *


while True:
    secret_number = random.randint(1,10)
    guess = single_input('Guess a number between 1 and 10')

    try:
        if int(guess) == secret_number:
            show_message('Result', 'You win! You guessed the correct number.')
        else:
            show_message('Result', f'You lose. The correct number was {secret_number}')
    except:
        show_message('error', 'Please enter a vaild number')

    answer = single_input('Would you like to play again? Enter y/n')
    if answer != 'y':
        break

print('hello')
