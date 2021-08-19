import random

roll = random.randint(1, 6)

guess = input("Guess the dice roll: ")
guess = int(guess)

if guess == roll:
	print("Correct!")
else:
	print("Wrong!")
	
print("The computer rolled a " + str(roll))
