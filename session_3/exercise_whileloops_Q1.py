#Solution 1

number = input("Enter a number")
number_list = []
while number != '':
    number_list.append(int(number))
    number = input("Enter another number")
if  number == '':
    print(f"Your numbers sum to {sum(number_list)}")

