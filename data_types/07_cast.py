name = 'Nick'
print(type(name)) #<class 'str'>

age = 14
print(type(age)) #<class 'int'>

is_elegible = False
print(type(is_elegible)) #<class 'bool'>

print('Nick' + ' Torres') #Nick Torres
print(10 + 30) #40
print('Nick' + str(10)) #Nick10 ← using str() casting
print('Nick' + '10') #Nick10 ← string inside ' '
print(f'Nick {10 + 30}') #Nick 40 ← casting the sum as a string

# testing with inputs

age = input("Insert age: ") 
print(type(age)) #<class 'str'>

age = int(age) #we can only input numerical values, for the transformation into an integer
print(type(age)) #<class 'int'>

print(f"Your age in 10 year will be {age + 10}") #now we can make operation with this data type, that already is an integer
