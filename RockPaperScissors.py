import random

def play_game():
    user_choice = input("Enter your choice (rock, paper, or scissors): ")
    computer_choice = random.choice(['rock', 'paper', 'scissors'])
    
    print("You chose:", user_choice)
    print("Computer chose:", computer_choice)

    if user_choice == computer_choice:
        print('Its a tie!')
    elif (user_choice == 'rock' and computer_choice == 'scissors') or\
         (user_choice == 'paper' and computer_choice == 'rock') or\
         (user_choice == 'scissors' and computer_choice == 'paper'):
        print('You win, congratulations')
    else:
        print('Computer wins')
        
play_game()