my_dict = {}
print(type(my_dict))    # <class 'dict'>

my_dict = {
    'engine': 'bla bla bla',
    'name': 'Xavier',
    'last_name': 'Lopez',
    'age': 99
}

print(my_dict)      # {'engine': 'bla bla bla', 'name': 'Xavier', 'last_name': 'Lopez', 'age': 99}
print(len(my_dict))     # 4 ← how many elements are in 'my_dict'

print(my_dict['age'])       # 99
#print(my_dict['something'])     # KeyError: 'something'   ← typing a non-existing key in the dictionary will throw an error

print(my_dict.get('something'))     # None  ← using '.get' function for dictionaries with a non-existing key will throw a handler that will take care of the event

print(my_dict['last_name'])     # Lopez

print('engine' in my_dict)      # True
print('non-existing' in my_dict)        # False