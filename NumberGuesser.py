#Danny Garcia
#11/08/24

#initialize
import random

#Functions
def numbergame(numberguess):
    print("Do you want to play the random number game?")
    yesno=input("yes or no")
    if yesno == ("yes"):
        print("What difficulty do you want? Easy, Medium, or hard")
        print("Easy is 1-10, Medium is 1-100, and Hard is 1-1000")
        emh=input("Easy,Medium,Hard")
        if emh==("Easy"):
            print("You chose Easy mode")
            print("Guess a number then")
            number=random.randint(0,10)
            print(numberguess)
            print("You guessed this number? Well..")
            if number == numberguess:
                print("You guessed the right number!")
            else:
                print("WRONG!")
            print("The correct number is")
            print(number)
            if number > numberguess:
                print("You were too low")
            if number < numberguess:
                print("You were too high")
        elif emh==("Medium"):
            print("You chose Medium mode")
            print("Guess a number then")
            number=random.randint(0,100)
            print(numberguess)
            print("You guessed this number? Well..")
            if number == numberguess:
                print("You guessed the right number!")
            else:
                print("WRONG!")
            print("The correct number is")
            print(number)
            if number > numberguess:
                print("You were too low")
            if number < numberguess:
                print("You were too high")
        elif emh==("Hard"):
            print("You chose Hard mode")
            print("Guess a number then")
            number=random.randint(0,1000)
            print(numberguess)
            print("You guessed this number? Well..")
            if number == numberguess:
                print("You guessed the right number!")
            else:
                print("WRONG!")
            print("The correct number is")
            print(number)
            if number > numberguess:
                print("You were too low")
            if number < numberguess:
                print("You were too high")
    else:
        print("Leave")
#Main
numbergame(10)
