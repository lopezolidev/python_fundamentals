# lists have advantages over strings (character lists)
str = "Hello"
#str[0] = 'w'
#print(str)      # TypeError: 'str' object does not support item assignment

list = [2, 9 , 4, 17, -7]
print(list)      # [2, 9, 4, 17, -7]
print(type(list))   # <class 'list'>

list_2 = [True, 'apple', 49, 4.76]  # ← lists can store elements of different data type
print(list_2)       # [True, 'apple', 49, 4.76]

# we can also use the same methods for strings in lists

print(True in list_2)       # True
print(list[:4])     # [2, 9, 4, 17]
print(list[2:5])        # [4, 17, -7]
print(list[::2])        # [2, 4, -7]
print(48 in list_2)     # False


# we can alter the elements inside lists

list[2] = 'number'
print(list)     # [2, 9, 'number', 17, -7]