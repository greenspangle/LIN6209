
def magic7():
    """This function answers the integer 7 every time it is called"""
    return 7

def times2(parameter):
    """ return twice parameter """
    the_result = parameter + parameter
    return the_result 

def all_ops_pt1(int1, int2): 
    """ This function takes any two intergers and return the tuple """
    return int1 + int2, int1 - int2, int1 * int2, int1 / int2, int1 // int2, int1 % int2,

def all_ops_pt2(int1, int2):
    """ This function takes any two intergers and return the tuple """
    return  int1 < int2, int1 <= int2, int1 == int2, int1 != int2, int1 >= int2, int1 > int2

def magic_number(a_num):
    """If the parameter a_num is magic number (7) answer boolean True. If not answer boolean False. """
    return '7' in str(a_num) 

def hms_to_s(hours, minutes, seconds):
    """Convert a duration of hours:minutes:seconds to seconds """
    h = hours
    m = minutes
    s = seconds
    the_result = int(h * 3600) + int (m * 60) + int (s)
    return the_result 


def s_to_hms(seconds):
    """ Convert a duration in seconds to hours:minutes:seconds in standard form. """
    hours = seconds //3600
    seconds %= 3600
    minutes = seconds // 60
    s = seconds % 60
    return (hours, minutes, s)


def add_hms (hr1, min1, sec1,hr2, min2, sec2):
    secs = sec1 + sec2
    mins = min1 + min2
    hrs = hr1 + hr2
    if (secs >= 60):
        mins += secs// 60
        secs = secs%60
    if (mins >= 60):
        hrs += mins//60
        mins = mins%60
    return (hrs, mins, secs)


def add_old_uk (pounds1, shillings1, pennies1, pounds2, shillings2, pennies2):
    pounds = pounds1 + pounds2
    shillings = shillings1 + shillings2
    pennies = pennies1 + pennies2
    if(pennies >= 12):
        shillings += pennies//12
        pennies = pennies%12
    if (shillings >= 20):
        pounds += shillings//20
        shillings = shillings%20
    return (pounds, shillings, pennies)


def lucky_fun(an_int):
    """ This function accepts an integer parameter (outer_int) and returns a function.
    The returned function accepts an int or float parameter (inner_num) and answers boolean True if the
    sequence of digits in oute r_int occurs within inner_num, False otherwise."""
    def other_fun(inner_num):
        return str(an_int) in str(inner_num).replace(" ","")
    return other_fun
 

def rearranged(phrase1, phrase2):
    """Answer True if parameters contain exactly the same letters, possibly arranged differently. False otherwise."""
    phrase1 = phrase1.lower().replace(" ","")
    phrase2 = phrase2.lower().replace(" ","")
    return sorted(phrase1) == sorted(phrase2)
  

def is_back_to_front(phrase):
    """ If parameter is a string that reads the same backwards as forwards return True, else False."""
    phrase = phrase.lower().replace(" ","")
    return phrase == phrase[::-1]
