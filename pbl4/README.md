# Project Based Learning 4: Classes "Restaurant"

# Basic Information

## PART I (worth 30 points)
 - Make a class called Restaurant. The `__init__()` method for Restaurant should store two attributes: a `restaurant_name` and a `cuisine_type`.
 - Make a method called `describe_restaurant()` that prints these two pieces of information, and a method called `open_restaurant()` that prints a message indicating that the restaurant is open.
 - Make an instance called restaurant from your class. Print the two attributes individually, and then call both methods.


## PART II: Number Served (worth 30 points)
 - Add an attribute called `number_served` with a default value of 0. Create an instance called restaurant from this class. Print the number of customers the restaurant has served, and then change this value and print it again.
 - Add a method called `set_number_served()` that lets you set the number of customers that have been served. Call this method with a new number and print the value again.
 - Add a method called `increment_number_served()` that lets you increment the number of customers who’ve been served. Call this method with any number you like that could represent how many customers were served in, say, a day of business.


## PART III: Ice Cream Stand (worth 30 points)
An ice cream stand is a specific kind of restaurant.

 - Write a class called IceCreamStand that inherits from the Restaurant class you wrote in Part II. Add an attribute called `flavors` that stores a list of ice cream flavors. Write a method that displays these flavors. Create an instance of IceCreamStand, and call this method.


## PART IV: Imported Restaurant (worth 10 points)
Using your latest Restaurant class, store it in a module. Make a separate file that imports Restaurant. Make a Restaurant instance, and call one of Restaurant’s methods to show that the import statement is working properly.

---

### Project Heading

Use the following as a header for all of your projects:
```
#------------------------------------------------------------------------------------------------------------------------
# Program name – filename.py
# Written by – your name
# Date – todays date
# Description of the program.
#--------------------------------------------------------------------------------------------------------------------------
```

### Style
Be sure you have header comments for each of your classes.


### Due Date
Week 15 - 16

### Turn In
1. Algorithm or flow chart
2. Program listing. Save file(s) as P4_YourName.py, include the imported module.