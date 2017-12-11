#-----------------------------------------------------------------------------
# Progran name - PBL_3_EricPatrick.py
# Written by Eric Patrick
# Date - November 2017
# A solution for PBL 3
#-----------------------------------------------------------------------------

import random

# Decides your prize/punishment by returning -1, 0, or 1
def randomBuff() :
    return random.randint(-1, 1)

# Returns the type of player stat that will be affected by the room
def chooseConsequence():
    choice = random.randint(0,2)
    options = ['lives', 'gold', 'inventory']
    return options[choice]

# Display the player status
def displayStatus():
    print('--------------------------------------------------------------------------------')
    print('You have %i lives, %i gold, and the following items:' % (lives, gold))
    for item in inventory:
        print(' - %s' % item)
    print('--------------------------------------------------------------------------------')

# Decide which random piece of gear to add to the inventory of the player
def randomGear():
    rand = random.randomint(0, 5)
    gear = ['Shield Upgrade', 'Sword Upgrade', 'Crossbow', 'Torch', 'Hatchet', 'Lockpick']
    return gear[rand]

# Define variables before the game begins
lives = 3
gold = 100
inventory = ['Basic Sword', 'Basic Shield']
playAgain = 'yes'
print('You have entered a hallway that is filled with rooms.n')

# Begin the game!
while playAgain == 'yes' or playAgain == 'y':
    
    displayStatus()

    print('You decide to enter a room.')
    buff = randomBuff()

    if buff == 1:
        consequence = chooseConsequence()
        if consequence == 'lives':
            print('You gain one life!')
            lives += 1
        elif consequence == 'gold':
            print('You gain 100 gold!')
            gold += 100
        elif consequence == 'inventory':
            gear = randomGear()
            inventory.append(gear)
            print('You gain a %s!' % gear)
    elif buff == 0:
        print('It\'s very dark. You hear something moving inside of it, but you find the door and escape unharmed!')
    elif buff == -1:
        print('There is a terrible sounding creature lunging towards you! During your escape, you lose something...')
        consequence = chooseConsequence()
        if consequence == 'lives':
            lives -= 1
            if lives == 0:
                print('Your last life! Game over.')
                playAgain = false
            else:
                print('A life! Now you only have %i left.' % lives)
        elif consequence == 'gold':
            gold -= 10
            if gold < 1:
                print('Every last piee of gold! You\'re now out of gold, which is wholly unimpressive.')
                gold = 0
            else: 
                print('10 gold! Now you only have %i' % gold)
        elif consequence == 'inventory':
            if len(inventory) == 0:
                print('Some dust, maybe an eyelash? Your inventory is already empty. You\'re doing really poorly.')
            else: 
                lostItem = inventory[-1]
                print('%s from your inventory!' % lostItem)
                del inventory[-1]

    displayStatus()
    print('You are back in the main hallway. You can either exit, or try your luck in another room.')
    print('Do you want to enter another room? (y or n)')
    playAgain = input()
