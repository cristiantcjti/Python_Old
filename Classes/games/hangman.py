import random
 
def play_hangman():

    print_open_message()
    secret_word = load_secret_words()
    hidden_letters = stars_hidden_letters(secret_word) 
    
    errors = 0
    attempts = 7
    loose = False
    got_correct = False

    while (not loose and not got_correct ):
        
        guess_letter = take_guess()

        if (guess_letter in secret_word):
            set_correct_guess(guess_letter, hidden_letters, secret_word)
        else:
            errors += 1
            draw_gallows(errors)
            
        print(hidden_letters)
        if (errors == attempts):
            loose = True
            break
        if ("_ " not in hidden_letters):
            got_correct = True
            break
        
    if(loose): 
        print_loose(secret_word) 
    elif(got_correct):
        print_win()

    
    print("End of game!")

def print_open_message():
    print("****************************")
    print("Welcome to the Hangman Game")
    print("****************************")


def load_secret_words():
    secret_list = []
    with open("words.txt", "r") as file_words:
        for line in file_words:
            line = line.strip()
            secret_list.append(line)
    number = random.randrange(0,len(secret_list))
    secret_word = secret_list[number].upper()
    return secret_word

def stars_hidden_letters(secret_word):
    return ["_ " for letter in secret_word]  

def take_guess():
    guess = input("Guess a letter: ").strip().upper()
    return guess

def set_correct_guess(guess_letter, hidden_letters, secret_word):
    index = 0
    for letter in secret_word:
        if guess_letter == letter:
            hidden_letters[index] = letter
        index = index + 1  

def draw_gallows(errors):
    print("  _______     ")
    print(" |/      |    ")

    if(errors == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(errors == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(errors == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(errors == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(errors == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(errors == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (errors == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()

def print_loose(secret_word):
    print("This was the secret word:", secret_word)
    print(" You lost!") 
       
def print_win():
    print("Congratulations, you got it!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")
    
if(__name__ == "__main__"):
    play_hangman()