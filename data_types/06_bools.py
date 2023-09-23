is_single = True
print(is_single) #True

is_single = False
print(is_single) #False

# ' not ' operator flips the value of the given variable
print(not True)
print(not False)

is_single = not is_single
print(is_single) #True

print(not(not(not is_single))) # False → True → False

