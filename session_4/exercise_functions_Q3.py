number = input("Enter a number")

def define_odd_numbers():
    if int(number) % 2 == 0:
        return False
    else:
        return True

answer = define_odd_numbers()
print(answer)