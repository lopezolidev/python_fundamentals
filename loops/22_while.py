'''
while True:
    print('executed')

    Example of an infinite loop
''' 

counter = 0

while counter < 10:
    print('counter: ', counter)
    counter += 1

# counter:  0
# counter:  1
# counter:  2
# counter:  3
# counter:  4
# counter:  5
# counter:  6
# counter:  7
# counter:  8
# counter:  9


i = 0

while i < 20:
    i += 1
    if i == 15:
        break   # we want to stop the execution of the loop when i == 15 
    print('i: ', i)
    
'''
i:  1
i:  2
i:  3
i:  4
i:  5
i:  6
i:  7
i:  8
i:  9
i:  10
i:  11
i:  12
i:  13
i:  14
'''

j = 0

while j < 20:
    j += 1
    if j < 15:
        continue        # ← 'continue' means going to the next iteration of the loop without executing the logic ahead if the condition is fulfilled, hence no number < 15 was printed due to the condition, then 'continue' is executed and the loop does a new iteration 
    print('j: ', j)

'''
j:  15
j:  16
j:  17
j:  18
j:  19
j:  20
'''