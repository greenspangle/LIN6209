def magic7():
    """Always return the integer 7"""
    return 7

def times2 (parameter):
    """Return twice a value"""
    the_result = parameter + parameter
    return the_result

def all_ops_pt1(int1, int2):
    """Return the tuple of any two integers"""
    the_result = int1 + int2, int1 - int2, int1 * int2, int1 / int2, int1 // int2, int1 % int2
    return the_result

def all_ops_pt2(int1, int2):
    """Return the tuple of any two integers - extended"""
    the_result = int1 < int2, int1 <= int2, int1 == int2, int1 != int2, int1 >= int2, int1 > int2
    return the_result

def magic_number(a_num):
    """If a_num contains 7 answer boolean True. If not answer boolean False."""
    if 7 in a_num:
        return True
    else:
        return False

def hms_to_s(hours, minutes,seconds):
    """Convert a duration of hours:minutes:seconds to seconds"""
    the_result = ((hours * 3600) + (minutes * 60) + seconds)
    return the_result

def s_to_hms(seconds):
    """Convert a duration of seconds into hours:minutes:seconds"""
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    secs = (seconds % 3600) % 60
    return hours,minutes,secs

def add_hms(hr1,min1,sec1,hr2,min2,sec2):
    """Add two hours:minutes:seconds time durations in the same format"""
    hours = hr1 + hr2
    minutes = min1 + min2
    seconds = sec1 + sec2
    if sec1 + sec2 >=60:
        seconds = (sec1 + sec2) % 60
        minutes = (min1 + min2) + ((sec1 + sec2) // 60)
    if min1 + min2 >=60:
        minutes = (min1 + min2) % 60
        hours = (hr1 + hr2) + ((min1 + min2) // 60)
    the_result = hours,minutes,seconds
    return the_result

def add_old_uk(pounds1,shillings1,pennies1,pounds2,shillings2,pennies2):
    """Add two pre-decimilisation amounts of UK currency in the same format"""
    pounds = pounds1 + pounds2
    shillings = shillings1 + shillings2
    pence = pennies1 + pennies2
    if pennies1 + pennies2 >=12:
        pence = (pennies1 + pennies2) % 12
        shillings = (shillings1 + shillings2) + ((pennies1 + pennies2) // 12)
    if shillings1 + shillings2 >=20:
        shillings = (shillings1 + shillings2) % 20
        pounds = (pounds1 + pounds2) + ((shillings1 + shillings2) // 20)
    the_result = pounds,shillings,pence
    return the_result

def lucky_fun(an_int):
    """If the specified (outer_int) occurs within (inner_num) the input (outer_int)(inner_num) will return True"""
    def inner_function(inner_num):
        if (an_int) in (inner_num):
            return True
        else:
            return False

def rearranged(phrase1,phrase2):
    """If both parameters contain the same letters, the function will return true"""
    if(sorted(phrase1)) == (sorted(phrase2)):
        return True
    else:
        return False

def is_back_to_front(phrase):
    """If parameter is a string that reads the same backwards as forwards return True, else False"""
    if phrase[0] == phrase[-1]:
        return True
    else:
        return False
