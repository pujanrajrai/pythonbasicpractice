import random

def setRange():
    ranges=True
    while ranges:
        try:
            lowerRange=int(input("Enter lower range value"))
            upperRange=int(input("Enter upper range value"))
            randomNumber = random.randint(lowerRange+1,upperRange-1)
            print(randomNumber)
            return lowerRange,upperRange,randomNumber
        except:
            print("Invalid input range")
def inputNumber(lowerRange,upperRange):
    randBool = True
    while randBool:
        guessNumber = None
        try:
            guessNumber=int(input(f"Guessed Numbered between {lowerRange} to {upperRange}"))
            if guessNumber<lowerRange or guessNumber >upperRange:
                print(f"Number you have input is not in range between {lowerRange} to {upperRange}")
            else:
                randBool=False
                return guessNumber
        except:
            if guessNumber==None:
                print("please donot leave field empty")
            else:
                print("Only integer number input allowed")
def guessCheck(lowerRange,upperRange,randomNumber,guessNumber):
    while guessNumber != randomNumber:
        if guessNumber > randomNumber:
            upperRange = guessNumber
            print(f"The actual number is more than {lowerRange} and less than {guessNumber}")
            guessNumber = inputNumber(lowerRange, upperRange)
        elif guessNumber < randomNumber:
            lowerRange = guessNumber
            print(f"The actual number is more than {guessNumber} and less than {upperRange}")
            guessNumber = inputNumber(lowerRange, upperRange)
    print("you have guessed the right number")

repeatGuess=True
while repeatGuess:
    lowerRange, upperRange, randomNumber = setRange()
    guessNumber = inputNumber(lowerRange, upperRange)
    guessCheck(lowerRange,upperRange,randomNumber,guessNumber)
    repeatGuessInput=input("Enter Y to continue and any other key to exit")
    print(repeatGuessInput)
    if repeatGuessInput.upper() !="Y":
        repeatGuess=False
