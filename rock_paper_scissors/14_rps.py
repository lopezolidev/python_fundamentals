import random

options = ('rock', 'paper', 'scissors')

rounds = 0

computer_wins = 0
user_wins = 0
condition = True

while condition:

    print('*' * 30)
    print('ROUND ', rounds)
    print('computer ', computer_wins)
    print('user ', user_wins)
    print('*' * 30)

    user_option = input("rock, paper, scissors → ").lower()
    computer_option = random.choice(options)

    rounds += 1

    if not user_option in options:      # checking if the user took an invalid choice
        print("That's not a valid choice!")
        continue    # if we don't have a valid choice there's no need for the rest of the code to be executed

    print("User's option -> ", user_option)
    print("Computer's option -> ", computer_option)

    if user_option == computer_option:
        print("Draw!")
    elif user_option == 'rock':
        if computer_option == 'scissors':
            print('rock beats scissors')
            print('User wins!')
            user_wins += 1
        else:
            print('paper beats rock')
            print('Computer wins!')
            computer_wins += 1
    elif user_option == 'paper':
        if computer_option == 'rock':
            print('paper beats rock')
            print('User wins!')
            user_wins += 1
        else:
            print('scissors beats paper')
            print('Computer wins!')
            computer_wins += 1
    elif user_option == 'scissors':
        if computer_option == 'paper':
            print('scissors beats paper')
            print('User wins!')
            user_wins += 1
        else:
            print('rock beats scissors')
            print('Computer wins!')
            computer_wins += 1
    
    if computer_wins == 2:
        print('Final winner is computer!')
        condition = False
    if user_wins == 2:
        print('Final winner is the user!')
        condition = False   