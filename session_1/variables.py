# Create a variable named first_name and assign Asli
first_name = "Asli"
last_name = "Yoruk"
programming_language = "Python"

# Data Types - Text data, numerical data
# Text data - String

today = "Tuesday"

# print(today)
# print(f"Today is {today}")
# print(type(today))

# Numerical data types - Integer, Float
# Integer - whole number

parkers_age = 4
print(type(parkers_age))
print(f"Parker is turning {parkers_age+1} soon! ")

height = 162
print(f"My height is {height/100} in metres")


#float
weight = 47.67
print(type(weight))
print(f"My weight is {weight*2.1} in lbs")


#string data type ""
distance = "5000"
print(int(distance) + 8)
print(distance + str(8))


#this function expects input
# input("Hello")

# I take the information about the dog's name from the user
dog_name = input("What's the dog's name?")
print(f"Nice to meet you {dog_name}")


# Input stores data as a string
birth_year = input("What year were yu born?")
print(f"You are {2023-int(birth_year)} years old")