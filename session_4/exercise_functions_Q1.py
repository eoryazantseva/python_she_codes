prompt = "Could I please have an integer?"

def get_integer():
    result = input(prompt)
    return int(result)                                                                                                                                              

user_input = get_integer()
print(f"So your integer is {user_input}? Thanks!")