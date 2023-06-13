print("Guess the random number!")
number = 76
guess_attempt = int(input("Make a guess:"))

while(guess_attempt != number):
    if guess_attempt < number:
        print("Too low...")
    else:
        print("Too high...")
    guess_attempt = int(input("Make another guess:"))
print("You get it right!")