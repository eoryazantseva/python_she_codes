question_1 = input ("Does Sarah have a helmet?")
sarah_has_helmet = False
if question_1 == "yes":
    sarah_has_helmet = True
    

question_2 = input ("Does Rei have a rope?")
rei_has_rope = False
if question_2 == "yes":
    rei_has_rope = True

if (sarah_has_helmet and rei_has_rope):
    print("Let's send it")
elif (sarah_has_helmet and not rei_has_rope):
    print("Who's unprepared now, Rei?")
elif (not sarah_has_helmet and rei_has_rope):
    print("No way, my brain is my moneymaker!")
else:
    print("I guess, let's just go hiking?")

