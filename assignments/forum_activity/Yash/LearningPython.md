# Intro to the Python Programming
- The aim of this is to introduce to the python language
- our end goal is to give you enough python knowledge to be able to make a simple calculator in python

## Comments
- comments are pieces of code that don't get run.
- they can be used to add info about the code or whatever you want to have in them.

```python
# this is a comment

# this is a
# multiline comment
```

## Data types in python
### Strings (str)
anything in quotes is a string.
```python
"this is my string"
'this is another string'

"""this is a 
multiline string"""
```

### Numbers
#### Integers (int) - whole numbers

```python
1
2
400
5000000
1_000_000
```

#### Floating point numbers (float) - decimal numbers
```python
0.5
0.001
0.00001
```

### Boolean values - boolean values (bool)
```python
True
False
```

## The print() function

the **print()** function prints out whatever you put inside it to the console

this will print out "Im using a print function" to the console
```python
print("Im using a print function")

# output
"Im using a print function"
```
```python
print("   /|")
print("  / |")
print(" /  |")
print("/___|")

# output 
"   /|"
"  / |"
" /  |"
"/___|"
```


## Variables
### how to declare variables in python
variables hold data, they can be assigned to any piece of data.
they can hold primitive types like `strings`, `integers`, `floats`, `booleans`, and complex types like `lists` and `classes`
don't worry about the latter part just yet, you don't need to know about objects just yet.
```python
my_string_variable = "this is a my other variable"  # string - str

my_integer_variable = 5  # integer - int

pi = 3.14  # floating point number - float

is_it_day_outside = True  # boolean value - bool
```
#### *note*
in python variables names with multiple words in them should be seperated by underscores **"_"** as shown above.
a variable should NOT:
- contain spaces
- be a reserved keyword that has special uses in python like `while`, `for`, `in`,`is` and a few others
- however, you can use them along with other words like
```python
is_sunny_today = True
```

### Variable mutability
#### Python is a dynamically typed language
this means that we can assign and reassign a variable to anything we want.
we can declare a variable with a `string` then later reassign it to a `boolean` for example
```python
# the variables we assigned earlier
my_string_variable = "this is a my other variable"  # string - str
my_integer_variable = 5  # integer - int
pi = 3.14  # floating point number - float
is_it_day_outside = True  # boolean value - bool

# our changed variables 
my_string_variable = 50.6
my_integer_variable = "python is really cool!"
pi = False
is_it_day_outside = 9

# lets print them out
print(my_string_variable)
print(my_integer_variable)
print(pi)
print(is_it_day_outside)

# output
50.6
"python is really cool!"
False
9
```

#### Assigning variables to other variables
```python
my_string = "this is my string 1"
my_string_2 = "this is another string"

my_string = my_string_2
print(my_string)
print(my_string_2)

# output
"this is another string"
"this is another string"
```


## Some simple maths
### Basic maths operations
```python
2 + 2  # addition
2 - 2  # subtraction
2 * 2  # multiplication
2 / 2  # division
```

