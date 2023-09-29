matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(matrix[0][2])         # ← matrix[row][column]
# 3

for row in matrix:
    print(row)
'''
[1, 2, 3]
[4, 5, 6]
[7, 8, 9]
'''


print(" ")

for row in matrix:
    print(row)
    for item in row:
        print(item)
'''
[1, 2, 3]
1
2
3
[4, 5, 6]
4
5
6
[7, 8, 9]
7
8
9
'''
print(" ")