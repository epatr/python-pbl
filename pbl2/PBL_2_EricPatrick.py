#------------------------------------
# Filename: PBL_2_EricPatrick.py
# Written by Eric Patrick
# October 2017
# A solution for PBL 2
#------------------------------------

guests = []
food = []

choices = '''MAIN MENU
Choose a number from below:
1. Add a Guest
2. Remove a Guest
3. Print the Guest List'''

def playAgain():
    # Return True if they type yes to play again, otherwise False
    print('Return to main menu? (yes or no)')
    return input().lower().startswith('y')

gameIsDone = False

while True:
    print(choices)
    user_choice = int(input())

    if user_choice == 1:
        print('What is the name of the guest?')
        guest_name = input()
        print("What food does the guest want to bring?")
        food_choice = input()
        while (food_choice in food):
            print('Somebody is already bringing that, please choose something else')
            food_choice = input()
        else:
            guests.append(guest_name)
            food.append(food_choice)
            print('%s is bringing %s.' % (guest_name, food_choice))
            gameIsDone = True

    if user_choice == 2:
        print('What is the name of the guest?')
        guest_name = input()
        if (guest_name in guests):
            guest_location = guests.index(guest_name)
            del guests[guest_location]
            del food[guest_location]
            print('%s has been removed from the party.' % guest_name)
        else:
            print('%s was not found.' % guest_name)

    if user_choice == 3:
        guest_list = dict()
        for key,value in enumerate(guests):
            guest_list[value] = food[key]
            print('%s is bringing %s' % (guests[key], food[key]))

    else:
        print('Please choose a valid option.')

    gameIsDone = True
    if gameIsDone:
        if playAgain():
            gameisDone = False
        else: 
            break