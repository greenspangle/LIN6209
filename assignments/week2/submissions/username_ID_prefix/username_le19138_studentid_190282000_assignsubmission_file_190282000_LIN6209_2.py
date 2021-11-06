"""" This is your LIN6209 Week 2 Assignment which is assessed

IMPORTANT
    -- DO NOT change the signatures of these functions
    --    That is: Do not change its name, the number of parameters, or the number of values returned
    -- ALL of the functions must be in a single python file
    -- The name of the python script you submit MUST BE
            xxxxxxxxx_LIN6209_2.py (where x..x is your student number)

Your assignment is to design, write, test, and deliver functions that satisfy the requirements specified below.

You do not need to submit any of your notes or tests. Just a working version of each of the requested functions.

All of the Python required to build these functions is covered in lessons 1 and 2: The operators +, -, *, /, //, %,
<, <=, ==, !=, >=, >, the built-in functions, the object methods associated with integer, floating point and string
objects, and a knowledge of how to use and create functions.

You can write as many 'helper functions' as you want and call them anything you want.
You can delete as much of my text instructions as you want."""


def magic7():
    """This function answers the integer 7 every time it is called"""
    return 7


def times2(a_value):
    """ return twice a_value: """
    the_result = a_value + a_value
    return the_result


def all_ops_pt1(int1, int2):
    
    the_result = int1 + int2, int1 - int2, int1 * int2, int1 / int2, int1 // int2, int1 % int2
    return  the_result

def all_ops_pt2(int1, int2):
    """ Same as all_ops_pt1 but this time with the operators <, <=, ==, !=, >=, and < """
    the_result = int1 < int2, int1 <= int2, int1 == int2, int1 != int2, int1 >= int2, int1 < int2
    return the_result


def magic_number(a_num):
    if '7' in str(a_num):
        return True
    else:
        return False


def hms_to_s(hours, minutes, seconds):
    """Convert a duration of hours:minutes:seconds to seconds.

    Parameters are guaranteed to be positive integers.
    The return value is always an integer.
    For example:
        hms_to_s(0,0,0) returns 0
        hms_to_s(0,0,1) returns 1
        hms_to_s(0,2,0) returns 120
        hms_to_s(3,0,0) returns 10800
        hms_to_s(3,2,1) returns 10921 """
    
    s = (hours*3600) + (minutes*60) + seconds
    return print (s)



def s_to_hms(seconds):
    """Convert a duration in seconds to hours:minutes:seconds in standard form.
    Standard form means hours, minutes, seconds are all integers, and minutes and seconds are both < 60
    Parameter is guaranteed to be positive integer.

    For example:
        s_to_hms(0) returns 0,0,0
        s_to_hms(61) returns 0,1,1
        s_to_hms(10921) returns 3,2,1"""

    h = seconds//3600
    m = (seconds % 3600) // 60
    s = ((seconds % 3600) % 60)
    return  print (h, m, s)


def add_hms(hr1, min1, sec1, hr2, min2, sec2):
    """Add two hour:minute:seconds time durations and answer the sum in standard form.
    Standard form means the minutes and seconds are both < 60
    Parameters are all guaranteed to be positive integers

    For example:
        add_hms(0, 0, 50, 0, 0, 40) returns (0, 1, 30)
        add_hms(25, 50, 50, 145, 40, 20) returns (171, 31, 10) """

    hours = hr1 + hr2 
    minutes = min1 + min2
    seconds = sec1 + sec2
    s = (hours*3600) + (minutes*60) + seconds

    h = s//3600
    m = (s % 3600) // 60
    s = ((s % 3600) % 60)
    
    return print (h, m, s)


def add_old_uk(pounds1, shillings1, pennies1, pounds2, shillings2, pennies2):
    """Add two pre-decimalisation amounts of UK currency and return the result in standard form with
    pennies<12 and shillings<20. """
    
    pounds = (pounds1 + pounds2) + ((shillings1 + shillings2) // 20)
    shillings = ((pennies1 + pennies2)//12) + ((shillings1+shillings2)%20)
    pennies = ((pennies1 + pennies2)%12)
    return  pounds, shillings, pennies


def lucky_fun(an_int):
    """ This function accepts an integer parameter (outer_int) and returns a function.
    The returned function accepts an int or float parameter (inner_num) and answers boolean True if the
    sequence of digits in outer_int occurs within inner_num, False otherwise.
    For example:
        a = lucky_fun(7) # returns a function and assigns it to a
        a(11711)  # returns True
        a(11511)  # returns False
        a(0)  # returns False

        b = lucky_fun(11) then
        b(11511)  # returns True
        b(15151)  # returns False
        b(1.102)  # returns True
        b(1010)   # returns False """
    lucky_fun = str(an_int)
    def newfun(inner_num):
        if str(an_int) in str(inner_num):
            print ("True")
        else:
            print ("False")
    return (newfun) 


def rearranged(phrase1, phrase2):
    """Answer True if parameters contain exactly the same letters, possibly arranged differently. False otherwise.

    Parameters phrase1 and phrase2 are guaranteed to be type str and only contain the  [A-Z][a-z] and space.
    Spaces and capitalization are ignored during comparison.

    Examples:
        rearranged('Debit card', 'Bad credit')  # returns True
        rearranged('Sugared ambulances', 'Cumberland Sausage')  # returns True
        rearranged('A legal title', 'Tagliatelle')  # returns True
        rearranged('this phrase', 'that phrase')  # returns False

    Hints:
        1. Everything you need is either a built-in function or a string method
        2. Make both parameters lower-case and remove spaces before comparing"""

    if sorted(phrase1) == sorted (phrase2):
        return True
    else:
        return False


def is_back_to_front(phrase):
    """ If parameter is a string that reads the same backwards as forwards return True, else False. """
    
    if phrase[:] == phrase [::-1]:
        return True
    else:
        return False
