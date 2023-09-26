text = "She knows Python"

# Indexing

print(text[0])  # S
print(text[1])  # h

# print(text[999])        #IndexError: string index out of range

size = len(text)
print("size -> ", size)     # size ->  16
#print(text[size])       # IndexError: string index out of range
print(text[size - 1])       # n

print(text[-1])     # n

print(text[size - 1] == text[-1])   # True

# Slicing

print(text[0:5])        # She k   ← it's always one character behind
print(text[10:16])      # Python
print(text[:10])        # She knows
print(text[5:-1])       # nows Pytho
print(text[5:])         # nows Python
print(text[:])          # She knows Python
print(text[10:16:1])    # Python    ← jumping 1 character at the time from position 10 to 16 
print(text[10:16:2])    # Pto   ← jumping 2 character at the time from position 10 to 16
print(text[::2])        # SekosPto  ← jumping 2 characters from start to finish