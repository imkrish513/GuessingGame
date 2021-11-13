import random

print("Welcome to the Number Guessing Game")

value = random.randint(1,9)

guesses = 0

print("The goal of the game is to guess a number between 1-9")

while(guesses < 5):
    guess = int(input("Enter you guess: "))
    if(guess == value):
        print("You guessed the correct number!")
        break
    elif(guess < value):
        print("You guessed too low, try something higher, you have",5-guesses,"remaining")
    else:
        print("You guessed too high, try something lower, you have",5-guesses,"remaining")
    guesses+=1

if(guesses == 5):
    print("Sorry you lost :( , the number was",value)