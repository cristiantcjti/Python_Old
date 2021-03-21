import random

def play_guess():      
    print("****************************")
    print("Welcome to the Guessing Game")
    print("****************************")

    secret_number = random.randrange(1,101) 
    total_attempts = 0
    points = 1000

    print("Select the round level:",secret_number)
    print("(1 = Easy) (2 = Moderate) (3 = Hard)):")
    level =  int(input())

    if (level == 1):
        total_attempts = 10
    elif (level == 2):
        total_attempts = 5
    else:
        total_attempts = 3


    # With for loop
    for game_round in range(1,total_attempts+1):
        print("Round {} of {}.".format(game_round,total_attempts))
        guess_str = input("Guess a number between 1 and 100: ")
        print("This is the number you typed: ", guess_str)
        guess = int(guess_str)

        if (guess < 1 or guess > 100):
            print("Your guess have to be between 1 and 100!")
            continue

        correct = guess == secret_number
        lower = guess > secret_number
        higher = guess < secret_number

        if (secret_number == guess):
            print("You got it!")
            print(f"You scored {points}")
            break
        else: 
            lost_points = abs(secret_number - guess)
            points = points - lost_points  
            if (lower):
                print("You failed! The secret number is lower.")
                if (game_round == total_attempts):
                    print(f"The secret number was {secret_number}. You scored {points}")
            elif (higher):
                print("You failed! The secret number is higher.") 
                if (game_round == total_attempts):
                    print(f"The secret number was {secret_number}. You scored {points}")
    print("End of game!")

if(__name__ == "__main__"):
    play_guess()

    # With while loop
    """
    while (game_round <= total_attempts):
        print("Round {} of {}.".format(game_round,total_attempts))
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
        game_round = game_round + 1
    print("End of game!")
    """
