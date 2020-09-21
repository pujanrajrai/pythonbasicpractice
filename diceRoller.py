from random import randint
def diceNumber():
    file = open("dice.txt", "r")
    readfile = file.read()
    return readfile.split(",")

def rollDice():
    repeatDiceRoll = True
    while repeatDiceRoll:
        diceRolledNumber = randint(1, 6)
        print("You have got:", diceNumber[diceRolledNumber - 1])
        if diceRolledNumber == 6:
            print("you got one more chance")
            input("press any key to roll again")
        else:
            print("other turn")
            repeatDiceRoll = False

anotherRoll=True
anotherRollInput=None
diceNumber = diceNumber()
while anotherRoll:
    rollDice()
    anotherRollInput=input("enter any n to exit\nany other key to roll again\n").upper()
    if anotherRollInput=="N":
        anotherRoll=False

