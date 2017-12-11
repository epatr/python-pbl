#------------------------------------------------------------------------------
# Program Name - P4_EricPatrick.py
# Written By - Eric Patrick
# Date - 12/05/2017
# This problem completes problem based learning assignment 4 by creating a class
# called Restaurant, calling its methods, and using inheritance to extend it.
#------------------------------------------------------------------------------

# Part 4
from Restaurant import Restaurant

# Part 1
restaurant = Restaurant('Hungry Howies', 'Spongey Pizza')
restaurant.describe_restaurant()
restaurant.open_restaurant()

# Part 2
restaurant.display_number_served()
restaurant.number_served = 4
restaurant.display_number_served()
restaurant.set_number_served(15)
restaurant.display_number_served()
restaurant.increment_number_served(10)
restaurant.display_number_served()

# Part 3
class IceCreamStand(Restaurant):
    """Adds the option to display ice cream flavors from the restaurant"""
    flavors = ['Vanilla', 'Chocolate', 'Birthday', 'Peanut Butter', 'Dairy-Free']

    def display_flavors(self):
        length = len(self.flavors)
        i = 0
        print("%s has %s flavors:" % (self.restaurant_name, length), end=' ')
        for flavor in self.flavors:
            print(flavor, end ='')
            i += 1
            if i < length:
                print(',', end=' ')

ice_cream_stand = IceCreamStand('Rodeo Whip', 'Delicious Ice Cream')
ice_cream_stand.display_flavors()
