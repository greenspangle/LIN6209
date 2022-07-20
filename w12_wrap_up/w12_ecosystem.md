# The Python and IT ecosystem

## f strings

Introduced in Python 3.6 fstrings are a convenient (and efficient) way of formatting strings.
See https://docs.python.org/3/reference/lexical_analysis.html#index-25 for details.

Suppose your program uses an integer variable `age` which has a current value of 27, and you want to create
the string `'You are 27 years of age'`.

```python
age = 27
#  Rather that having to write something like
str_1 = 'You are ' + str(age) + ' years of age'
# or
str_2 = 'You are {0} years of age'.format(age)
# using an f string it's just
str_3 = f'You are {age} years of age'
# you can even do calculations within the f string
str_4 = f'You have been able to vote for {age - 18} years'
```

Try a few examples yourself:

```python
# A room measures in meters 
width, breadth = 3, 5
# using an fstring, create a nice string stating its area and dimensions
message_1 = f'?'
#
# I work 15 hours at £12 per hour less £11 national insurance and tax at 20% 
message_2 = f'?'
#
# and try a couple of your own examples
```

## Documenting your programs

Ever tried using someone else's software without any instructions or help? Not easy. Now imagine trying to
amend someone else's code without any documentation or information about how the code works, or what it
does, or even is supposed to be doing. Even less easy.

Documentation is important because **most developers spend most of their time fixing and enhancing other
peoples code**.

Code is difficult enough to read and understand at the best of times. Trying to find bugs in software of
anything more than trivial complexity is a serious intellectual exercise. If the code is unfamiliar and
poorly documented that can rapidly become a mind twisting experience. Fixing undocumented or, perhaps worse,
incorrectly documented code is in another league beyond that. It's often quicker to throw it away and write
it again from scratch rather than attempt to fix an impenetrable jungle of code.

At a minimum your code should be documented with:

* meaningful object names
* informative in-line comments
* docstrings

### Object Names

The name of an object should give the reader a good clue about what type of object it is and what data it
will contain or function it will perform.

```python
x, y, z = 0, 0, 0  # meaningless names = bad
height, width, depth = 0, 0, 0  # informative names = good
```

### In-line comments

Say what the code is doing. Don't say the trivially obvious, you are after all talking to another
programmer.

```python
cost, profit, tax = 17, 8, 5
price = cost + profit + tax  # add cost and profit and tax and assign to price = pointless verbiage!

matrix_1 = [[1, 2, 3], [4, 5, 6], [7, 8.9]]
# matrix_1 is a list of lists. A list of the rows of the matrix and each row is a list of the elements
flat = [element for row in matrix_1 for element in row]  # flatten the matrix into a single list
```

### Docstrings

Your functions should contain an explanation of what they do within themselves.

```python
def pointless():
    """ This function takes no parameter and does nothing.
    
    This is the 'docstring' that provided users of this function helpful information.
    It is ALWAYS good practice to include one.
    blah blah blah dee dah
    """
    return


# execute the above in IDLE and then run
help(pointless)
# Voila! Your functions are now integrated into the Python help system :-) 
```

You should also develop the habit of placing a docstring as the first item of code in your modules, classes
and class methods - for exactly the same reasons. For example, run the following few lines of code in IDLE:

```python
import fractions

help(fractions)

# and perhaps
import string

help(string)
```

## Try - Except

For when things go wrong.

When Python encounters a problem it cannot fix it ‘raises an exception’. This cascades an exception object
upwards through the code stack. If this exception object is not ‘caught’ and dealt with before it gets to
the top of the call stack then the program crashes.

Possible reasons an exception may occur: user enters 'wrog' sort of data, attempt to divide by zero, attempt
to read a file that does not exist, and so on.

```python
# The simple but fragile version
def get_float_v1():
    a_float = float(input('input a number'))
    return a_float


# the robust version
def get_float_v2():
    input_ok = False  # keep asking the user for input until this is True
    while not input_ok:
        try:
            a_float = float(input('input a number'))
            input_ok = True
        except ValueError as err:
            # 'user entered a string that cannot be converted to a float':
            print("That was not a valid number. Try again...")
    return a_float
```

Another example with a potential divide by zero error

```python
def reciprocal(a_num):
    """Answer the reciprocal of the parameter a_num.
    
    If the parameter is zero then return zero. 
    """
    try:
        inverse = 1 / a_num
    except ZeroDivisionError as z_err:
        print(f'Caught the exception {z_err} and will now deal with it')
        # Normally reciprocal of zero is undefined
        # This function will return zero
        inverse = 0
    return inverse
```

Your application does not have to deal with the exception as soon as it is raised, as long as the exception
is caught somewhere, your application will be robust.

## Classes

Defining your own datatypes

Numbers, lists, sets, strings are different datatypes. Each of them has many methods particular to
themselves. The operator ‘+’ behaves differently for numbers and strings. They are Classes. Create your own
classes with the ‘class’ statement.

```python
# A door class
class Door():
    def __init__(self, color='TBA', height='TBA'):
        self.__color = color
        self.__height = height

    def set_color(self, color):
        self.__color = color

    def set_height(self, height):
        self.__height = height

    def __str__(self):
        return f'This door is a {self.__color} door and is {self.__height} high'


# and create a few doors
red_door = Door('red', 2)
blue_door = Door('blue', 2.2)
print(red_door, '\n', blue_door)
# make the red door scarlet
red_door.set_color('Scarlet')
# and check it has changed
print(red_door, '\n', blue_door)
```

## Testing & Debugging

```python
def seven(anything):
    return 7


assert seven(7) == 7
assert seven(17) == 7
assert seven(717) == 8
assert seven(1) == 7
```

## SQL

Try the examples at [sqlzoo.net](https://sqlzoo.net/wiki/SQL_Tutorial)
and [W3schools](https://www.w3schools.com/sql/default.asp)

## Version Control

Git and GitHub are my preferences, there are others
