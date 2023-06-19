groceries = {
    "Baby Spinach": 2.78,
    "Hot Chocolate": 3.70,
    "Crackers": 2.10,
    "Coffee": 9.00,
    "Carrots": 0.56,
    "Oranges": 3.08}

question = print("Print the quantity of each item you would like to buy:")
total = 0

for key, value in groceries.items():
    item_quantity = input(key+":")
    item_price = value
    result = float(item_price) * int(item_quantity)
    total += result
print(f"The total cost of your groceries is ${total}")
