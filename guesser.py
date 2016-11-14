def runGuesser():
    import random
    # Initializie the program
    print ("Guess a number between 1 and 100.")
    # randomNumber = 35 # for debugging only
    randomNumber = random.randint(1,100)
    found = False   # Flag variable to see if they guessed it
    # Run through the guessing process
    while not found:
        userGuess = int(input("your guess: "))
        if userGuess == randomNumber:
            print ("You got it!")
            found = True
        elif userGuess > randomNumber:
            print ("Guess lower!")
        else:
            print ("Guess higher!")

    print ("Thanks for playing our guessing game.")
    return
    

def main():
    runGuesser()

if __name__ == "__main__":
    main()
    
