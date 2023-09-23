# number types
age = 25
budget = 300.25
separation = 0.000000000000000000000000000000000000003

print("type of 'age': ", type(age)) # type of 'age':  <class 'int'>
print("type of 'budget': ", type(budget)) # type of 'budget':  <class 'float'>
print("type of 'separation': ", type(separation)) # type of 'separation':  <class 'float'>

# Now operations 

lives = 3

lives = lives - 1  # redeclaring the variable with an operation
print(f"lives: {lives}") #lives: 2

lives -= 1      # arithmetic operation with the '=' after
print(f"lives: {lives}") #lives: 3

# scientific notation

print(f"value of 'separation': {separation}") #value of 'separation': 3e-39

distance = 8000000000000000000000000000000000000000.1 
distance2 = 9999999999999999999999999999999999999999999999
#scientific notation only works with floats, not with integers

print(f"quantic distance {distance} and {distance2}")

# challenge: make a quarter budget

january = float(input("first month budget: "))    # float
february = int(input("second month budget: "))      # int
march = int(input("third month budget: "))         # int

quarter = january + february + march
print(f"The quarter budget results in {quarter/3}")  # ← the final value is casted as a float