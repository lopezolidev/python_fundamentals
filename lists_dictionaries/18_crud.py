# CRUD → Create, Read, Update, Delete 

numbers = [2, 6, 9 , 7, 5]
print(numbers)      # [2, 6, 9, 7, 5]
print(numbers[1])   # 6
print(numbers[-1])  # 5

numbers.append(40)
print(numbers)      # [2, 6, 9, 7, 5, 40]

numbers.insert(0, 'WOW')
print(numbers)      # ['WOW', 2, 6, 9, 7, 5, 40]

numbers.insert(3, 'mod')
print(numbers)      # ['WOW', 2, 6, 'mod', 9, 7, 5, 40]

tasks = ['task_1', 'task_2', 'task_3']
new_list = numbers + tasks
new_list2 = tasks + numbers

print(new_list)     # ['WOW', 2, 6, 'mod', 9, 7, 5, 40, 'task_1', 'task_2', 'task_3']    ← the order copied is in which we sum
print(new_list2)    # ['task_1', 'task_2', 'task_3', 'WOW', 2, 6, 'mod', 9, 7, 5, 40]


index = new_list.index('task_2')    # obtaining where is 'task_2' 
new_list[index] = 'task_changed'    # setting in such place on the list a new element
print(new_list)         # ['WOW', 2, 6, 'mod', 9, 7, 5, 40, 'task_1', 'task_changed', 'task_3']

new_list.append('task_1')
print(new_list)         # ['WOW', 2, 6, 'mod', 9, 7, 5, 40, 'task_1', 'task_changed', 'task_3', 'task_1']
new_list.remove('task_1')       # ← eliminating the first element that fits such criteria
print(new_list)         # ['WOW', 2, 6, 'mod', 9, 7, 5, 40, 'task_changed', 'task_3', 'task_1']

new_list.pop()      # deleting last element of the list by default
print(new_list)     # ['WOW', 2, 6, 'mod', 9, 7, 5, 40, 'task_changed', 'task_3']

new_list.pop(0)     # deleting the element in position '0'
print(new_list)     # [2, 6, 'mod', 9, 7, 5, 40, 'task_changed', 'task_3']

new_list.reverse()  # reversing the order of elements in the list
print(new_list)     # ['task_3', 'task_changed', 40, 5, 7, 9, 'mod', 6, 2]

numbers_a = [1, 4, 6 , 3]
numbers_a.sort()    # ordering the elements in the list in ascending order by default
print(numbers_a)    # [1, 3, 4, 6]

strings = ['re', 'ab', 'ed']
strings.sort()      # ordering the elements in the list in alphabetical order
print(strings)      # ['ab', 'ed', 're']  

#new_list.sort() # TypeError: '<' not supported between instances of 'int' and 'str' ← we cannot sort numbers and strings in the same list

