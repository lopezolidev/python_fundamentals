#  AND
print('AND')
print('True and True →', True and True)     # True
print('True and False →', True and False)     # False
print('False and True →', False and True)     # False
print('False and False →', False and False)     # False

print(990 > 5 and 5 < 90)   # True
print(10 > 99 and 50 > 10)  # False

stock = input('Insert stock => ') # 70  # 800
stock = int(stock) 
print(stock >= 400 and stock <= 1500)  # False     # True

# OR
print('OR')
print('True or True =>', True or True)
print('True or False =>', True or False)
print('False or True =>', False or True)
print('False or False =>', False or False)

role = input('Insert role => ')     # guest   -    admin   -   seller

print(role == 'admin' or role == 'guest')   # True   -   True   - False