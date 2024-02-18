# Simple Calculator - A simple calculator program
# Copyright (c) 2020 Ercan Ersoy
# This file licensed under MIT License.

while True:
    print("1. Addition")
    print("2. Substraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")
    choice = input("Your choice: ")
    print()
    
    if choice == "1":
        first_addend = float(input("First addend: "))
        second_addend = float(input("Second addend: "))
        print("Result: ", end="")
        print(first_addend + second_addend)
    elif choice == "2":
        first_subtrahend = float(input("First subtrahend: "))
        second_subtrahend = float(input("Second subtrahend: "))
        print("Result: ", end="")
        print(first_subtrahend - second_subtrahend)
    elif choice == "3":
        multiplier = float(input("Multiplier: "))
        multiplicand = float(input("Multiplicand: "))
        print("Result: ", end="")
        print(multiplier * multiplicand)
    elif choice == "4":
        dividend = float(input("Dividend: "))
        divider = float(input("Divider: "))
        print("Result: ", end="")
        print(dividend / divider)
    elif choice == "5":
        break
    else:
        print("Wrong choice!")
    
    print()