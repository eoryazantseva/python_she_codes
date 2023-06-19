lyrics = [    
    ["Monica", "in my life"],    
    ["Erica", "by my side"],    
    ["Rita's", "all I need"],    
    ["Tina's", "what I see"],    
    ["Sandra", "in the sun"],    
    ["Mary", "having fun"],    
    ["Jessica", "here I am"]
    ]

for i in lyrics:
    name = i[0]
    text = i[1]
    song = "A little bit of " + name + " " + text + ";"
    print(song)
print(f"A little bit of you makes me your man (ah!)")
print(f"*trumpet solo*")

# for i in lyrics:
#     name, text = i #unpacking the list
#     song = "A little bit of " + name + " " + text + ";"
#     print(song)