from random import randrange

# hintGiver function takes theAnswer and noOfGuesses and calculates two numbers which has theAnswer between it.
def hintGiver(answer, guesses):
    
    lenghtOfHint = 20 - (4*(guesses-1))
    upperLimit = answer + lenghtOfHint
    lowerLimit = answer - lenghtOfHint
    # I made this randomCenterNumber because I didn't wanted the answer to be mean of the list. 
    # If I used theAnswer as randomCenterNumber then you can guess easily by taking mean of the hintUpper and hintLower. 
    
    randomCenterNumber = randrange(lowerLimit, upperLimit)
    hintUpper = randomCenterNumber + lenghtOfHint
    hintLower = randomCenterNumber - lenghtOfHint
    if hintLower < 0:
        hintLower = 1

    return print("Hint : The answer is between %d and %d" % (hintUpper, hintLower))
        
# declaring the variable theAnswer and noOfGuesses
theAnswer = randrange(1, 101)
print(theAnswer)
noOfGuesses = 0
while True:
    guessedAnswer = (input("=============================================\nGuess what the number is between 1 to 100: "))

    if noOfGuesses == 5:
        print("You have used all 5 tries, better luck next time!")
        break
    elif theAnswer == guessedAnswer:
        pointsScored = 50 + (noOfGuesses*10)
        print("Congrats, That's the correct answer!! You have scored %d points in %d guesses" % (pointsScored, noOfGuesses))
        break
    elif not(guessedAnswer == theAnswer): 
        print(guessedAnswer, theAnswer)
        noOfGuesses += 1
        print("Please Try again. You have more %d guesses" % (5 - noOfGuesses))
        hintGiver(theAnswer, noOfGuesses)

    print("=============================================\n")