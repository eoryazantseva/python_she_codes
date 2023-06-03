# Boolean
# name = "Asli"
# age = 19
# height = 1.5
# is_raining = True
# my_variable2 = False
# print(is_raining)
# print(type(my_variable))
# Boolean expressions - Expressions that produce  aboolean values
# Comparson operators
#  == is equal to
# > greater than
#  < less than
#  >= greater or equial to
# <= less or equal to 
# print(5 > 3)
# print(3.5 > 6.3)
# print("Asli" == "Asli")

# Mathematical Operators - Addition, Division, Subtraction, Multiplication
# Boolean operators - not, and, or

# is_sunny = True
# is_warm = True
# print(not is_sunny)
# print(is_sunny and is_warm)
# print(is_sunny == is_warm)
# print(is_sunny != is_warm)


# print(is_sunny or is_warm)
# at least one of those conditions is true, then the whole statement is true

temperature = 20
# syntax (grammar) / semantics (logic)
if temperature < 18:
    print("Weather is too cold!")
    print("I want to stay home")
# elif - else if (if we add another condition that needs to be checked)

elif temperature > 28: #if if statement is false, it will check elif
    print("Weather is too hot!") #multiple elif statements
else:
    print("Weather is nice!")


