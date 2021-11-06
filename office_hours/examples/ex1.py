"""" This is your LIN6209 Week 2 Assignment which is assessed"""


def magic7():
    """This function answers the integer 7 every time it is called"""
    return 7


def times2(a_value):
    """ This function takes any number or string and returns twice the value."""
    the_result = a_value + a_value
    return the_result


def all_ops_pt1(int1, int2):
    """ This function takes any two integers and returns the tuple
            ( int1 + int2, int1 - int2, int1 * int2, int1 / int2, int1 // int2, int1 % int2,)"""
    the_result = int1 + int2, int1 - int2, int1 * int2, int1 / int2, int1 // int2, int1 % int2
    return  the_result


def all_ops_pt2(int1, int2):
    """ Same as all_ops_pt1 but this time with the operators <, <=, ==, !=, >=, and < """
    the_result = int1 < int2, int1 <= int2, int1 == int2, int1 != int2, int1 >= int2, int1 > int2
    return  the_result


##def magic_number(a_num):
##""" If the parameter a_num is a magic number answer boolean True.
##If not answer boolean False. A magic number is any number that contains the digit 7. The parameter is guaranteed to be type int or float."""    
##    any_number = set(str(a_num))
##    magic_number = "7"
##    if magic_number in any_number:
##        return print ("True")
##    else:
##        return print ("false")


def hms_to_s(hours, minutes, seconds):
    """Convert a duration of hours:minutes:seconds to seconds."""
    s= (hours*3600) + (minutes*60) + seconds
    return  s


def s_to_hms(seconds):
    """Convert a duration in seconds to hours:minutes:seconds in standard form."""
    hours = seconds // 3600
    seconds %= 3600
    minutes = seconds // 60
    ss = seconds % 60
    return(hours, minutes, ss)


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

    hours = seconds // 3600
    seconds %= 3600
    minutes = seconds // 60
    ss = seconds % 60
    return (hours, minutes, ss)


def add_old_uk(pounds1, shillings1, pennies1, pounds2, shillings2, pennies2):
    """Add two pre-decimalisation amounts of UK currency and return the result in standard form with
    pennies<12 and shillings<20."""
    shillings_to_pounds = (shillings1+shillings2)//20
    pounds = (pounds1+pounds2) + shillings_to_pounds
    pennies_to_shillings = (pennies1 + pennies2)//12
    shillings = ((shillings1+shillings2)%20) + pennies_to_shillings
    pence = (pennies1 + pennies2)%12
    return  pounds, shillings, pence


##def lucky_fun(an_int):
##     """ This function accepts an integer parameter (outer_int) and returns a function.
##    The returned function accepts an int or float parameter (inner_num) and answers boolean True if the
##    sequence of digits in outer_int occurs within inner_num, False otherwise. """
##    def lucky_fun(an_int):
##        lucky_fun = set(str(an_int))
##        def unlucky_fun(inner_num):
##            unlucky_fun = set(str(inner_num))
##            if str(an_int) in str(inner_num):
##                print ("True")
##            else:
##                print ("False")
##        return (unlucky_fun)


def rearranged(phrase1, phrase2):
    """Answer True if parameters contain exactly the same letters, possibly arranged differently. False otherwise."""
    def rearranged(phrase1, phrase2):
        if sorted(phrase1)==sorted(phrase2):
                return print("True")
        else:
                return print("False")


def is_back_to_front(phrase):
    """ If parameter is a string that reads the same backwards as forwards return True, else False."""
    if phrase [:]==phrase[::-1]:
        return print ("True")
    else:
        return print ("False")
