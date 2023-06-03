# Given the list of foods below, print:
    ## The first item in the list.
    ## The third item in the list.
    ## The last item in the list.
    ## The first three items in the list.
    ## The last three items in the list.
    ## The last item in the sublist

foods = [
    "orange",
    "apple",
    "banana",
    "strawberry",
    "grape",
    "blueberry",    
    ["carrot", "cauliflower", "pumpkin"],
    "passionfruit",
    "mango",
    "kiwifruit"
    ]

print(foods[0])
print(foods[2])
print(foods[-1])
print(foods[0:3])
print(foods[-3:])
print(foods[6][-1])