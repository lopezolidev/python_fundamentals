# creating the iterable 
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# iterating over the list
iterable = iter(numbers)

# type of iterable:
print(type(iterable)) # <class 'list_iterator'>

# printing each element of the iterable

first = next(iterable)
print(first) # 1

second = next(iterable)
print(second) # 2

third = next(iterable)
print(third) # 3

# odd number iterator
odd_iter = iter(range(1, len(numbers)+1, 2))

for n in odd_iter:
    print(n)
'''
1
3
5
7
9
'''

# now using generators
def fibonacci(limits):
    a, b = 0, 1
    while a < limits:
        yield a
        a, b = b, a + b

print(list(fibonacci(10))) # [0, 1, 1, 2, 3, 5, 8]

for number in fibonacci(10):
    print(number)
'''
0
1
1
2
3
5
8
'''

def even_odd_generator(odd_or_even, limit):
    n = 0
    if odd_or_even:
        n = 1

    for i in iter(range(n, limit, 2)):
        yield i

for numb in even_odd_generator(False, 10):
    print(numb)
'''
Case for odd_or_even = True

1
3
5
7
9

Case for odd_or_even = False

0
2
4
6
8

'''

# try:
#     valor = int(input("Ingresa un número: "))
#     resultado = 10 / valor
#     print(f"El resultado es {resultado}")
# except ValueError:
#     print("Por favor, ingresa un número válido.")
# except ZeroDivisionError:
#     print("No se puede dividir por cero.")