my_name = "Javier"
my_lastname = 'Lopez'
print(my_name)
print(my_lastname)

full_name = my_name + " " + my_lastname # concatenating 3 strings
print(full_name)

# alternating between simple and double quotation marks without altering python's interpretation of strings

quote = " That's a better solution "
quote2 = ' She said "Hello" '

print(quote)
print(quote2)

# 3 different forms to concatenate

my_age = input("age: ")

full_name = "My full name is " + my_name + " " + my_lastname + " and my age is " + my_age + " years"    # using '+' sign
print(full_name)

full_name = "My full name is {} {} and my age is {} years".format(my_name, my_lastname, my_age) 
# using {} to fill with the variables after ' .format ' function
# the order for setting the ' {} ' is the order in which we'll call the variables
print(full_name)

full_name = f"My full name is {my_name} {my_lastname} and my age is {my_age} years" 
# using ' f ' at the start with ' { variable } ' 
print(full_name) 