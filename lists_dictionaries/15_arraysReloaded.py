text = "She knows how to program in Python"

print('JavaScript' in text)     # False
print('Python' in text)     # True

'''
if 'JS' in text:
  print('Good choice!!')    
else:
  print('You also choose well')     # You also choose well
'''
  
size = len(text)
print(size)     #34

print(len('computer'))       #  8

print(text)     # She knows how to program in Python
print(text.upper())     # SHE KNOWS HOW TO PROGRAM IN PYTHON
print(text.lower())     # she knows how to program in python
print(text.count('o'))      # 5

print(text.swapcase())      # sHE KNOWS HOW TO PROGRAM IN pYTHON
print(text.startswith('She'))       # True
print(text.endswith('Rust'))        # False
print(text.replace('Python', 'Go'))     # She knows how to program in Go

text_2 = 'this is a title'
print(text_2)       # this is a title
print(text_2.capitalize())      # This is a title
print(text_2.title())       # This Is A Title
print(text_2.isdigit())     #False
print("398".isdigit())      #True
