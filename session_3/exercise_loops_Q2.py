number = input("Enter a number")
list_of_numbers = range(int(number)+1)
odd_numbers_list = []
for number in list_of_numbers:
    if number % 2 == 0:
        pass
    else:
        odd_numbers_list.append(number)
print(odd_numbers_list)