#Input

rock = "Rock"
paper = "Paper"
scissors = "Scissors"
player_move = ''

#logic
while player_move != ['rock', 'paper', 'scissors', 'exit']:
    player_move = input("Choose [r]ock, [p]aper , [s]cissors or [e] for exit: ")
    player_move_lower = player_move.lower()
    if player_move_lower != ["r", "p", "s"]:
        if player_move_lower == "r":
            player_move = "rock"
        elif player_move_lower == "p":
            player_move = "paper"
        elif player_move_lower == "s":
            player_move = "scissors"
        elif player_move_lower == "e":
            exit()
        if player_move_lower == 'r' or player_move_lower == 'p' or player_move_lower == 's' or player_move_lower == 'e':
         print(f'You choose: "{player_move}"')
         break
        else:
         print("Invalid input. Try again...")

# Идеята ми е след правилен избор от player, кода да продължи с автоматичен избор на компютъра.
# След това да има сравнение на резултата и да се броят победи и загуби