person = {
    'name': 'Peter',
    'last_name': 'Parker',
    'langs': ['pyton', 'R'],
    'age': 100
}

print(person)       # {'name': 'Peter', 'last_name': 'Parker', 'langs': ['pyton', 'R'], 'age': 100}

# altering values

person['name'] = 'John Jonah'
print(person)       # {'name': 'John Jonah', 'last_name': 'Parker', 'langs': ['pyton', 'R'], 'age': 100}

person['age'] -= 60
print(person)       # {'name': 'John Jonah', 'last_name': 'Parker', 'langs': ['pyton', 'R'], 'age': 40}

person['langs'].append('C++')   # inserting an element at the end of the array 'langs', which is an attribute of the dictionary 'person'
print(person)       # {'name': 'John Jonah', 'last_name': 'Parker', 'langs': ['pyton', 'R', 'C++'], 'age': 40}

del person['last_name']         # ← sentence 'del' means "delete" and its used to eliminate an item from the dictionary
print(person)       # {'name': 'John Jonah', 'langs': ['pyton', 'R', 'C++'], 'age': 40}

# person.pop()            # TypeError: pop expected at least 1 argument, got 0  ← in dictionaries, '.pop()' method requires at least 1 argument to delete from the structure

person.pop('age')
print(person)       # {'name': 'John Jonah', 'langs': ['pyton', 'R', 'C++']}

print('items')              # items
print(person.items())       # dict_items([('name', 'John Jonah'), ('langs', ['pyton', 'R', 'C++'])]) ← result in an array of tuples where we have [('key', 'value'), ('key 2', 'value 2')]

print('keys')       # keys
print(person.keys())        # dict_keys(['name', 'langs'])  ← only outputs the keys 

print('values')     # values
print(person.values())      # dict_values(['John Jonah', ['pyton', 'R', 'C++']]) ← only outputs the values

person['socials'] = 'twitter'
print(person)       # {'name': 'John Jonah', 'langs': ['pyton', 'R', 'C++'], 'socials': 'twitter'}