# This is my first phython program.
print ("Hello World")

# Here, my second code.
# Python code that generates a random number between 1 and 10 and asks the user to guess the number.
import random

number = random.randint(1, 10)

guess = int(input("Guess a number between 1 and 10: "))

if guess == number:
    print("Congratulations! You guessed the number correctly.")
else:
    print("Sorry, the number was", number)

