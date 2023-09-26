# not
print(not True)     # False
print(not False)    # True

# not AND
print('NOT AND')
print('not True and True →', not(True and True))     # False
print('not True and False →', not(True and False))     # True
print('not False and True →', not(False and True))     # True
print('not False and False →', not(False and False))     # True

# setting boundaries
stock = int(input('Insert stock => ')) # 70  # 800
 
print(not(stock >= 400 and stock <= 1500))  # True     # False

'''
Before:
 400 <= stock <= 1500   → True

After:
 stock <= 400 - 1500 <= stock  → True
'''