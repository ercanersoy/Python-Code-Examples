import sys
from random import random

count_of_numbers = int(input("Count of guess (1-10): "))

if count_of_numbers < 1 and count_of_numbers > 10:
    print("Wrong input!")
    sys.exit()

print("A decimal random number generating between 0 to 100.")
random_number = int(random() * 100.0)
print("A decimal random number have generated between 0 to 100.")

for i in range(count_of_numbers, 0, -1):
    print(i, end="")
    print(" guess remaining.")
    guessed_number = int(input("Enter a decimal number: "))

    if random_number == guessed_number:
        print("Congratulations! You have guessed this random number.")
        sys.exit()
    elif random_number < guessed_number:
        print("You should guess a smaller decimal number.")
    else:
        print("You should guess a bigger decimal number.")

print("You have not been guessed this random number.")