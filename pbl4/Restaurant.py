"""This module provides a restaurant object with a number of properties and methods"""

class Restaurant:
    """Object that stores properties and methods needed for a restaurant."""

    def __init__(self, restaurant_name, cuisine_type):
        """Stores the properties needed for the restaurant object."""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        """Prints the properties for the restaurant object."""
        print(self.restaurant_name)
        print(self.cuisine_type)

    def set_number_served(self, total):
        """Sets the number served outside of the constructor."""
        self.number_served = total

    def increment_number_served(self, served_today):
        """Increments the number_served property with the number served today."""
        self.number_served += served_today

    def display_number_served(self):
        """Displays the amount of customers served at the restaurant."""
        print("%s has served %s total customers." % (self.restaurant_name, self.number_served))

    def open_restaurant(self):
        """Prints a message indicating the restaurant is open."""
        print("%s is now open." % self.restaurant_name)
