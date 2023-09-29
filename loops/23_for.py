for element in range(20):       # for ... in is a for loop where the first field is the iterator and second the iterable
    print('element: ', element)

print(" ")
'''
element:  0 element:  1
element:  2 element:  3
element:  4 element:  5
element:  6 element:  7
element:  8 element:  9
element:  10    element:  11
element:  12    element:  13
element:  14    element:  15
element:  16    element:  17
element:  18    element:  19
'''

for e in range(1, 21):      # ← first number is where we start, last is where we finish
    print('e: ', e)

print(" ")
'''
e:  1   e:  2   e:  3
e:  4   e:  5   e:  6
e:  7   e:  8   e:  9
e:  10  e:  11  e:  12
e:  13  e:  14  e:  15
e:  16  e:  17  e:  18
e:  19  e:  20
'''

# iterating over a list

my_list = [3, 45, 13, 97, 65, 99]

for i in my_list:
    print('i: ', i)
print(" ")

'''
i:  3
i:  45
i:  13
i:  97
i:  65
i:  99
'''

my_tuple = ('jackie', 'kathy', 'jill', 'ashley')

for j in my_tuple:
    print('j: ', j)
print(" ")

'''
j:  jackie
j:  kathy
j:  jill
j:  ashley
'''

product = {
    'name': 'T-shirt',
    'price': 99.98,
    'stock': 4,
}

for value in product:
    print(value)
'''
name             
price
stock

    Only printed the keys
'''
print(" ")

for value in product:
    print(product[value])
'''
T-shirt
99.98
4  

    Now only prints the values of each key
'''
print(" ")

for value in product:
    print(value, ": ", product[value])
'''
name :  T-shirt
price :  99.98
stock :  4

    Now there're keys and values
'''
print(" ")


# there's a simpler way to do this...

for key, value in product.items():
    print(key, ": ", value)
'''
name :  T-shirt
price :  99.98
stock :  4

    product.items() → [('name', 'T-shirt'), ('price', 99.98), ('stock', 4)]  → iterating through... [(key, value), (key, value), (key, value)]  → [(iterable), (iterable), (iterable)]
'''

print(" ")

people = [
    {
        'name': 'John Doe',
        'age': 30
    },
    {
        'name': 'Luke Skywalker',
        'age': 24
    },
    {
        'name': 'Lara Croft',
        'age': 32
    }
]


for person in people:
    print(person)
'''
 
{'name': 'John Doe', 'age': 30}
{'name': 'Luke Skywalker', 'age': 24}
{'name': 'Lara Croft', 'age': 32}
 
'''
print(" ")

for person in people:
    print('name: ', person['name'])
'''
name:  John Doe
name:  Luke Skywalker
name:  Lara Croft
'''

