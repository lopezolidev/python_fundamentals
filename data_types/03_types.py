# string -> chain of characters
# written in ' ' or with " "

my_name = "Javier"
my_name = 'Sergio'
my_lastname = input("lastname: ")
print('my name =>', my_name, " and my last name, ", my_lastname)
print('data type for my_name: ', type(my_name))

'''
data type for my_name:  <class 'str'>
'''

# numbers -> integers or floats

my_age1 = 10
my_age2 = 10.5
my_future_age = input("your age in 10 years: ")
print('my age 1 =>', my_age1, " and in 10 years I'll be: ", my_future_age)
print('data type for my_age1: ', type(my_age1), " data type for my_future_age: ", type(my_future_age)) # function type() helps us know which is the data type of a variable

# NOTE: any time we input a number will be of data type STRING

'''
data type for my_age1:  <class 'int'>  data type for my_future_age:  <class 'str'>
'''

print('my age 2 =>', my_age2)
print('data type for my_age2: ', type(my_age2))

'''
data type for my_age2:  <class 'float'>
'''

# boolean -> True / False → must be in Capital the first letter of the word

is_single = True
is_python = False
print("is single?", is_single)
print("Data type of is_single:", type(is_single))

logged = input("are you logged? ")
print(type(logged)) # <class 'str'> ← also happens with boolean values


