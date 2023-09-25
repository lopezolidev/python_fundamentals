x = 3.3
print(x)    # 3.3

y = 1.1 + 2.2
print(y)    # 3.3000000000000003

# x and y should be the same right?

print(x == y)   # False

# There're 2 ways to change this. 

# "string form"

y_str = format(y, ".2g")    # ← transforming 'y' into a string, and then manually eliminating those 0's until only 2 decimal points → "3.3"

print('str =>', y_str)  # str => 3.3
print(y_str == str(x))  # True   ← 'x' also turns into a string

print('-' * 10)     # ----------
print(x, y)     # 3.3 3.3000000000000003

# "math form"

tolerance = 0.00001
print(abs(x - y) < tolerance)   #True   → | 3.3 - 3.3000000000000003 | < 0.00001    →    (absolute value of a very small number) < 0.00001   → it's true. Both numbers are equal aside from the difference