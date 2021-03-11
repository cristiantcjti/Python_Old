print("****************************")
print("Welcome to the Guessing Game")
print("****************************")

secret_number = 42
total_attempts = 3


# With for loop
for round in range(1,total_attempts+1):
    print("Round {} of {}.".format(round,total_attempts))
    guess_str = input("Guess a number: ")
    print("This is the number you typed: ", guess_str)
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



# With while loop
"""
while (round <= total_attempts):
    print("Round {} of {}.".format(round,total_attempts))
    guess_str = input("Guess a number: ")
    print("This is the number you typed: ", guess_str)
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
    round = round + 1
print("End of game!")
"""
