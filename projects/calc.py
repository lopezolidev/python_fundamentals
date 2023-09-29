def add(a, b):
    ans = a + b
    print(a, " + ", b, " = ",ans)

def subs(a, b):
    ans = a - b
    print(a, " - ", b, " = ",ans)

def mult(a, b):
    ans = a * b
    print(a, " * ", b, " = ",ans)

def div(a, b):
    ans = a / b
    print(a, " / ", b, " = ",ans)


while True:
        
    print('Welcome to calculator')  

    a = float(input("Insert first number: "))

    print('a. +')
    print('b. -')
    print('c. *')
    print('d. /')    
    
    op = input('Choose operation: ')


    b = float(input("Insert second number: "))

    if op == 'a':
        add(a, b)
    elif op == 'b':
        subs(a, b)
    elif op == 'c':
        mult(a, b)
    elif op == 'd':
        div(a, b)
    else:
        print('Invalid operation')
        continue

    print("1. yes")
    print("2. no")
    selection = int(input("Would you like to make another operation?  "))


    if selection == 1:
        continue
    elif selection == 2:
        break
    else:
        print("Not a valid option")
        continue
