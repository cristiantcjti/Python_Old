import time
import random


def print_pause(message_to_print):
    print(message_to_print)
    time.sleep(2)


def intro(place, build, transport):
    print_pause("You find yourself in a huge unknown " + place + ".")
    print_pause("You are lost, trying to find the way to come back to the"
                " hotel.")
    print_pause("In front of you there are two routes.")
    print_pause("One route is dark,full of " + build + " and there is a bank"
                " machine\n"
                "there.The other one is well illuminated and there is a\n"
                + transport + "terminal in the end of the route.\n")


def valid_input(message, option1, option2):
    while True:
        response = input(message).lower()
        if option1 in response:
            break
        elif option2 in response:
            break
    return response


def valid_input_group(message, options):
    while True:
        response = input(message).lower()
        for option in options:
            if option in response:
                return response


def choose_way(wallet):
    print_pause("Which way will you decide to go?\n"
                "Enter 1 to take the dark route .\n"
                "Enter 2 to take the well illuminated one.")

    choice_way = valid_input("(Please enter 1 or 2.)\n", "1", "2")
    if "1" in choice_way:
        dark_route(wallet)
    elif "2" in choice_way:
        illuminated_route(wallet)


def dark_route(wallet):
    if "2" in wallet or "5" in wallet:
        print_pause("Hey, wait...you know the dangerous gangue over there.\n"
                    "It is better come back and take the other route.\n")
        illuminated_route(wallet)
    else:
        print_pause("You keep walking by the dark route...")
        print_pause("Suddenly, as you are just passing by in front of the\n"
                    "bank machine, you decide to withdraw a sum of money\n"
                    "because you haven't any money to pay the bus charge.")
        print_pause("But there are only low-value bills of 2 or 5.")

        amount = valid_input("(Please enter the value of the bill you want"
                             " withdraw 2 or 5.)\n", "2", "5")
        wallet.append(amount)

        print_pause("Soon after withdrawing the bill you see a suspected group"
                    "is\n""approching to you.!!!")
        print_pause("So you need to decide whether you should stay or run"
                    "away.")

        decision = valid_input_group("(Please enter your decision, stay or"
                                     "run?)\n", ["stay", "run"])

        if "stay" in decision:
            print_pause("Worst decision. The group hits and robs you. You"
                        "have\n no more chance to come back to the hotel."
                        "SORRY!")
            play_again(wallet)
        elif "run" in decision:
            print_pause("Best decision. You flee from the group and return"
                        "to\n the previous spot ready to choose your route"
                        "again.\n")
            choose_way(wallet)


def illuminated_route(wallet):
    print_pause("You chose the safer route...")
    print_pause("After all, your aim is getting on a bus toward the hotel.")
    print_pause("You arrive at the terminal. You go to buy the ticket bus.\n")
    if "2" in wallet:
        print_pause("Nooo! The ticket charge is 4. Unfortunately you can't buy"
                    "it")
    elif "5" in wallet:
        print_pause("Well done!!! You have the required sum of money as you've"
                    " withdrawn 5.\n"
                    "Eventually, you can go safe and sound to the hotel!!!")
        play_again(wallet)
    else:
        print_pause("Oh no!!! You haven't any money in on wallet. Ok time to\n"
                    "go back to the dark route to withdraw some money...\n")
        dark_route(wallet)


def adventure_game():
    wallet = []
    place = random.choice(["town", "city", "country", "countryside"])
    build = random.choice(["houses", "buildings", "factories"])
    transport = random.choice(["bus ", "cab"])
    intro(place, build, transport)
    choose_way(wallet)


def play_again(wallet):
    while True:
        again = valid_input_group("Whould you like to play again? (yes/no)\n",
                                  ["yes", "no"])
        if "yes" in again:
            adventure_game()
            break
        elif "no" in again:
            print_pause("Ok!!! Good Bye.")
            break


adventure_game()
