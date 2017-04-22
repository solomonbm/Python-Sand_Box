# This is a guess the number game.
import random
def runGuesser(n):
    secretNumber = random.randint(1, n)
    print('I am thinking of a number between 1 and ' + str(n) + '.')

    # Ask the player to guess 6 times.
    for guessesTaken in range(1, 7):
        print('Take a guess.')
        guess = int(input())

        if guess < secretNumber:
            print('Your guess is too low.')
        elif guess > secretNumber:
            print('Your guess is too high.')
        else:
            break    # This condition is the correct guess!

    if guess == secretNumber:
        print('Good job! You guessed my number in ' + str(guessesTaken) + ' guesses!')
    else:
        print('Nope. The number I was thinking of was ' + str(secretNumber))    

def main():
    runGuesser(30)
    runGuesser(50)

if __name__ == "__main__":
    main()
    
