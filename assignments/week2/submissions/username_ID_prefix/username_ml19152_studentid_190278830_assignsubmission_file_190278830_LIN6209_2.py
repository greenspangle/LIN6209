def magic7():
    """ Return 7 """
    the_result = 7
    return the_result


def times2(parameter):
    """ Return twice parameter  """
    the_result = parameter + parameter
    return the_result



def all_ops_pt1(int1, int2):
     """ This function takes any two integers and returns the tuple """
     return int1 + int2, int1 - int2, int1 * int2, int1 / int2, int1 // int2, int1 % int2

    

def all_ops_pt2(int1, int2):
     """ This function takes any two integers and returns the tuple """
     return int1 < int2, int1 <= int2, int1 == int2, int1 != int2, int1 >= int2, int1 > int2


def magic_num(a_num):
    """ If the parameter a_num is a magic number answer boolean True. If not answer boolean False."""
    return '7' in str(a_num)


def hms_to_s(hoursminutesseconds_str):
    """Convert a duration of hours,minutes,seconds to seconds"""
    h, m, s = hoursminutesseconds_str.split(",")
    return int(h) * 3600 + int(m) * 60 + int(s)

# print(hms_to_s('0,0,0'))


def s_to_hms(seconds):
    """Convert a duration in seconds to hours:minutes:seconds in standard form."""
    a = str(seconds //3600)
    b = str((seconds%3600)//60)
    c = str((seconds%3600)%60)
    d = ["{},{},{}".format(a,b,c)]
    return d

#  print(s_to_hms(10000))



def add_hms(hr1, min1, sec1, hr2, min2, sec2):
    """Add two hour:minute:seconds time durations and answer the sum in standard form"""
    secs = sec1 + sec2
    mins = min1 + min2
    hrs = hr1 + hr2
    if(secs >= 60):
        mins += secs//60
        secs = secs%60
    if(mins >= 60):
        hrs += mins//60
        mins = mins%60
    return (hrs, mins, secs)


def add_old_uk(pounds1, shillings1, pennies1, pounds2, shillings2, pennies2): 
    """Add two pre-decimalisation amounts of UK currency and return the result in standard form with
    pennies<12 and shillings<20."""
    pounds = pounds1 + pounds2
    shillings = shillings1 + shillings2
    pennies = pennies1 + pennies2
    if (pennies >=12):
        shillings += pennies//12
        pennies = pennies%12
    if (shillings >=20):
        pounds += shillings//20
        shillings = shillings%20
    return (pounds, shillings, pennies)



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
    # y our code goes here
    return  # a function


def rearranged(phrase1, phrase2):
    if set(filter(str.isalnum, phrase1)) == set(filter(str.isalnum, phrase2)):
        print('True')
    else:
        print('False')



def is_back_to_front(phrase):
    """ If parameter is a string that reads the same backwards as forwards return True, else False."""
    if str(phrase) == str(phrase)[::-1] :
        print("True")
    else:
        print("False")

