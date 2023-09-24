print(10 + 10) # 20

print(10 + 10.4) # 20.4 ← the floating number will cast the result into a float

print(40 - 18) # 22

print(12 - 27.74) # -15.739999999999998  ← same here

print(7 * 4) # 28  ← multiplication by 2 integers
print(7 * 0.2) # 1.4000000000000001  ← multiplication by a float

print(50 / 4) # 12.5

print(12 / 3) # 4.0 ← even though the numbers are integers the result is a float

print(type(12 / 3)) # <class 'float'>

print(14 // 7) # 2  ← integer division, doesn't take decimals into account

print(14 / 7) # 2.0  ← division with decimal appreciation

print(15 / 2.75) # 5.454545454545454

print(15 // 2.75) # 5.0   ← result is a float, but doesn't have any decimals in the result

print(4 ** 3) # 64  ← exponenciation
print(4 ** 0.3) # 1.515716566510398   ← third root of 4
print(4 ** -3) # 0.015625   ← negative exponent, it's 1 / 4³


print(6 % 4) # 2  ← module, takes the residue of the division by that number
print(6 % 3) # 0  ← as being an exact division the residue is 0

print(4**3 + 90 - 2 / 7 // 3) # 154.0 ← by the order of operations: 4**3 → -2 / 7 → (2/7) // 3 → + 90 - (2 / 7 // 3) 
