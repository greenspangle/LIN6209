# Practice Question 3
# make a loop that says hello 5 times
# but every time it has to say hello in a different way

# Solution 1
counter = 1

while counter <= 5:
    if counter == 1:
        print("hi")
    elif counter == 2:
        print("hello")
    elif counter == 3:
        print("yo")
    elif counter == 4:
        print("wassup")
    elif counter == 5:
        print("saaaa dude")

    counter += 1
```

# Solution 1
for number in range(1,6):
    if number == 1:
        print("hi")
    elif number == 2:
        print("hello")
    elif number == 3:
        print("yo")
    elif number == 4:
        print("wassup")
    elif number == 5:
        print("saaaa dude")