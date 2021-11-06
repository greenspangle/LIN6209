
def magic7():
    """This function answers the integer 7 every time it is called"""
    return 7


def times2(parameter):
    """ This function takes any number or string and returns twice the value."""   
    return parameter*2


def all_ops_pt1(int1, int2):
    """ This function takes any two integers and returns the tuple
            ( int1 + int2, int1 - int2, int1 * int2, int1 / int2, int1 // int2, int1 % int2,)"""
    return (int1 + int2, int1 - int2, int1 * int2, int1 / int2, int1 // int2, int1 % int2)
    


def all_ops_pt2(int1, int2):
    """ Same as all_ops_pt1 but this time with the operators <, <=, ==, !=, >=, and < """
    return  (int1 < int2, int1 <= int2, int1 == int2, int1 != int2, int1 >= int2, int1 > int2)


def magic_number(a_num):
    """ If the parameter a_num is a magic number answer boolean True. If not answer boolean False."""
    a_num=str(a_num)
    if '7' in a_num:
        return True
    else:
        return False


def hms_to_s(hours, minutes, seconds):
    """Convert a duration of hours:minutes:seconds to seconds."""
    return((hours*3600) + (minutes*60) + seconds) #3600 = 60*60
    


def s_to_hms(seconds):
    """Convert a duration in seconds to hours:minutes:seconds in standard form."""   
    hrs=seconds//(3600)
    mins=(seconds%(3600)//60)
    secs=((seconds%(3600))%60)
    return (hrs, mins, secs)


def add_hms(hr1, min1, sec1, hr2, min2, sec2):
    """Add two hour:minute:seconds time durations and answer the sum in standard form."""    
    hour_secs=(hr1+hr2)*3600
    min_secs=(min1+min2)*60
    sec_secs=(sec1+sec2)
    total_secs=(hour_secs+min_secs+sec_secs)
    return s_to_hms(total_secs)
   


def add_old_uk(pounds1, shillings1, pennies1, pounds2, shillings2, pennies2):
    """Add two pre-decimalisation amounts of UK currency and return the result in standard form with
    pennies<12 and shillings<20."""    
    poundsaspennies=(pounds1+pounds2)*240 # 240 = 20*12
    shillingsaspennies=(shillings1+shillings2)*12
    penniesaspennies=(pennies1+pennies2)
    totalpennies=(poundsaspennies+shillingsaspennies+penniesaspennies)
    pounds=totalpennies//(240)
    shillings=(totalpennies%(240)//12)
    pennies=((totalpennies%(240))%12)
    return  pounds, shillings, pennies


def lucky_fun(an_int):
    """ This function accepts an integer parameter (outer_int) and returns a function.
    The returned function accepts an int or float parameter (inner_num) and answers boolean True if the
    sequence of digits in outer_int occurs within inner_num, False otherwise."""    
    """add your lucky number"""
    a_num=str(input("please type in a number and we'll tell you if your lucky number is in it: "))
    def lucky_check(a_num):
        """checking if lucky number an_int is in a_num"""
        return lucky_check(a_num)
    a_num=a_num.replace('.', '')
    an_int=str(an_int)
    if (an_int) in (a_num):
        return True
    else:
        return False


def rearranged(phrase1, phrase2):
    """Answer True if parameters contain exactly the same letters, possibly arranged differently. False otherwise."""
    phrase1=phrase1.replace(' ', '')
    phrase2=phrase2.replace(' ', '')
    phrase1=phrase1.lower()
    phrase2=phrase2.lower()
    phrase1=sorted(phrase1)
    phrase2=sorted(phrase2)
    if phrase1==phrase2:
        return True
    else:
        return False
    

def is_back_to_front(phrase):
    """ If parameter is a string that reads the same backwards as forwards return True, else False."""
    phrase=phrase.replace(' ', '')
    phrase=phrase.lower()
    if phrase[::1] == phrase[::-1]:
        return True
    else:
        return False
   
