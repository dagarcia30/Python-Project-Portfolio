#Danny Garcia
#01-07-25
#Rock Paper Scissors

#Initialize
import random
global computer
global move
global win
global loss
global ties
win = 0
loss = 0
ties = 0
#Functions
def RPS():
    global computer
    global move
    global win
    global loss
    global ties
    print("Welcome to Rock, Paper, Scissors!")
    while True:
        print("Do you want to play?")
        play = input("Yes or No")
        play = play.upper()
        if play == "YES" or play == "Yes":
            print("Now pick one, Rock, Paper, or Scissors?")
            move = input("Rock, Paper, Scissors")
            move = move.upper()
            if move == "ROCK":
                move = 1
            if move == "PAPER":
                move = 2
            if move == "SCISSORS":
                move = 3
            computer = random.randint(1,3)
            #Rock
            if computer == 1 and move == 2:
                print("I choose ROCK you chose PAPER, YOU WIN")
                win = win + 1
            if computer == 1 and move == 1:
                print("We both chose ROCK, it's a tie")
                ties = ties + 1
            if computer == 1 and move == 3:
                print("I choose ROCK and you chose SCISSORS, you lose...")
                loss = loss + 1
            #Paper
            if computer == 2 and move == 2:
                print("We both chose PAPER, it's a tie")
                ties = ties + 1
            if computer == 2 and move == 1:
                print("I choose PAPER and you chose ROCK, you lose...")
                loss = loss + 1
            if computer == 2 and move == 3:
                print("I choose PAPER you chose SCISSORS, YOU WIN")
                win = win + 1
            #Scissors
            if computer == 3 and move == 2:
                print("I choose SCISSORS and you chose PAPER, you lose...")
                loss = loss + 1
            if computer == 3 and move == 1:
                print("I choose SCISSORS and you chose ROCK, YOU WIN")
                win = win + 1
            if computer == 3 and move == 3:
                print("We both chose SCISSORS, it's a tie")
                ties = ties + 1
            print("Wins")
            print(win)
            print("Losses")
            print(loss)
            print("Ties")
            print(ties)

        if play == "NO":
            print("Bye, Bye!")
            break

#Main
RPS()

