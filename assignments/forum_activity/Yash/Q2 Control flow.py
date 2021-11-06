# Practice Question 2
# make an age checker that tells you what you can do at each important age milestones
 #so 16, 18, 21 etc...

# Solution
age = 16

if age >= 21:
    print("you can do anything you like")
elif 21 > age >= 18:
    print("you're legally an adult in the UK")
elif 18 > age >= 16:
    print("you can get driving lessons")
else:
    print("sorry you're too young")

# output
"you can get driving lessons"