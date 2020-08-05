from random import randint

# Sets the initial number variable that the user will try and guess
# while also setting the win condition to false
number = randint(1, 20)
win_condition = False

# Sets the difficulty parameters
# The harder the difficulty the less guesses the user have
difficulty = {
    "easy" : 20, 
    "medium" : 10, 
    "hard" : 5
}

print("Hello and welcome to my guess the number game!!!")
sel_diff = input("Select your difficulty, Easy, Medium or Hard")
diff = difficulty.get(sel_diff.lower(), 5)

for i in range(diff):
    guess = int(input("Guess a number between 1 and 20: "))
    if guess == number:
        print("That's correct, you did it!")
        win_condition = True
        break
    elif guess > 20 or guess < 1:
        print("I said guess a number between 1 and 20 -_-")
    elif guess > number:
        print("Your guess is too high!")
    elif guess < number:
        print("Your guess is too low!")
    else:
        print("Please enter a valid number")

if win_condition == True:
    print("You won the game, congratulations!!!")
else:
    print("Sorry, you lost. Try again sometime!")


