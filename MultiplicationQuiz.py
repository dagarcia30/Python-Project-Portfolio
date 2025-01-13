#Danny Garcia
#01-09-25
#multiplication quiz

#Initialize
import random
correct = 0
#Functions
def multiplication_quiz(questions):
    global correct
    print("Hello! Welcome to the multiplication quiz. Would you like to play?")
    while True:
         play = input("Yes or no")
         play = play.lower()
         if play == "yes":
            for i in range(questions):
                print("Okay get ready")
                number1 = random.randint(1,12)
                number2 = random.randint(1,12)
                correctanswer = number1 * number2
                print(str(number1) + " x " + str(number2))
                print("What do you think the answer is?")
                guess = int(input("What do you think the answer is?"))
                if guess == correctanswer:
                    print("Correct!")
                    correct = correct + 1
                else:
                    print("incorrect")
            print("Congrats on finishing this quiz! You finished with a " + str(correct) + "/" + str(questions))
         if play == "no":
            print("Bye,bye!")
            break



#Main
multiplication_quiz(5)
