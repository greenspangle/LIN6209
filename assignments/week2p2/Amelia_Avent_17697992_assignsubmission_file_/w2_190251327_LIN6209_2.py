"""" PMcG comments
Python script contained syntax errors within 2 functions (lucky_fun and is_back_to_front) which I have commented out

 """


def magic7():
    """This function answers the integer 7 every time it is called"""
    return 7
    
def times2(parameter):
    """return twice parameter"""
    the_result = parameter + parameter
    return the_result


def all_ops_pt1(int1, int2):
    """ This function takes any integers and returns the tuple """
    the_result = int1 + int2, int1 - int2, int1 * int2, int1 / int2, int1 // int2, int1 % int2
    return the_result


def all_ops_pt2(int1, int2):
    """ Same as all_ops_pt1 but this time with the operators <, <=, ==, !=, >=, and > """
    the_result = int1 < int2, int1 <= int2, int1 == int2, int1 != int2, int1 >= int2, int1 > int2
    return the_result


def magic_number(a_num):
    """ If the parameter a_num is a magic number answer boolean True. If not answer boolean False.

    A magic number is any number that contains the digit 7.
    The parameter is guaranteed to be type int or float. """
    the_result = '7' in str(a_num)
    return the_result


def hms_to_s(hours, minutes, seconds):
    """Convert a duration of hours:minutes:seconds to seconds.
    Parameters are guaranteed to be positive integers.
    The return value is always an integer."""
    h, m, s = (hours, minutes, seconds)
    the_result = int(h * 3600) + int(m * 60) + int(s)
    return the_result


def s_to_hms(seconds):
    """Convert a duration in seconds to hours:minutes:seconds in standard form.
    Standard form means hours, minutes, seconds are all integers, and minutes and seconds are both < 60
    Parameter is guaranteed to be positive integer. """

    h = str(seconds//3600)
    m = str((seconds%3600)//60)
    s = str((seconds%3600)%60)
    the_result = ["{},{},{}".format(h,m,s)]
    return the_result


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
    if (seconds >= 60):
        minutes += seconds // 60
        seconds = seconds%60
    if (minutes >= 60):
        hours += minutes // 60
        minutes = minutes%60
    return (hours, minutes, seconds)


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
    pounds = pounds1 + pounds2
    shillings = shillings1 + shillings2
    pennies = pennies1 + pennies2
    if (pennies >=12):
        shillings += pennies // 12
        pennies = pennies%12
    if (shillings >= 20):
        pounds += shillings //20
        shillings = shillings%20
    return (pounds, shillings, pennies)


def lucky_fun(an_int):
    inner_num = int

    print (inner_num)
#
# def lucky_number(inner_num):
#         if len(an_int) == len(set(inner_num)):
#             return (True)
#         else:
#             return (False)

""" This function accepts an integer parameter (outer_int) and returns a function.
    The returned function accepts an int or float parameter (inner_num) and answers boolean True if the
    sequence of digits in outer_int occurs within inner_num, False otherwise. """


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
    phrase1 = phrase1.lower().replace(" ", "")
    phrase2 = phrase2.lower().replace(" ", "")

    return sorted(phrase1) == sorted(phrase2)


# def is_back_to_front(phrase):
#     """ If parameter is a string that reads the same backwards as forwards return True, else False.
#
#     Parameter phrase is guaranteed to be a string (str) and only contain the characters [A-Z][a-z] and space.
#     Spaces and capitalisation are ignored during comparison.
#
#     Examples:
#         is_back_to_front('Kayak') returns True
#         is_back_to_front('Akasaka') returns True  # a town in Japan
#         is_back_to_front('never odd or even') returns True
#         is_back_to_front('backwards') returns False
#
#     Hints:
#         1. Everything you need is either a built-in function or a string method
#         2. Make phrase all lower-case (or upper case) and remove spaces before comparing"""
#
#     phrase = phrase.lower().replace(" ", "")
#     return  phrase = phrase (
#
