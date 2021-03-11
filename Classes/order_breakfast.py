import time

def conclusion():
    print("Your order will be ready shortly.")
    time.sleep(1)

def order():
    while True:
        response = input("Please place your order. Would you like waffles or pancakes?\n").lower()
        if "waffles" in response:
            print("Waffles it is!")
            time.sleep(1)
            conclusion()
            break
        elif "pancakes" in response:
            print("Pancakes it is!")
            time.sleep(1)
            conclusion()
            break
        else:
            print("Sorry, I don't understand.")
            time.sleep(1)

def another_order():
    while True:
        response_2 = input("Would you like to place another order? Please say 'yes' or 'no'.\n").lower()
        if 'yes' in response_2:
            print('Very good, I\'m happy to take another order.')
            time.sleep(1)
            order()
        elif 'no' in response_2:
            print('Ok, goodbye!')
            time.sleep(1)
            break


print("Hello! I am Bob, the Breakfast Bot.")
time.sleep(1)
print("Today we have two breakfasts available.")
time.sleep(1)
print("The first is waffles with strawberries and whipped cream.")
time.sleep(1)
print("The second is sweet potato pancakes with butter and syrup.")
time.sleep(1)

order()
another_order()
