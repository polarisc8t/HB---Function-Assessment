# PART ONE

# 1. We have some code which is meant to calculate an item cost
#    by adding tax. Tax is normally 5% but it's higher in
#    California (7%).

#    Turn this into a function. Your function will pass in
#    the default tax amount (5%), a state abbreviation, and the
#    cost amount as parameters.

#    If the state is California, apply a 7% tax within the function.
#    Your function should return the total cost of the item,
#    including tax.

#    If the user does not provide a tax rate it should default to 5% 

CA_TAX = 0.07
OTHER_TAX = 0.05
item_cost = 0

state = str(raw_input("Please enter the state abbreviation from which you are paying taxes: "))
tax = raw_input("Please enter CA_TAX for California tax or OTHER_TAX for all other states: ")
item_cost = float(raw_input("Please enter the cost of your item: "))

def tax_calc(state, tax, item_cost):

	if state == 'ca' or 'CA':
		total_cost = (item_cost) + (0.07 * item_cost) 
		print "The total cost of the item in California is {}".format(total_cost)			    
		return total_cost
	else:
		total_cost = (item_cost) + (0.05 * item_cost)
		print "The total cost of the item in {} is {}".format(state, total_cost)				
		return total_cost
		
#####################################################################
# PART TWO

# 1. (a) Write a function, `is_berry()`, which takes a fruit name as a string
#        and returns a boolean if the fruit is a "strawberry", "cherry", or 
#        "blackberry".

def is_berry(fruit_name):
	if fruit_name == 'strawberry' or 'cherry' or 'blackberry':
		return True
	else:
		return False

#    (b) Write another function, shipping_cost(), which calculates shipping cost
#        by taking a fruit name as a string, calling the `is_berry()` function 
#        within the `shipping_cost()` function and returns `0` if ``is_berry()
#        == True``, and `5` if ``is_berry() == False``.

def shipping_cost(fruit_name):
	if is_berry() == True:
		return 0
	else: 
		return 5

# 2. (a) Write a function, `is_hometown()`, which takes a town name as a string
#        and evaluates to `True` if it is your hometown, and `False` otherwise.

HOME_TOWN = 'San Jose'
town_name = str(raw_input("Please state your town name: "))

def is_hometown(town_name):
	if town_name == HOME_TOWN:
		return True
	else:
		return False

#
#    (b) Write a function, `full_name()`, which takes a first and last name as
#        arguments as strings and returns the concatenation of the two names in
#        one string.

first_name = str(raw_input("What is your first name? "))
last_name  = str(raw_input("What is your last name? "))

def full_name(first_name, last_name):
	name = first_name+last_name
	return name

#
#    (c) Write a function, `hometown_greeting()`, which takes a home town, a
#        first name, and a last name as strings as arguments, calls both
#        `is_hometown()` and `full_name()` and prints "Hi, 'full name here',
#        we're from the same place!", or "Hi 'full name here', where are you 
#        from?" depending on what `is_hometown()` evaluates to.

# def hometown_greeting(town_name, first_name, last_name):

# 	if is_hometown(town_name) == True:
# 		print "Hi" full_name(first_name, last_name), "We're from the same place!"
# 	else: 
# 		print "Hi" full_name(first_name, last_name) "Where are you from?"

# 	return None

#####################################################################

# PART THREE

# 1. Write a function ``increment()`` with a nested inner function, ``add()`` 
#    inside of it. The outer function should take ``x``, an integer which
#    defaults to 1. The inner function should take ``y`` and add ``x`` and ``y`` together.

def increment(x):
    def add(y):
        return x + y
    return add

# 2. Call the function ``increment()`` with x = 5. Assign what is returned to a variable name, addfive. Call 
#    addfive with y = 5. Call again with y = 20.

addfive = increment(5)


# 3. Make a function that takes in a number and a list of numbers. It should append
#    the number to the list of numbers and return the list.

num = 0
num_list = []

def make_adder(num, num_list):
	myList = num_list.append(num)
	print myList
	return myList


#####################################################################
