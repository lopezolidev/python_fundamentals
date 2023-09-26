if True:
    print('Should execute')     # Should execute
if False:
    print("Shouldn't execute")

'''
vehicle = input('What is your favorite vehicle?')

if vehicle == 'car':
    print("You have good taste")
elif vehicle == 'bike':     # ← elif == else if
    print("That's cool!")
elif vehicle == 'boat':
    print("Nice choice")
else:
    print("You don't have vehicle taste")
'''


stock = int(input('Insert stock => '))

if (stock >= 400 and stock <= 1800) and (stock >= 1500 and stock <= 5000):      # overlapping two intervals
  print('correct stock')
else:
  print('incorrect stock')


# challenge, find out if a number is odd or even

num = int(input("Insert a number → "))

num = num % 2

if num == 0:
   print("Even number")
else:
   print("Odd number")