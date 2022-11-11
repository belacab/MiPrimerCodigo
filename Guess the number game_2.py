import random
import sys


def getGuess():
    for i in range(3):
        try:
            guess = int(input())
            return guess
        except ValueError:
            print('Error, please introduce a number. ')
    print('You lose, try again from beginning. ')
    sys.exit()


print('Hello! What is your name? ')
name = input()
secretNumber = random.randint(1, 20)
print('Well, ' + name + ', I am thinking of a number between 1 and 20. ')

for guessesTaken in range(1, 7):
    print('Take a guess. ')
    guess = getGuess()
    if guess < secretNumber:
        print('Your guess is too low. ')
    elif guess > secretNumber:
        print('Your guess is to high. ')
    else:
        break


if guess == secretNumber:
    print('Good job, ' + name + '! You guessed my number in ' + str(guessesTaken) + ' guesses! ')
else:
    print('Nope. The number I was thinking of was ' + str(secretNumber))
