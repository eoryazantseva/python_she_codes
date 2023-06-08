print("Guess the random number!")
number = 76
guess_attempt = input("Make a guess:")

while(True):
    if int(guess_attempt) < 76:
        print("Too low...")
        guess_attempt = input("Make another guess:")
    elif int(guess_attempt) > 76:
        print("Too high...")
        guess_attempt = input("Make another guess:")
    elif int(guess_attempt) == 76:
        print("You got it right!")
        break