def play_hangman():

    print("****************************")
    print("Welcome to the Hangman Game")
    print("****************************")

    secret_word = "strawberry".upper()
    hidden_letters = ["_ " for letter in secret_word]
    guess_letter = ''
    letter = ''
    errors = 0
    attempts = 5
    loose = False
    got_correct = False

    while (not loose and not got_correct ):
        index = 0
        guess_letter = input("Guess a letter: ").strip().upper()
        if (guess_letter in secret_word):
            for letter in secret_word:
                if guess_letter == letter:
                    hidden_letters[index] = letter
                index = index + 1
        else:
            errors += 1
        
        print(hidden_letters)
        if (errors == attempts):
            loose = True
            break
        if ("_ " not in hidden_letters):
            got_correct = True
            break
        

    if(loose): 
        print(" You lost!") 
    elif(got_correct):
        print("You got it!")
    
    print("End of game!")

if(__name__ == "__main__"):
    play_hangman()
