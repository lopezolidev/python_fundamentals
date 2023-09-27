import random

options = ('rock', 'paper', 'scissors')

user_option = input("rock, paper, scissors → ").lower()
computer_option = random.choice(options)

if not user_option in options:      # checking if the user took an invalid choice
    print("That's not a valid choice!")

print("User's option -> ", user_option)
print("Computer's option -> ", computer_option)

if user_option == computer_option:
    print("Draw!")
elif user_option == 'rock':
    if computer_option == 'scissors':
        print('rock beats scissors')
        print('User wins!')
    else:
        print('paper beats rock')
        print('Computer wins!')
elif user_option == 'paper':
    if computer_option == 'rock':
        print('paper beats rock')
        print('User wins!')
    else:
        print('scissors beats paper')
        print('Computer wins!')
elif user_option == 'scissors':
    if computer_option == 'paper':
        print('scissors beats paper')
        print('User wins!')
    else:
        print('rock beats scissors')
        print('Computer wins!')