import hangman
import guess

def choose_game():
    print("****************************")
    print("******* Choose a Game ******")
    print("****************************")

    print("(1=hangman) (2=guess)")
    game = int(input())

    if (game == 1):
        print("Playing hangman!")
        hangman.play_hangman()
    elif (game == 2):
        print("Playing guess!")
        guess.play_guess()

if(__name__ == "__main__"):
    choose_game()


