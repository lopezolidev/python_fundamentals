user_option = input("rock, paper, scissors → ").lower()

computer_option = 'scissors'

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