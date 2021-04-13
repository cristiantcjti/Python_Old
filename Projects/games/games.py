import hangman
import guess
import adventure_game

def choose_game():
    print("****************************")
    print("******* Choose a Game ******")
    print("****************************")

    print("(1=hangman) (2=guess) (3=adventure_game)")
    game = int(input())

    if (game == 1):
        print("Playing hangman!")
        hangman.play_hangman()
    elif (game == 2):
        print("Playing guess!")
        guess.play_guess()
    elif (game == 3):
        print("Playing adventure_game!")
        adventure_game.play_adventure_game()

if(__name__ == "__main__"):
    choose_game()


