from random import randint

# Sets the initial number variable that the user will try and guess
number = randint(1, 20)
sel_diff = None
# Variable to keep the game loop running
game_loop = True

# Sets the difficulty parameters
# The harder the difficulty the less guesses the user have
difficulty = {
    "easy" : 20, 
    "medium" : 10, 
    "hard" : 5
}

# Keeps the game loop running as long as the game_loop variable is true
while game_loop == True:

    # Sets the win_condition variable to false, if true the user has won the game
    win_condition = False

    print("Hello and welcome to my guess the number game!!!")
    while True:
        sel_diff = input("Select your difficulty, Easy, Medium or Hard ")
        if sel_diff.lower() in ["easy", "medium", "hard"]:
            break
        else:
            print("Please enter one of the listed difficulties.")

    diff = difficulty.get(sel_diff.lower())
    count = diff

    while count > 0:
        print(f"You have {count} guesses left")
        guess = input("Guess a number between 1 and 20: ")
        # Checks if the guess is a valid integer
        try:
            guess == int(guess)
        except ValueError:
            print("Please enter a valid number")
            continue

        guess = int(guess)

        if guess == number:
            print("That's correct, you did it!")
            win_condition = True
            break
        elif guess > 20 or guess < 1:
            print("I said guess a number between 1 and 20 -_-")
        elif guess > number:
            print("Your guess is too high!")
            count = count - 1
        elif guess < number:
            print("Your guess is too low!")
            count -= 1

    # Declares wether the player won or lost the game and lets them retry again
    if win_condition == True:
        print("You won the game, congratulations!!!")
        cont = input("Would you like to try again? yes/no ")
        if cont.lower() == "yes":
            continue
        else:
            game_loop = False
    else:
        print("Sorry, you lost.")
        cont = input("Would you like to try again? yes/no ")

        if cont.lower() == "yes":
            continue
        else:
            game_loop = False

print("Hope you'll play again someday!")
