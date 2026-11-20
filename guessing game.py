import random

random_number = random.randint (1, 20)

print ("hello this is a gussing game\nyou will have five tries to guess\nthe range is from 1 to 20" )


tries = 0


while (tries < 5):
    guess= input("enter a number from 1 to 20: ")

    guess = int(guess)
    
    if guess == random_number:
        print (f"you win!! you guessed correcrtly. in {tries + 1}")
        break

    elif guess > random_number:
        print("too high! try again")

    elif guess < random_number:
        print ("too low! try again")

    else:
        print("make sure to enter a valid number!")

    tries +=1

else:
    print("you lost")
