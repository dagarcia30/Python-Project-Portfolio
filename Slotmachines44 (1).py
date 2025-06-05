#Danny Garcia
#01-29-25


#Initialize
import random
import time
symbols = ["♣", "♣", "☆", "☆" "7", "♥", "♥", "♦", "♦", "♠", "♠"]
global money
money = 100

#Functions
def slotmachine():
    print("Heyyyyy welcome to the slot machine!")
while True:
    play = input("Do you want to play or not.")
    play = play.lower()
    print("You have this many dollars")
    print(money)
    if play == "yes":
        print("you must have atleast one dollar left AFTER your bet")
        cost = input("How much do you want to bet")
        cost = int(cost)
        money = money - cost
        if money < cost:
            print("You're too broke get money")
            break
        print("The slots are spinning!")
        slotoutcome1 = random.choice(symbols)
        slotoutcome2 = random.choice(symbols)
        slotoutcome3 = random.choice(symbols)
        time.sleep(1)
        print(slotoutcome1)
        print(slotoutcome2)
        print(slotoutcome3)
        if slotoutcome1 == "7" and slotoutcome2 == "7" and slotoutcome3 == "7":
            print("YOU GOT THE JACKPOT")
            print("You earned 100x!!!")
            money = money + cost*100
            print("You have this many dollars")
            print(money)
        if slotoutcome1 == "☆" and slotoutcome2 == "☆" and slotoutcome3 == "☆" or slotoutcome1 == "♣" and slotoutcome2 == "♣" and slotoutcome3 == "♣" or slotoutcome1 == "♠" and slotoutcome2 == "♠" and slotoutcome3 == "♠" or slotoutcome1 == "♦" and slotoutcome2 == "♦" and slotoutcome3 == "♦" or slotoutcome1 == "♥" and slotoutcome2 == "♥" and slotoutcome3 == "♥":
            print("You win!")
            print("You earned 10x")
            money = money + cost*10
            print("You have this many dollars")
            print(money)
        if slotoutcome1 == slotoutcome2 or slotoutcome1 == slotoutcome3 or slotoutcome2 == slotoutcome3:
            print("You won 2x")
            money = money + cost*2
        else:
            print("you lost")
            print("You have this many dollars")
            print(money)

    if play =="no":
        print("See you in a little")
        break

#Main
slotmachine()
