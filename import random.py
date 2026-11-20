import random

print("Welcome to my small rock, paper, scissors program!")

choices = ["rock", "paper", "scissors"]

while True:
    print("Choose: 1. Rock 2. Paper 3. Scissors")

    try:
        choice = int(input("Enter your choice: "))
    except ValueError:
        print("Enter a valid number")
        continue

    while choice < 1 or choice > 3:
        choice = int(input("Enter a valid number from 1 to 3: "))
        

    user_choice = choices[choice - 1]

    print("Your choice is:", user_choice)
    print("The computer will choose now")

    comp_choice = random.randint(1, 3)
    computer_choice = choices[comp_choice - 1]

    print("Computer choice is:", computer_choice)

    if choice == comp_choice:
        print("Oh, it's a tie. Try again")
    
    elif (
        (choice == 1 and comp_choice == 3)
        or (choice == 2 and comp_choice == 1)
        or (choice == 3 and comp_choice == 2)
    ):
    
        print("YOU WIN YAYYYY")
    
    
    else:
        print("Oh no ): The computer wins")

    while True:
        answer = input("Do you want to play again Y/N?: ").strip().upper()

        if answer == "N":
            break

        print()

print("Thank you for playing!")
