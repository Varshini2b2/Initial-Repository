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

#Python code that displays a smiley face after it runs
print("\U0001F600")

#Python code that generates a pyramid of asterisks (*) based on user input
rows = int(input("Enter the number of rows for the pyramid: "))

for i in range(1, rows+1):
    for j in range(1, rows-i+1):
        print(" ", end="")
    for j in range(1, 2*i):
        print("*", end="")
    print()

