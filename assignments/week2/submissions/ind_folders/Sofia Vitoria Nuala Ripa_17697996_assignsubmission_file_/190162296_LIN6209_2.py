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
    # your code goes here


def magic7():
    """Always return the integer 7"""
    return 7




def times2(parameter): 
    """ This function takes any number or string and returns twice the value.
    The parameter is guaranteed to be either an integer, a float or a string.
    For example:
        times2(7) returns 14
        times2('x') returns 'xx'
        times2(a) returns = depends on the value of the variable a """
    # your code goes here



def times2(a_value):
    """Return twice a_value:"""
    the_result = a_value + a_value
    return the_result





def all_ops_pt1(int1, int2): 
    """ This function takes any two integers and returns the tuple
            ( int1 + int2, int1 - int2, int1 * int2, int1 / int2, int1 // int2, int1 % int2,)
    For example:
        all_ops(4, 2) returns 6, 2, 8, 2.0, 2, 0
        all_ops(5, 4) returns 9, 1, 20, 1.25, 1, 1
        all_ops(9, 3) returns 12, 6, 27, 3.0, 3, 0 """
    # your code goes here
    return  # your, return, values


def all_ops_pt1(int1, int2):
    """Always return the tuple of int1, int2"""
    the_result =  int1 + int2, int1 - int2, int1 * int2, int1 / int2, int1 // int2, int1 % int2,
    return the_result








def all_ops_pt2(int1, int2):
    """ Same as all_ops_pt1 but this time with the operators <, <=, ==, !=, >=, and < """
    return  # your, return, values



def all_ops_pt2(int1, int2):
    """Always return the tuple of int1, int2"""
    the_result =  int1 < int2, int1 <= int2, int1 == int2, int1 != int2, int1 >= int2, int1 > int2,
    return the_result



def magic_number(a_num):
    """ If the parameter a_num is a magic number answer boolean True. If not answer boolean False.

    A magic number is any number that contains the digit 7.
    The parameter is guaranteed to be type int or float.
    For example:
        magic_num(7) returns True
        magic_num(11171171) returns True
        magic_num(-7) returns True
        magic_num(0.123456789) returns True
        magic_num(0) returns False
        magic_num(0123.456) returns False """
    # your code goes here
    return  # either boolean True or Boolean False

def magic_number(a_num):
    if '7' in str(a_num):
        print('{} True'.format(a_num))
    else:
        print("False")




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
    # your code goes here
    return  # the integer number of seconds



def hms_to_s(hours, minutes, seconds):
    """Get Seconds from time."""
    h, m, s = hours, minutes, seconds
    return int(h) * 3600 + int(m) * 60 + int(s)





def s_to_hms(seconds): 
    """Convert a duration in seconds to hours:minutes:seconds in standard form.
    Standard form means hours, minutes, seconds are all integers, and minutes and seconds are both < 60
    Parameter is guaranteed to be positive integer.

    For example:
        s_to_hms(0) returns 0,0,0
        s_to_hms(61) returns 0,1,1
        s_to_hms(10921) returns 3,2,1"""
    # your code goes here
    return  # the tuple (hours, minutes, seconds)


def s_to_hms(seconds):
     
 """Get time from seconds"""
 seconds = seconds % (24 * 3600)
 hour = seconds // 3600
 seconds %= 3600
 minutes = seconds // 60
 seconds %= 60
      
 return "%d,%02d,%02d" % (hour, minutes, seconds)
      







def add_hms(hr1, min1, sec1, hr2, min2, sec2):
    """Add two hour:minute:seconds time durations and answer the sum in standard form.
    Standard form means the minutes and seconds are both < 60
    Parameters are all guaranteed to be positive integers

    For example:
        add_hms(0, 0, 50, 0, 0, 40) returns (0, 1, 30)
        add_hms(25, 50, 50, 145, 40, 20) returns (171, 31, 10) """
    # your code goes here
    return  # the tuple (hours, minutes, seconds)


def add_hms(hr1, min1, sec1, hr2, min2, sec2):
    """Add two hour:minute:seconds time"""

    hours =hr1 + hr2
    minutes = min1 + min2
    seconds = sec1 + sec2
    s= (hours*3600) + (minutes*60) + seconds

    h= s//3600
    m= (s % 3600) // 60
    s= ((s % 3600) % 60)

    return print (h, m, s)




def add_old_uk(pounds1, shillings1, pennies1, pounds2, shillings2, pennies2):
    """Add two pre-decimalisation amounts of UK currency and return the result in standard form with
    pennies<12 and shillings<20.
    Prior to decimalisation-day (15 February 1971) UK currency consisted of pounds, shillings and pence.
    Twelve pence made one shilling and twenty shillings made one pound. Prices were displayed as £5/10s/6d
    (pronounced as "five pounds ten shillings and sixpence" https://en.wikipedia.org/wiki/%C2%A3sd)
    Parameters are all guaranteed to be positive integers

    For example:
        add_old_uk(0, 0, 11, 0, 0, 7) returns 0, 1, 6
        add_old_uk(0, 19, 11, 1, 10, 6) returns 2, 10, 5

    Hint - break the problem into parts and solve it one step at a time """
    # your code goes here
    return  # the tuple (pounds, shillings, pence)


def add_old_uk(pounds1, shillings1, pennies1, pounds2, shillings2, pennies2):

    pounds = (pounds1 + pounds2) + ((shillings1 + shillings2) // 20)
    shillings = ((pennies1 + pennies2) // 12) + ((shillings1 + shillings2) % 20)
    pennies = ((pennies1 + pennies2) % 12)

    return pounds, shillings, pennies



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
    # your code goes here
    return  # a function

def lucky_fun(an_int):
    def other_fun(inner_num):
        if '7' in str(inner_num):
            print('{} True'.format(inner_num))
        else:
            print("False")
        return str(an_int) in str(inner_num).replace(",","")
    return (other_fun)


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

    # your code goes here
    return  # either boolean True or Boolean False



def rearranged(phrase1, phrase2):
    if sorted(phrase1) == sorted(phrase2):
        print("True")
    else:
        print("False") 



def is_back_to_front(phrase): 
    """ If parameter is a string that reads the same backwards as forwards return True, else False.

    Parameter phrase is guaranteed to be a string (str) and only contain the characters [A-Z][a-z] and space.
    Spaces and capitalisation are ignored during comparison.

    Examples:
        is_back_to_front('Kayak') returns True
        is_back_to_front('Akasaka') returns True  # a town in Japan
        is_back_to_front('never odd or even') returns True
        is_back_to_front('backwards') returns False

    Hints:
        1. Everything you need is either a built-in function or a string method
        2. Make phrase all lower-case (or upper case) and remove spaces before comparing"""

    # your code goes here
    return  # either boolean True or boolean False


def is_back_to_front(string):
    revString = string[::-1]
    if string == revString:
        print('True')
    else:
        print('False')