### Other maths operations
*(you don't need to worry about these for now)*
```python
# exponents (5^2)
5 ** 2 # result is 25
# modulus operator - gives the remainder of repeated division
7 % 2 # result is 1
# floor division - rounds down to the nearest whole number
5.7 // 3.6 # result is  1.0
5.7 / 3.6 # this would be 1.5833333333333333
```

## String concatenation
- concatenation is like adding but for strings
- you can use `+` operator to concatenate strings **and** to add numbers

the 2 strings below when printed will look exactly the same
```python
print("my name is Yash")
print("my name is " + "Yash") # joins the strings as they are so the space after 'is' is required
print("my name is", "Yash") # comma implicitly adds a space to the string

# output - all of them will print out 
"my name is Yash"
```
####
- you can use variables to substitute parts of a string
- this also prevents us having to repeat the same word over and over again
- this will also change the string as the variables change

```python
name = "Mike"
job = "teacher"
age = 29

phrase = "my name is " + name + " I am a " + job + " and I am " + str(age) + "years old."
print(phrase)

name = "James"
job = "student"
age = 20

print(phrase)

# output
"my name is Mike I am a teacher and I am 29 years old."
"my name is James I am a student and I am 20 years old."
```

# Q1 String and variables
- look at the text below
```python
"There was once a man named John"
"He was 30 years old"
"He Liked the name John"
"but he didn't like being 30"
```
- replace **'John'** with a variable
- replace **'30'** with a variable

#### solution at the end of the file

## Comparison operators pt.1
### Simple comparison operators
```python
4 < 5  # Less than
5 > 2  # Greater Than
5 <= 10  # Less than or Equal to
5 <= 5  # Less than or Equal to
50 >= 1  # Greater than or Equal to
50 >= 50  # Greater than or Equal to
5 == 5  # Equal to
5 != 90 # Not equal to
```
#### *note*
if you print these out they will result in either `true` or `false` the comparison operators are either true or false

this will print 'True' to the console as 2 + 3 is indeed equal to 5
```python
5 == 2 + 3

# output
True
```

**order of execution**
5 == 2 + 3
5 == 5
True

this will print 'False' to the console as 2 + 2 is not equal to 4
```python
5 == 2 + 2

# output
False
```

#### *note*
**=** means 'assign this value to a variable'
```python
variable_name = "some data"

# no output
```
**==** means 'tell me if this value is exactly equal to something else'

```python
# declare the variable
is_it_sunny_outside = False

# lets check if it's True
is_it_sunny_outside == True

# output 
False
```
**order of execution**
declare a variable is_it_sunny_outside to be False
check if is_it_sunny_outside is equal to True
is_it_sunny_outside == True
False == True
outputs False as False is not the same thing as True


```python
# variable we assigned earlier 
is_it_sunny_outside = False

# lets check if it's not true 
is_it_sunny_outside != True # Not equal to

# output
True
```
**order of execution**
declare a variable is_it_sunny_outside to be False
check if is_it_sunny_outside is NOT equal to True
is_it_sunny_outside == True
False != True
outputs True as False is indeed not the same thing as True

## Control flow pt.1
- python reads the code like humans do
- left to right and top to bottom
- this means that our code gets run line by line
- however, we can control what parts of the code gets run using control flow
- we can give python conditions for when the code should be run and when to skip over a line

#### *note*
python code uses indentation heavily for control flow (if, elif, else), loops (for, while), functions and many other things

### Look at the following code
```python
# delcare our varible 
is_sunny = True

if is_sunny == True:
	print("it's sunny :)")
else:
	print("it's not sunny :(")

# we could also say
if is_sunny != False:
	print("it's sunny :)")

# or just
if is_sunny:
	print("it's sunny :)")

# the above 3 will all output 
"it's sunny :)"

# they're 3 different ways of saying the same thing
```
the english equivalent would be "if it's sunny, say 'it's sunny', if it's not sunny, say 'it's not sunny'. "

## Comparison operators & control flow pt.2
### Like **==** you can also use the word **'is'**
Instead of:
```python
# delcare our varible 
is_sunny = True

if is_sunny == True:
	print("it's sunny :)")
	# code to execute if the condition met
```
You can just say:
```python
# delcare our varible 
is_sunny = True

if is_sunny is True:
	print("it's sunny :)")
	# code to execute if the condition met
```

### Like **!=** you can also use the word **'not'**
Instead of:
```python
# delcare our varible 
is_sunny = True

if is_sunny != False:
	print("it's sunny :)")
	# code to execute if the condition met
```
You can just say:
```python
# delcare our varible 
is_sunny = True

if not is_sunny:
	print("it's sunny :)")
	# code to execute if the condition met
```
Or
```python
# delcare our varible 
is_sunny = True

if is_sunny is not False:
	print("it's sunny :)")
	# code to execute if the condition met
```

- theres more than just `if` and `else`
- we also have`elif` which is a combination of `else` and `if`

take a look at the code below

```python
favourite_food = "pizza"

if favourite_food == "pasta":
	print("i love Pasta")
elif favourite_food == "fish":
	print("i love Fish")
elif favourite_food == "cake":
	print("i love Cake")
elif favourite_food == "pizza":
	print("i love Pizza")
elif favourite_food == "fish":
	pass
else:
	print("my favourite food isn't in your list!")

# output
"i love Pizza"
```
*as you saw earlier you can use `pass` to break out of your `if`, `elif` and `else` conditions*

#### *note*
- sometimes a variable can have no value
- we represent that using **`None`**
- if we print a value assigned to **`None`** to the console we will get **`None`** as the output
- in other programming languages this is often called `Void`, python uses `None`

```python
empty_variable = None

print(empty_variable)

# output
None
```
### *inportnat note*
- never compare to a variable with 'None' with the **`==`** operator, use the **`is`** keyword instead.

# Q2 Control flow
- make an age checker that tells you what you can do at each important age milestones
- so 16, 18, 21 etc...

#### solution at the end of the file

## Loops
### while loop
a loop runs a piece of code for a specified amount of cycles or while a condition is met

a `while loop` in particular runs a piece of code over and over again until the specified condition is no longer met
```python
counter = 0

while counter < 5:
	print("this is iteration", counter)
	counter = counter + 1  # increments the count by 1
	# and goes badk to the start of the loop

# output 
"this is iteration 0"
"this is iteration 1"
"this is iteration 2"
"this is iteration 3"
"this is iteration 4"
```
you can write the last line using **short hand**
```python
counter = 0

# long way
counter = counter + 1

# short way
counter += 1

# they both do the same thing, they increment the counter by 1
```

#### *note*
- the loop ended at 4 because we said **less than 5**, not **less than AND equal to 5**
- we started the counter at 0, so it did 5 iteration in total
- as the counter is incremented by 1 at the end of each cycle
- if we incremented the counter at the start we would have a loop that goes from 1 to 4
- if we DIDN'T increment the counter the loop would go on for ever as the counter would always be equal to =

#### *note*
- you can do **`while True`** and it will create an infinite loop
- unless and until you break out of it using the **`break`** keyword
- you can also use the **`continue`** keyword to force the loop to go back to the start

###
this code will stop running after 4 iterations because of the **`if`** condition and the **`break`** keyword
```python
counter = 1

while counter < 15:
	if counter == 2:
		# if we're in this code block counter is equal to 2
		print("going back to the start")
		counter += 1 # we need to increment the counter before we go back to the start 
		# if we don't the loop will continue for ever 
		continue
		# noting after the continue will get run
	elif counter == 4:
		# if we're in this code block counter is equal to 4
		print("i've done this 4 times now, time to stop")
		break
	# if we're in this code block, counter is not equal to 4 
	print("this is iteration", counter)
	counter += 1

# output
"this is iteration 1"
"going back to the start"
"this is iteration 3"
"i've done this 4 times, time to stop"
```

### for loop
```python
for number in range(5):
	print("this is iteration", number)

# output
"this is iteration 0"
"this is iteration 1"
"this is iteration 2"
"this is iteration 3"
"this is iteration 4"
```
#### **note**
- we didn't need to declare a counter variable by hand and increment it
- the loop increments the `number` variable itself.
- `range(5)` is a range from 0 to 4
- we can also say `range(2, 5)` which is a range from 2 to 4
- `range(1, 6)` would be a range from 1 to 5

*loops can do a lot more, such as iterating over `strings`, `lists`, `dictionaries` etc...
but we won't cover that right now*

# Q3 Loops
- make a loop that says hello 5 times
- but every time it has to say hello in a different way

#### solution at the end of the file

## Type Conversin
- as we discussed before, python is a dynamically typed language
- we can also convert between types by wrapping values that we want to convert into special functions
- (we will cover `functions` later on)
```python
fav_num = 3
print("my favourate number is " + fav_num + " it's a cool number.")

# output
"TypeError: can only concatenate str (not 'int') to str"
```

this means that we can't add numbers to strings, obiously not right?
python can add strings together as we discussed earlier, but you can't add strings to numbers

Unless...

- we can however solve this problem by converting our number to a string so python can concatenate the strings
- we do that by putting our **'pm_house_number'** in the **str()** function which converts any value we give it into a string

```python
fav_num = 3
print("my favourate number is " + str(fav_num) + " it's a cool number.")


# output
"my favourate number is 3 it's a cool number."
```
#### **note**
- we can also convert `strings` to `int` and `floats`
- ***but be careful***, unlike `int to string` or `float to string` conversion,
- if the `string` contains any non-numeric values it will result in an `ERROR`

```python
# this will work fine, converts "50" to 50
int("50")

# this will work fine, converts 50.0 to 50
int(50.0)

# this will work fine, converts 50.93 to 50
int(50.93)
# note that if you convert a float to an int 
# any information after the decimal point will be lost 

# this will result in an error
int("hi")
```
similarly
```python
# this will work fine - converts 50 to 50.0
float(50)

# this will also work fine - converts "50" to 50.0
float("50")

# this will result in an error
float("hi")
"ValueError: invalid literal for int() with base 10: 'hi'"
```

# Getting user input
this ones easy

you just type **input()** and it gets user input
- you can use a message to tell the user what to input
- you can store that in a variable for later use

#### *note*
- you get back a `string` so if you want to get an `int` or `float` back you'll need convert it using `int()` or `float()`

take a look at the code below

```python
name = input("What is your name: ")
print("your name is " + name)

# output 
'What is your name: '
# you can write whatever you want in the input
"What is your name: 'Yash'"

# it will then print 
"your name is Yash"
```

# functions
- functions are block of reusable code
- you write them once, and you can reuse them as many times as you want
- this avoids you writing the same code multiple times

take a look at the code below - this is a function
this is called a function declaration

```python
def function_name():
	print("some code")
	# some more code
```
#### **note**
notice how the body of the function is indented like a in control flow statements or loops

lets write a function that prints "cool function"
```python
def my_function():
	print("cool function")
```

to use the function you write the name of the function followed by open and closed parenthesis.

like this

```python
# declare the function
def my_function():
	print("cool function")

# call the function
my_function()

# ouput 
"cool function"
```

- functions can also take in values and return values
- for example, lets make a function that takes 2 numbers and gives us their sum

```python
def add(a, b):
	return a + b
```
- the **'return'** keyword gives us back a value
- this function doesn't print anything, it simply returns a value
- this means that you can assign the return value of the function to a variable for later use

like this

```python
def add(a, b):
	return a + b

sum_of_4_and_5 = add(4, 5)
print(sum_of_4_and_5)

# output
9
```

# Q4 Calculator
our calculator should:
- let the user chose 2 numbers and an operation they want to conduct
- you should let the user chose from addition, subtraction, multiplication and division
    - if you want you can add support for exponents, floor division and/or modulus
- you should also tell the user if their input is invalid

# All Solutions below

#
#
#
#
#

# make sure to try the problems yourself first

#
#
#
#
#

# Solutions

## Q1 Solution
```python
my_name = "[Your Name]"
my_age = 0

"There was once a man named " + my_name
"He was " + my_age + " 30 years old"
"He Liked the name " + my_name
"but he didn't like being " + my_age

# output
"There was once a man named [Your Name]"
"He was 0 years old"
"He Liked the name [Your Name]"
"but he didn't like being 0"
```

## Q2 Solution
```python
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
```

## Q3 Solution 1
```python
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

## Q3 Solution 2
```python
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
```

## Q4 Solution
```python
def add(x, y):
	return x + y

def subtract(x, y):
	return x - y

def multiply(x, y):
	return x * y

def divide(x, y):
	return x / y

def power(x, y):
	return x ** y

def int_divide(x, y):
	return x // y

def mod(x, y):
	return x % y


while True:
	num1 = float(input("Enter first number: "))
	num2 = float(input("Enter second number: "))
	print("chose between: +, -, *, /, **, //, %")
	operator = input("what operation do you want to conduct: ")


	if operator == '+':
		print(num1, "+", num2, "=", add(num1, num2))
		break
	elif operator == '-':
		print(num1, "-", num2, "=", subtract(num1, num2))
		break
	elif operator == '**':
		print(num1, "**", num2, "=", power(num1, num2))
		break
	elif operator == '*':
		print(num1, "*", num2, "=", multiply(num1, num2))
		break
	elif operator == '//':
		print(num1, "//", num2, "=", int_divide(num1, num2))
		break
	elif operator == '/':
		print(num1, "/", num2, "=", divide(num1, num2))
		break
	elif operator == '%':
		print(num1, "%", num2, "=", mod(num1, num2))
		break
	else:
		print("""
		############################
		# Invalid Input, Try again #
		############################
		""")
```
