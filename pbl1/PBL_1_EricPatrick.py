import random

key_press = 'y'

while (key_press == 'y'):
    roll1 = random.randint(1, 6)
    roll2 = random.randint(1, 6)
    print('Roll 1: %s' % roll1)
    print('Roll 2: %s' % roll2)

    if (roll1 + roll2 == 7) or (roll1 + roll2 == 11) or (roll1 == roll2):
        print('You win!')
    else:
        print('You lose :(')

    print('Press \'y\' to play again!')
    key_press = input()
