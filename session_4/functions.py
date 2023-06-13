# Function is an activty that is natural to or the purpose of a person or a thing.
# Functions we've already seen.

# input(), len(), int(), print()
# name = input("What is your name?")
# age = input("How old are you?")
# if age >= 18:
#     print("Welcome")
# else:
#     print("You can not enter")

# Task separation
# def ask_user_name():
#     name = input("What is your name?")
#     return name
# print("Hello") #will not be executed as it comes after "return"


# answer = ask_user_name() # we are calling the function. DEfinition of the function should always come first.
# print(answer)


# def ask_user_age():
#     age = input("How old are you?")
#     if age >=18:
#         print("Welcome")
#     else:
#         print("You can not enter.")




# Parameters
def add(number1, number2): # number1 = 2, number2 = 3
    result = number1 + number2
    return result # It is LOCAL VARIABLE, it doesn not exist outside of the function

answer = add(2,3) #answer is created outside of the function, it's GLOBAL VARIABLE. It can be called from anywhere in the file
print(answer)