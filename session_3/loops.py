# Loops help us to perform the tasks multiple times
# letters = ['a', 'b', 'c']
# print(letters[0])

# 2 types of loops 
# While loops
# count = 0
# while 5 > count: #as long as this condition is true, the program will execute the following line
#     print("Hello")
#     count = count + 1

#     name = input("What is your name?")
#     while name != "Ashley":
#         print("I don't know you!")
#         name = input("Well, what's the new name?")


# For Loops
letters = ['a', 'b', 'c']
# for letter in letters: # letter = 'a'
#     print(letter)

# if we want to iterate for a certain amount of time, ..
#list_name[0:10] range() is similar to slicing
for number in range(10):
    print(number)

students = [
    ["Cindy", "Emily", "Eve"], 
    ["Julie", "Maddy", "Andrea"], 
    ["Jenny","Sarah", "Yara"]
    ]
for student in students:
    print(student)
    for name in student:
        print(name)