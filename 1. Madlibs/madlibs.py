#title screen/introduction
print("================================")
print("+++++++Mad Libs Generator+++++++")
print("================================")

# function for game code.
def game():
    # the part of the game where various inputs are taken from the user
    name = input("Enter an noun: ")
    verb = input("Enter an verb: ")
    adverb = input("Enter an adverb: ")
    name2 = input("Enter an noun2: ")

    #the story template and output part of the function.
    print("================================================================================")
    print("%s was sad on a monday afternoonY, and was %s %sing. But then called %s and he was happy thereafter." % (name, adverb, verb, name2))
    print("================================================================================")


wantsToPlay = input("Do you want to play the game of Mad libs?(Y/N): ")
wantsToPlay = wantsToPlay.lower()

if wantsToPlay == "y":
    game()
elif wantsToPlay == "n":
    print("quitting...")
else: 
    print("invalid option, quitting....")