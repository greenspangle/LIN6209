def magic7():
    """This function answers the integer 7 every time it is called"""
    return 7



def times2(parameter):
    """ This function takes any number or string and returns twice the value."""
    return parameter *2



def all_ops_pt1(int1, int2):
    """ This function takes any two integers and returns the tuple
            ( int1 + int2, int1 - int2, int1 * int2, int1 / int2, int1 // int2, int1 % int2,)"""
    op_sum = int1 + int2
    op_sub = int1 - int2
    op_mult = int1 * int2
    op_div = int1 / int2
    op_fl_div = int1 // int2
    op_mod = int1 % int2
    
    return  op_sum, op_sub, op_mult, op_div, op_fl_div, op_mod



def all_ops_pt2(int1, int2):
    """ Same as all_ops_pt1 but this time with the operators <, <=, ==, !=, >=, and >
        (last operator corrected from '<' to '>' 6pm Tuesday)"""
    return  int1 < int2, int1 <= int2, int1 == int2, int1 != int2, int1 >= int2,int1 > int2



def magic_number(a_num):
    """ If the parameter a_num is a magic number answer boolean True. If not answer boolean False.
    A magic number is any number that contains the digit 7."""

    magic = 7
    s = set(str(a_num))
    is_magic = str(magic) in s
        
    return  is_magic



def hms_to_s(hours, minutes, seconds):
    """Convert a duration of hours:minutes:seconds to seconds"""

    scnd = (hours*60 + minutes)*60 + seconds
    return  scnd



def s_to_hms(seconds):
    """Convert a duration in seconds to hours:minutes:seconds in standard form"""

    minutes = seconds // 60
    sec_left = seconds % 60

    hours = minutes // 60
    min_left = minutes %60
    
    return  hours, min_left, sec_left



def add_hms(hr1, min1, sec1, hr2, min2, sec2):
    """Add two hour:minute:seconds time durations and answer the sum in standard form"""

    seconds = hms_to_s(hr1,min1,sec1) + hms_to_s(hr2,min2,sec2)

    return  s_to_hms(seconds)



def add_old_uk(pounds1, shillings1, pennies1, pounds2, shillings2, pennies2):
    """Add two pre-decimalisation amounts of UK currency and return the result in standard form"""

    def pound_to_shill(lb):
        return lb*20

    def shill_to_pence(sh):
        return sh*12

    def psd_to_d(lb,sh,d):
        pennies = shill_to_pence(sh+pound_to_shill(lb))+d
        return pennies

    def d_to_psd(d):
        shill = d//12
        pennies_left = d%12
        pound= shill // 20
        shill_left = shill%20
        return pound,shill_left, pennies_left
    

    total_pennies = psd_to_d(pounds1, shillings1, pennies1) + psd_to_d(pounds2, shillings2, pennies2)
    
    return d_to_psd(total_pennies)



def lucky_fun(an_int):
    """ This function accepts an integer parameter (outer_int) and returns a function.
    The returned function accepts an int or float parameter (inner_num) and answers boolean True if the
    sequence of digits in outer_int occurs within inner_num, False otherwise"""

    def new_magic(a_num):
        
        magic = str(an_int)
        s = str(a_num)
        is_magic =  magic in s
        
        return  is_magic
    
    return  new_magic




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

    phrase1 = phrase1.lower()
    phrase1 = phrase1.replace(" ","")

    phrase2 = phrase2.lower()
    phrase2 = phrase2.replace(" ","")

    return  sorted(phrase1) == sorted(phrase2)



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
  
    phrase = phrase.lower()
    phrase = phrase.replace(" ","")

    rev_phrase = phrase[::-1]
    
        
    return  phrase == rev_phrase

    
