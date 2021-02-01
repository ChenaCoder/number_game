import numpy as np
import random as rand
numerOfround = None
questionsLeft = None
guessesLeft = None
numb = None
questionsLeft1 = None
guessesLeft1=None
b=None
a=None

# generates a random number
def start(parameterOne="", parameterTwo="1"):
    print("Welcome to number game. The way you play is pick a parameter for a number to be randomly picked.\nEnter the first number then hit enter and then the second and hit enter.\nex.1,10 the number will be between 1 and 10!")
    parameterOne = input()
    parameterTwo = input()
    global numb 
    numb = rand.randint(int(parameterOne), int(parameterTwo))
    return numb, guess()


#guessing
def guess():
    global questionsLeft
    global guessesLeft
    questionsLeft = 10
    guessesLeft=5
    b=guessesLeft
    a=questionsLeft
    print("Use the format x# x being the prameter and # being the number.\n>100,means that you are asking if the number is greater than 100.<100 means you think the number is less than 100.\nIf you want to guess the number use =#.You have ",
          questionsLeft, " questions and ", guessesLeft, " guesses. If you run out of guesses you lose!")
    guesss = input()
    guesss.replace("", "")
    intg = int(guesss[1:len(guesss)])
    if guessesLeft == 0:
        print("You lose! press enter to play again!")
        restart = input()
        if restart != "fhjfhgfiehuhugr59848hfhUHyyaygyfygfygfkdhcghchfjcj":
            start()
    if guesss[0:1] == "<":
        int(intg)
        if numb < intg:
            questionsLeft -= 1
            a=questionsLeft
            print("true")
            return questionsLeft, guess1(a,b)
        else:
            questionsLeft -= 1
            a=questionsLeft
            print("false")
            return questionsLeft, guess1(a,b)
    if guesss[0:1] == ">":
        int(intg)
        if numb > intg:
            questionsLeft -= 1
            a=questionsLeft
            print("true")
            return questionsLeft, guess1(a,b)
        else:
            questionsLeft -= 1
            a=questionsLeft
            print("false")
            return questionsLeft, guess1(a,b)
    if guesss[0:1] == "=":
        if guesss == "=" + str(numb):
            guessesLeft -= 1
            b=guessesLeft
            print("Congrats you have sucsessfully guessed the number: ", numb, "\nYou had: ",
                  guessesLeft, "guesses left and: ", questionsLeft, "questions left.\nIf you want to play again press enter.\nIf you would like to quit press ctrl + C")
            restart = input()
            if restart != "fhjfhgfiehuhugr59848hfhUHyyaygyfygfygfkdhcghchfjcj":
                return start()
        elif guesss != "=" + str(numb):
            print("wrong", guesss, ",", numb)
            guessesLeft -= 1
            b=guessesLeft
            return guessesLeft, guess1(a,b)
    return questionsLeft,guessesLeft



#guess 2 and on to work with counter
def guess1(questionsLeft1,guessesLeft1):
    print("Use the format x# x being the parameter and # being the number.\n>100,means that you are asking if the number is greater than 100.<100 means you think the number is less than 100.\nIf you want to guess the number use =#.You have ",
          questionsLeft1, " questions and ", guessesLeft1, " guesses. If you run out of guesses you lose!")
    guesss = input()
    guesss.replace("", "")
    intg = int(guesss[1:len(guesss)])
    if guessesLeft1 == 0:
        print("You lose! press enter to play again!\nYour number was: ",numb)
        restart = input()
        if restart != "fhjfhgfiehuhugr59848hfhUHyyaygyfygfygfkdhcghchfjcj":
            return start()
    if guesss[0:1] == "=":
        if guesss == "=" + str(numb):
            guessesLeft1 -= 1
            print("Congrats you have sucsessfully guessed the number: ", numb, "\nYou had: ",
                  guessesLeft1, "guesses left and: ", questionsLeft1, "questions left.\nIf you want to play again press enter.\nIf you would like to quit press ctrl + C")
            restart = input()
            if restart != "fhjfhgfiehuhugr59848hfhUHyyaygyfygfygfkdhcghchfjcj":
                return start()
        elif guesss != "=" + str(numb):
            print("wrong")
            guessesLeft1 -= 1
            return guessesLeft1, guess1(questionsLeft1,guessesLeft1)
    if questionsLeft1 ==0:
        print("You have run out of questions.Please press enter to continue to guess")
        restart = input()
        if restart != "fhjfhgfiehuhugr59848hfhUHyyaygyfygfygfkdhcghchfjcj":
            return guess1(questionsLeft1,guessesLeft1)
    if guesss[0:1] == "<":
        int(intg)
        if numb < intg:
            questionsLeft1 -= 1
            print("true")
            return questionsLeft1, guess1(questionsLeft1,guessesLeft1)
        else:
            questionsLeft1 -= 1
            print("false")
            return questionsLeft1, guess1(questionsLeft1,guessesLeft1)
    if guesss[0:1] == ">":
        int(intg)
        if numb > intg:
            questionsLeft1 -= 1
            print("true")
            return questionsLeft1, guess1(questionsLeft1,guessesLeft1)
        else:
            questionsLeft1 -= 1
            print("false")
            return questionsLeft1, guess1(questionsLeft1,guessesLeft1)
    


start()
