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
    return 7 

def times2(parameter):
    the_result = parameter + parameter
    return the_result


def all_ops_pt1(int1, int2):
    var_1 = int1 + int2
    var_2 = int1 - int2
    var_3 = int1 * int2
    var_4 = int1 / int2
    var_5 = int1 // int2
    var_6 = int1 % int2
    return var_1,var_2, var_3, var_4, var_5, var_6


def all_ops_pt2(int1, int2):
    var_1 = int1 < int2
    var_2 = int1 <= int2
    var_3 = int1 == int2
    var_4 = int1 != int2
    var_5 = int1 >=int2
    var_6 = int1 > int2
    return var_1,var_2, var_3, var_4, var_5, var_6


def magic_number(a_num):
    s = str(a_num)
    if s. count ('7') >=1:
            return bool (1)
    if s. count ('7') <1:
            return bool (0)
    return bool (1) or bool (0)


def hms_to_s(hours, minutes, seconds):
    return (hours * 3600 + minutes * 60 + seconds)


def s_to_hms(seconds):
    hours = (seconds // 3600)
    minutes = (seconds % 3600 // 60)
    seconds = (seconds%60)
    the_result = (hours, minutes, seconds)
    return  the_result


def add_hms(hr1, min1, sec1, hr2, min2, sec2):
    sum = hr1*3600 + min1* 60 + sec1 + hr2*3600 + min2*60+ sec2
    the_result = sum//3600, sum%3600//60, sum%60
    return the_result


def add_old_uk(pounds1, shillings1, pennies1, pounds2, shillings2, pennies2):
    sum = pounds1*240 + shillings1* 12 + pennies1 + pounds2*240 + shillings2*12+ pennies2
    the_result = sum//240, sum%240//12, sum%12
    return the_result


def lucky_fun(an_int):
    def innerfuction (num):
        s = str(num)
        s. replace ('.','')
        if s.count (str(an_int)) >=1:
                return bool (1)
        elif s.count (str(an_int)) <1:
                return bool (0)
    return innerfuction


def rearranged(phrase1, phrase2):
    a= phrase1
    b= phrase2
    a1= a. lower()
    b1= b. lower()
    a2= a1. replace (' ','')
    b2= b1.replace (' ','')
    s1= sorted (list(str(a2)))
    s2= sorted (list(str(b2)))
    if s1==s2:
        return bool (1)
    elif s1!=s2:
        return bool (0)


def is_back_to_front(phrase):
    a = phrase
    a1 = a.lower()
    a2= a1.replace (' ','')
    b = reversed(a2)
    if list (a2) == list (b):
        return bool (1)
    elif list (a2) != list (b):
        return bool (0) 
