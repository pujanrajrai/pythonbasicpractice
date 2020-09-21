from random import randint
choice = ["Rock", "Scissors", "Paper"]
def computerRSPguess():
    computerRSP = randint(0, 2)
    print(choice[computerRSP])
    return computerRSP

def userRSPinput():
    inputBool=True
    while inputBool:
        userRSP = None
        try:
            userRSP=int(input('press 1 to choose rock\npress 2 to choose scissor\npress 3 to choose paper\n'))-1
            if userRSP<0 or userRSP>2:
                print("input value is not valid")
                print("please select following")
            else:
                inputBool=False
                return userRSP
        except:
            if userRSP==None:
                print("you cannot leave input field empty")
            else:
                print("invalid input number only allowed")

def winnerRSP(userRSP,computerRSP):
    if userRSP==computerRSP:
        print("both have choosen",choice[userRSP])
        print("Draw")
    else:
        if choice[userRSP]=="Rock":
            print("You have choosen", choice[userRSP], "Computer have choosen", choice[computerRSP])
            if choice[computerRSP]=="Scissors":
                print("You won over computer")
            else:
                print("You loose")
        elif choice[userRSP]=="Scissors":
            print("You have choosen", choice[userRSP], "Computer have choosen", choice[computerRSP])
            if choice[computerRSP]=="Paper":
                print("You won over computer")
            else:
                print("You loose")

        elif choice[userRSP]=="Paper":
            print("You have choosen", choice[userRSP], "Computer have choosen", choice[computerRSP])
            if choice[computerRSP]=="Rock":
                print("You won over computer")
            else:
                print("You loose")


repeatRSP=True
while repeatRSP:
    computerRSP=computerRSPguess()
    userRSP = userRSPinput()
    winnerRSP(userRSP,computerRSP)
    repeatRSPinput = input("enter y to play again").upper()
    print(repeatRSPinput)
    if repeatRSPinput !="Y":
        repeatRSP=False






