email_address = input("Please enter your email address")

symbol_1 = "@"
symbol_2 = "."

if symbol_1 in email_address and symbol_2 in email_address:
    print("Email valid")
else:
    print("Email invalid")