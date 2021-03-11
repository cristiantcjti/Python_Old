print("****************************")
print("Welcome to the Guessing Game")
print("****************************")

secret_number = 42

guess_str = input("Guess a number: ")

print("This is the number you typed: ", guess_str)
5
guess = int(guess_str)

correct = guess == secret_number
lower = guess > secret_number
higher = guess < secret_number

if (secret_number == guess):
    print("You got it!")
else:
    if (lower):
        print("You failed! The secret number is lower.")
    elif (higher):
        print("You failed! The secret number is higher.") 

print("End of game!")