from random import uniform

elements = ["rock", "paper", "scissors"]

print("1) Rock")
print("2) Paper")
print("3) Scissors")
print()

player_choice = int(input("Your choice: "))
computer_choice = int(uniform(1, 3))

print("Player's choice: ", end="")
print(elements[player_choice - 1])
print()

print("Computer's choice: ", end="")
print(elements[computer_choice - 1])
print()

if (player_choice == computer_choice):
    print("This game is draw.")
elif (player_choice == 1):
    if (computer_choice == 2):
        print("You lose.")
    else:
        print("You win.")
elif (player_choice == 2):
    if (computer_choice == 3):
        print("You lose.")
    else:
        print("You win.")
elif (player_choice == 3):
    if (computer_choice == 1):
        print("You lose.")
    else:
        print("You win.")