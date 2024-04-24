import random

VALID_CHOICES = ['rock', 'paper', 'scissors']

def prompt(message):
    print(f'==> {message}')

def display_winner(player_choice, computer_choice):
    if ((player_choice == 'rock' and computer_choice == 'scissors') or
        (player_choice == 'paper' and computer_choice == 'rock') or
        (player_choice == 'scissors' and computer_choice == 'paper')):
        print("You win!")
    elif ((player_choice == 'rock' and computer_choice == 'paper') or
        (player_choice == 'paper' and computer_choice == 'scissors') or
        (player_choice == 'scissors' and computer_choice == 'rock')):
        print("Computer wins!")
    else:
        print("It's a tie!")

prompt("Welcome to RPS game!")

while True:
    prompt(f'Choose one: {", ".join(VALID_CHOICES)}')
    choice = input()

    while choice not in VALID_CHOICES:
        prompt('That is not a valid choice')
        choice = input()

    computer_choice = random.choice(VALID_CHOICES)

    prompt(f'You chose {choice}, computer chose {computer_choice}')

    display_winner(choice, computer_choice)

    prompt("Would you like to play again (y/n)?")
    answer = input().lower()

    while True:
        if answer.startswith('y') or answer.startswith('n'):
            break

        prompt("Invalid input. Try again.")
        answer = input().lower
    if answer[0] == 'n':
        break