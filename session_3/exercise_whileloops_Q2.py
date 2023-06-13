# WIth for loop

# number = input("Enter a number")
# list_of_numbers = range(int(number)+1)
# odd_numbers_list = []
# for number in list_of_numbers:
#     if number % 2 == 0:
#         pass
#     else:
#         odd_numbers_list.append(number)
# print(odd_numbers_list)


# With while loop

print("The first number is 0")
large_number = int(input("Enter a number: "))
while (large_number > 0):
    if (large_number % 2 != 0):
        print(large_number)
    large_number = large_number - 1