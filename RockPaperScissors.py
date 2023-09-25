from random import choice

# Input

rock = "Rock"
paper = "Paper"
scissors = "Scissors"
player_move = ''
computer_move = ''
result = ''
computer_counter = 0
player_counter = 0


# logic


while computer_counter != 3 or player_counter != 3:
    if computer_counter == 3:
        print("Sorry! Computer won the game!")
        exit()
    elif player_counter == 3:
        print("Congratulations! You won the game!")
        exit()
    while player_move != ['rock', 'paper', 'scissors', 'exit']:
        player_move = input("Choose [r]ock, [p]aper , [s]cissors or [e] for exit: ")
        computer_move = choice(['rock', 'paper', 'scissors'])
        player_move_lower = player_move.lower()
        if player_move_lower in ["r", "p", "s", "e"]:
            if player_move_lower == "r":
                player_move = "rock"
            elif player_move_lower == "p":
                player_move = "paper"
            elif player_move_lower == "s":
                player_move = "scissors"
            elif player_move_lower == "e":
                print("Thanks for playing!")
                exit()

            print(f'You choose: "{player_move}"')
            break
        else:
            print("Invalid input. Try again...")

    print(f"Computer chooses \"{computer_move}\"")

    if player_move == computer_move:
        result = "draw"
        print("Draw! Try again!")
        continue
    elif player_move == 'rock' and computer_move == 'paper':
        print("Computer won!")
        computer_counter += 1
        continue
    elif player_move == 'rock' and computer_move == 'scissors':
        print("You won!")
        player_counter += 1
        continue
    elif player_move == 'scissors' and computer_move == 'paper':
        print("You won!")
        player_counter += 1
        continue
    elif player_move == 'scissors' and computer_move == 'rock':
        print("Computer won!")
        computer_counter += 1
        continue
    elif player_move == 'paper' and computer_move == 'rock':
        print("You won!")
        computer_counter += 1
        continue
    elif player_move == 'paper' and computer_move == 'scissors':
        print("Computer won!")
        player_counter += 1
