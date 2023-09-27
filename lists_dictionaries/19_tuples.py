# Tuples are inmutable data structures, only for Reading its values

numbers = (2, 6, 9, 12, -5, -11)
print(numbers)      # (2, 6, 9, 12, -5, -11)
print("Type: ", type(numbers))      # Type:  <class 'tuple'>

names = ('jodie', 'male', 'george', 'kath', 'george')
print(names)        # ('jodie', 'male', 'george', 'kath')
print("Type of 'names': ", type(names))     # Type of 'names':  <class 'tuple'>

# CRUD
# numbers.append(3)       # AttributeError: 'tuple' object has no attribute 'append'   ← tuples are inmutable
print(numbers)

# numbers[1] = 'NaN'          # TypeError: 'tuple' object does not support item assignment ← tuples are inmutable

print(names)                    # ('jodie', 'male', 'george', 'kath', 'george')
print(names.index('male'))      # 1
print(names.count('george'))    # 2


# But we can turn the tuple into a list to become mutable 

my_list = list(names)
print(my_list)          # ['jodie', 'male', 'george', 'kath', 'george']
print(type(my_list))    # <class 'list'>

my_list.insert(1, 'lucy')
print(my_list)      # ['jodie', 'lucy', 'male', 'george', 'kath', 'george']

# Now we turn the list into a tuple back again...

my_tuple = tuple(my_list)
print(my_tuple)     # ('jodie', 'lucy', 'male', 'george', 'kath', 'george')
