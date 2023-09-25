from random import choice


#Input

rock = "Rock"
paper = "Paper"
scissors = "Scissors"
player_move = ''
computer_move = choice(['rock', 'paper', 'scissors'])

#logic
while player_move != ['rock', 'paper', 'scissors', 'exit']:
    player_move = input("Choose [r]ock, [p]aper , [s]cissors or [e] for exit: ")
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

print(f"Computer choses \"{computer_move}\"")

# Идеята ми е след правилен избор от player, кода да продължи с автоматичен избор на компютъра.
# След това да има сравнение на резултата и да се броят победи и загуби