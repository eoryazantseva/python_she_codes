price_per_unie = input("Enter a unit price")
num_units = input("Enter a quantity")

def total():
    result = float(price_per_unie) * int(num_units)
    return result

answer = total()
print(f"You spent ${answer}")
