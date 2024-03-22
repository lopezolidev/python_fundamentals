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

if not (my_dict.get('something')):
    print(bool(my_dict.get('something')))   # False


numbers = [1, 4, 3, 2, 4, 3, 5, 1, 1, 1, 1, 6, 8, 4 ,5, 9, 4, 3, 3]
freq = {}

for i in range(0, len(numbers)):
    if numbers[i] in freq:
        freq[numbers[i]] = freq[numbers[i]] + 1 
    else:
        freq[numbers[i]] = 1
#finding the frequency of numbers in a list and turning them into a dictionary

print(freq)     # {1: 5, 4: 4, 3: 4, 2: 1, 5: 2, 6: 1, 8: 1, 9: 1}

# Creating a dictionary with nestes dictionaries and copying the second element of the dictionary

myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}

second_child = myfamily['child2'].copy()    # this method allows copying of object, making a literal copy and not a reference copy
print(second_child) # {'name': 'Tobias', 'year': 2007}

# now creating a new dictionary and inserting it in the original dictionary of childs
child4 = {
    "child4": {
        "name": "Neal",
        "year": 2008
    }
}

myfamily.update(child4)
print(myfamily)
'''
    {
        'child1': {
            'name': 'Emil', 
            'year': 2004
            }, 
        'child2': {
            'name': 'Tobias', 
            'year': 2007
            }, 
        'child3': {
            'name': 'Linus', 
            'year': 2011
            }, 
            'child4': {
                'name': 'Neal', 
                'year': 2008
            }
    }
'''

#printing the name of the first child and his year of birth

print(f'This childs name is {myfamily["child3"]["name"]} and he was born on {myfamily["child3"]["year"]}')  # This childs name is Linus and he was born on 2011

