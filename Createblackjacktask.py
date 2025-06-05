#Danny Garcia
#03/14/25
#BLACK JACK


#INITIALIZE
import random
deck = ["🂡","🂢","🂣","🂤","🂥","🂦","🂧","🂨","🂩","🂪","🂫","🂭","🂮","🂱","🂲","🂳","🂴","🂵","🂶","🂷","🂸","🂹","🂺","🂻","🂽","🂾","🃁","🃂","🃃","🃄","🃅","🃆","🃇","🃈","🃉","🃊","🃋","🃍","🃎","🃑","🃒","🃓","🃔","🃕","🃖","🃗","🃘","🃙","🃚","🃛","🃝","🃞"]
        #Spades                                               #Hearts                                                #Diamonds                                              #Clubs
#The list for the deck list was obatianed from one of my sources see below
global number
number = 0
global botnumber
botnumber = 0
global win
win = 0
global lose
lose = 0
#FUNCTIONS
def Intro(introquestion = input("Are you sure you want to enter? Yes or no")):
    print("Hello, welcome to Black Jack")
    introquestion.lower()
    if introquestion == "yes":
        while True:
            print("You chose yes to play so what would you like to do?")
            print(" ")
            print("1.Play")
            print("2.Stats")
            print("3.Quit")
            print(" ")
            options = input("1, 2, or 3?")
            if options == "1":
                play()
            if options == "2":
                stats()
            if options == "3":
                print("Come back")
                break
    if introquestion == "no":
        print("Come around soon.")

def botlevel(dif = input("What difficulty do you want to play? Easy, Medium, or Hard?")):
    global botnumber
    if dif == "easy":
        botnumber = random.randint(17,24)
    elif dif == "medium":
        botnumber = random.randint (18,22)
    elif dif == "hard":
        botnumber = random.randint(19,21)



def play():
    global lose
    global win
    global botnumber
    global number
    print("You've selected to play")
    number = random.randint(2,8)
    print(number)
    while True:
        botlevel()
        hitorno = input("Do you want to hit or stand?")
        if hitorno == "stand":
            print(number)
            print("Dealer has")
            print(botnumber)
            if number > botnumber and number < 21:
                print("Game won")
                win = win + 1
                break
            elif number == 21:
                print("You win!")
                win = win + 1
                break
            elif number > 21:
                print("You lose")
                lose = lose + 1
                break
            elif botnumber > 21:
                print("You win!")
                win = win + 1
                break
            elif botnumber == number:
                print("Tie")
                break
            elif botnumber == 21:
                print("You lose")
                lose = lose + 1
                break
            elif botnumber > 21 and number > 21:
                print("Tie")
                break
            elif botnumber > number and botnumber < 21:
                print("You lose")
                lose = lose + 1
            break
        if hitorno == "hit":
            card = random.randint(0,51)
            cardnum = card
            card = deck[card]
            print(card)
            if cardnum == 0 or cardnum == 13 or cardnum == 26 or cardnum == 39:
                print("You got an Ace!")
                ace = input("would you like a 1 or 11 for this ace?")
                if ace == "1":
                    number = number + 1
                    print(number)
                if ace == "11":
                    number = number + 11
                    print(number)
            elif cardnum == 1 or cardnum == 14 or cardnum == 27 or cardnum == 40:
                number = number + 2
                print(number)
            elif cardnum == 2 or cardnum == 15 or cardnum == 28 or cardnum == 41:
                number = number + 3
                print(number)
            elif cardnum == 3 or cardnum == 16 or cardnum == 29 or cardnum == 42:
                number = number + 4
                print(number)
            elif cardnum == 4 or cardnum == 17 or cardnum == 30 or cardnum == 43:
                number = number + 5
                print(number)
            elif cardnum == 5 or cardnum == 18 or cardnum == 31 or cardnum == 44:
                number = number + 6
                print(number)
            elif cardnum == 6 or cardnum == 19 or cardnum == 32 or cardnum == 45:
                number = number + 7
                print(number)
            elif cardnum == 7 or cardnum == 20 or cardnum == 33 or cardnum == 46:
                number = number + 8
                print(number)
            elif cardnum == 8 or cardnum == 21 or cardnum == 34 or cardnum == 47:
                number = number + 9
                print(number)
            elif cardnum == 9 or cardnum == 22 or cardnum == 35 or cardnum == 48:
                number = number + 10
                print(number)
            elif cardnum == 10 or cardnum == 23 or cardnum == 36 or cardnum == 49:
                number = number + 10
                print(number)
            elif cardnum == 11 or cardnum == 24 or cardnum == 37 or cardnum == 50:
                number = number + 10
                print(number)
            elif cardnum == 12 or cardnum == 25 or cardnum == 38 or cardnum == 51:
                number = number + 10
                print(number)

def stats():
    global win
    global lose
    print("Your current win loss ratio is ")
    print(str(win) + "/" + str(lose))
    if lose > 0:
        print(win/lose)







#MAIN
Intro()








#SOURCES
#https://www.alt-codes.net/playing-cards-symbols.php

