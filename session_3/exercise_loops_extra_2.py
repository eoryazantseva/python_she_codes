print("Guess the random number!")
import random

while True:
    number = random.randrange(0, 10)
    guess_attempt = int(input("Make a guess:"))

    while(guess_attempt != number):
        if guess_attempt < number:
            print("Too low...")
        else:
            print("Too high...")
        guess_attempt = int(input("Make another guess:"))
    print("You get it right!")

    question = input("If you would like to stop playing, enter 'no'. Otherwise, we'll play again. ")
    if question.lower() == "no":
        print("See you later!")
        break
