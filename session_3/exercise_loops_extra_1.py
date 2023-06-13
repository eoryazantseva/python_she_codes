groceries = [    
    ["Baby Spinach", 2.78],    
    ["Hot Chocolate", 3.70],    
    ["BBQ Shapes", 9.00],    
    ["Bread", 2.10],    
    ["Carrots", 0.56],    
    ["Oranges", 3.08]
    ]

total = 0

for item in groceries:
    quantity = int(input(f"Please enter the quantity for " + item[0]+ " "))
    print(quantity)
    item_total = quantity * item[1]
    print(item_total)
    total += item_total
print(f"Thank you, your Total is {total}")