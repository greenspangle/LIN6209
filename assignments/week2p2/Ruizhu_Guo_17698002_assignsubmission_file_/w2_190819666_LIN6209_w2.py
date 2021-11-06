"""" This is your LIN6209 Week 2 Assignment which is assessed

Each of the function specifications below contain a description of what the function is required to do.
Your assignment is to design, write and test functions that deliver these requirements.

All of the Python required to build these functions is covered in lessons 1 and 2: The operators +, -, *, /, //, %,
the built-in functions, the object methods associated with integer, floating point and string objects (int,
float and str methods), and a knowledge of functions and how to create them.

You do not need to submit any of your notes or tests. Just a working version of each of the requested functions.

VERY IMPORTANT
    -- DO NOT change the signatures of these functions
    --    That is: Do not change its name, the number of parameters, the number of values returned
    -- ALL of the functions must be in a single python file
    -- The name of the python script you submit MUST BE
            xxxxxxxxx_LIN6209_1.py (where x..x is your student number)

You can write as many 'helper functions' as you want and call them anything you want.
You can delete as much of my text instructions as you want.
BUT
your assignment submission MUST contain these functions with these signatures in a single file."""


def magic7():
    """This function answers the integer 7 every time it is called"""
    return 7


def times2(parameter):
    """ This function takes any number or string and returns twice the value."""
    the_result = parameter + parameter
    return the_result

def all_ops_pt1(int1, int2):
    """ This function takes any two integers and returns the tuple"""
    the_result = int1+int2, int1-int2, int1*int2, int1/int2, int1//int2, int1%int2
    return the_result

def all_ops_pt2(int1, int2):
    """ Same as all_ops_pt1 but this time with the operators <, <=, ==, !=, >=, and > """
    the_result = int1<int2, int1<=int2, int1==int2, int1!=int2, int1>=int2, int1>int2
    return the_result

def magic_number(a_num):
    """ If the parameter a_num is a magic number answer boolean True. If not answer boolean False.A magic number is any number that contains the digit 7."""
    s=str(a_num)
    if s.count('7')>=1:
        return bool(1)
    elif s.count('7')<=1:
        return bool(0)

def hms_to_s(hours, minutes, seconds):
    """Convert a duration of hours:minutes:seconds to seconds."""
    the_result = hours*3600+minutes*60+seconds
    return the_result


def s_to_hms(seconds):
    """Convert a duration in seconds to hours:minutes:seconds in standard form"""
    the_result = seconds//3600,seconds%3600//60,seconds%60
    return the_result


def add_hms(hr1, min1, sec1, hr2, min2, sec2):
    """Add two hour:minute:seconds time durations and answer the sum in standard form."""
    sum = hms_to_s(hr1+hr2, min1+min2, sec1+sec2) 
    the_result = s_to_hms(sum)
    return the_result


def add_old_uk(pounds1, shillings1, pennies1, pounds2, shillings2, pennies2):
    """Add two pre-decimalisation amounts of UK currency and return the result in standard form with
    pennies<12 and shillings<20."""
    sum = (pounds1 + pounds2)*20*12 + (shillings1 + shillings2)*12 + pennies1 + pennies2
    the_result = sum//240, sum%240//12, sum%12
    return the_result


def lucky_fun(an_int):
    """lucky number"""
    def innerfunction(num):
        s1=str(num)
        s=s1.replace('.','')
        if s.count(str(an_int))>=1:
            return bool(1)
        elif s.count(str(an_int))<1:
            return bool(0)
    return innerfunction 


def rearranged(phrase1, phrase2):
    """Answer True if parameters contain exactly the same letters, possibly arranged differently. False otherwise."""
    a1=phrase1.replace(' ','')
    a2=phrase2.replace(' ','')
    b1=a1.lower()
    b2=a2.lower()
    if sorted(b1)==sorted(b2):
        return bool(1)
    elif sorted(b1)!=sorted(b2):
        return bool(0)


def is_back_to_front(phrase):
    """ If parameter is a string that reads the same backwards as forwards return True, else False."""
    a=phrase.lower()
    b=a.replace(' ','')
    if list(b)==list(reversed(b)):
        return bool(1)
    elif list(b)!=list(reversed(b)):
        return bool(0)
    
