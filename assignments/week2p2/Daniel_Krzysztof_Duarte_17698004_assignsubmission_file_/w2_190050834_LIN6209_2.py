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
    return parameter*2

def all_ops_pt1(int1, int2):
    return int1 + int2, int1 - int2, int1 * int2, int1 / int2, int1 // int2, int1 % int2


def all_ops_pt2(int1, int2):
    return int1 < int2, int1 <= int2, int1 == int2, int1 != int2, int1 >= int2, int1 < int2


def magic_number(a_num):
    found=False
    a_num=str(a_num)
    if a_num.count('7') > 0:
        found=True
    return found



def hms_to_s(hours, minutes, seconds):
    return ((hours*3600)+(minutes*60)+seconds)


def s_to_hms(seconds):
    return seconds//3600, ((seconds//60)%60), seconds%60


def add_hms(hr1, min1, sec1, hr2, min2, sec2):
    totalSeconds=(((hr1*3600)+(min1*60)+sec1)+((hr2*3600)+(min2*60)+sec2))
    return totalSeconds//3600, (totalSeconds//60)%60, totalSeconds%60


def add_old_uk(pounds1, shillings1, pennies1, pounds2, shillings2, pennies2):
    totalPennies=(pounds1*240)+(shillings1*12)+(pennies1)+(pounds2*240)+(shillings2*12)+(pennies2)
    return totalPennies//240, (totalPennies//12)%20, totalPennies%12


def lucky_fun(outer_int):
    outer_int=str(outer_int)
    def magic_num(inner_num):
        found=False
        inner_num=str(inner_num)
        if inner_num.count(outer_int) > 0:
            found=True
        return found
    return magic_num

def rearranged(phrase1, phrase2):
    phrase1=phrase1.lower()
    phrase1=sorted(phrase1)
    phrase1=''.join(phrase1)
    phrase1=phrase1.strip(" !?'")
    phrase2=phrase2.lower()
    phrase2=sorted(phrase2)
    phrase2=''.join(phrase2)
    phrase2=phrase2.strip(" !?'")
    return phrase1==phrase2


def is_back_to_front(phrase):
    phrase=phrase.lower()
    phrase=phrase.split()
    phrase=''.join(phrase)
    revphrase=phrase[::-1]
    return phrase==revphrase
