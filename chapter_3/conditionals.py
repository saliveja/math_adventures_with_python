# conditionals - if, elif, else
y = 6

if y > 7:
    print("yes!")
else:
    print("no!")

age = 50
if age < 10:
    print("What school do you go to?")
elif 11 < age < 20:
    # if age is between 11 and 20
    print("You're cool!")
elif 20 <= age < 30:
    print("What job do you have?")
elif 30 <= age < 40:
    print("Are you married?")
else:
    print("Wow, you're old!")