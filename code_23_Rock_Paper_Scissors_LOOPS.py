import random
player_wins = 0
computer_wins = 0
winning_score = 3
while player_wins < winning_score and computer_wins < winning_score:
    print(f"Player Score: {player_wins} Computer Score: {computer_wins}")
    print("...rock...")
    print("...paper...")
    print("...scissors...")
    player = input("Player, make your move: ").lower()
    if player == "quit" or player == "q":
        break
    rand_num = random.randint(0,2)
    if rand_num == 0:
        computer = "rock"
    elif rand_num == 1:
        computer = "paper"
    else:
        computer = "scissors"
    print(f"Computer plays {computer}")

    if player == computer:
        print("Draw")
    elif player == "rock":
        if player == "paper":
            print("computer wins")
            computer_wins += 1
        else:
            print("player wins")
            player_wins += 1
    elif player == "paper":
        if computer == "rock":
            print("player wins")
            player_wins += 1
        else:
            print("computer wins")
            computer_wins += 1
    elif player == "scissors":
        if computer == "rock":
            print("computer wins")
            computer_wins += 1
        else:
            print("player wins")
            player_wins += 1
    else:
        print("Please enter a right move!")
if player_wins > computer_wins:
    print("Congrats, you won")
else:
    print("Ou, computer beat you xD")
print(f"Finall score..Player Score: {player_wins} Computer Score: {computer_wins}")


