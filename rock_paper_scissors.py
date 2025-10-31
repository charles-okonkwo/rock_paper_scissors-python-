# Import command for the 'random' library
import random

# Function to display game instructions
def display_instructions():
    print('Welcome to Rock Paper Scissors.\n')
    print('The rules are simple:')
    print('1. Rock beats scissors')
    print('2. Scissors beat paper')
    print('3. Paper beats rock')

# Function to ask for the number of rounds
def get_rounds():
    rounds = input('\nHow many rounds would you like to play? \nRounds: ')
    rounds = int(rounds)
    return rounds

# Function to get the player's choice
def get_player_choice():
    player_choice = input('\nPlease enter rock, paper, or scissors. \nChoice: ')
    return player_choice

# Function to get the computer's choice
def get_computer_choice():
    options = ['rock', 'paper', 'scissors']
    computer_choice = random.choice(options)
    print('Computer chooses', computer_choice)
    return computer_choice

# Function to determine the winner of the round
def determine_round_winner(player_choice, computer_choice):
    if player_choice == computer_choice:
        print('Tie!')
    elif player_choice == 'rock' and computer_choice == 'scissors':
        print('You win!')
        return 'player'
    elif player_choice == 'rock' and computer_choice == 'paper':
        print('Computer wins!')
        return 'computer'
    elif player_choice == 'paper' and computer_choice == 'rock':
        print('You win!')
        return 'player'
    elif player_choice == 'paper' and computer_choice == 'scissors':
        print('Computer wins!')
        return 'computer'
    elif player_choice == 'scissors' and computer_choice == 'rock':
        print('Computer wins!')
        return 'computer'
    elif player_choice == 'scissors' and computer_choice == 'paper':
        print('You win!')
        return 'player'

# Function to determine the winner of the game and announce their name
def announce_game_winner(player_score, computer_score):
    # Write your code here.
    ...

# Function to contain the flow of the whole program
def main():
    computer_score = 0
    player_score = 0
    display_instructions()
    rounds = get_rounds()
    for i in range(rounds):
        print(f'\nRound {i+1}:')
        player_choice = get_player_choice()
        computer_choice = get_computer_choice()
        winner = determine_round_winner(player_choice, computer_choice)
        if winner == 'player':
            player_score += 1
        elif winner == 'computer':
            computer_score += 1
        else:
            pass
        print('Player score:', player_score, '| Computer score:', computer_score)
    # Function call to determine the winner of the game
    announce_game_winner(player_score, computer_score)
    print('\nFinal score: Player', player_score, '| Computer', computer_score)
    if player_score > computer_score:
        print('You won!')
    elif player_score < computer_score:
        print('Computer won!')
    else:
        print('This is a tie!')

main()