# Lists
# numbers = [1, 2, 3]
# numbers[0]
# Dictionary
# Keys are unique
# Values can ony be immutable data types
# Immutable data types are usuallu single data types like strings, integers, floats, booleans
student_phonebook = {
    "Cindy": 111, #CIndy is a key, 111 is a value
    "Tracey": 123,
    "Pauline":444
    }

print(student_phonebook)
# print(type(student_phonebook))
student_phonebook["Yara"] = 555 # added new key and value
print(student_phonebook)
# print(student_phonebook("Asli")) # will show KeyError as "Asli" does not exist


# deleting
# del student_phonebook["Tracey"]
# print(student_phonebook)

# Iterate allthe key-value pairs:
# for key in student_phonebook:
#     print(key, student_phonebook[key])

a,b = [1,2]
print(a)
print(b)

for key,value in student_phonebook.items():
    print(key,value)