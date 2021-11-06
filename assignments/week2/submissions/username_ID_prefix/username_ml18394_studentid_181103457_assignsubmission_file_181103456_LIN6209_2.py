
def magic7():
    return(7)

def times2(a_value):
    """ Return twice a_value  """
    the_result = a_value + a_value
    return the_result

def all_ops_pt1 (int1, int2):
    	""" This function takes any two integers and returns the tuple" """
    	return ( int1 + int2, int1 - int2, int1 * int2, int1 / int2, int1 // int2, int1 % int2,)

    	
def all_ops_pt2(int1, int2):
    return ( int1 < int2, int1 <= int2, int1 ==int2, int1!= int2, int1 >=int2, int1 > int2,)

def magic_number (a_num):
    return "7" in str(a_num)

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


def s_to_hms(seconds):
   seconds = seconds % (24 * 3600)
   hour = seconds // 3600
   seconds %= 3600
   minutes = seconds // 60
   seconds %= 60
   return "%02d:%02d:%02d" % (hour, minutes, seconds)




def add_hms(hr1, min1, sec1, hr2, min2, sec2):
	return (hr1,+min1,+sec1, + hr2,+min2,+sec2)

    

    



def add_old_uk(pounds_1,shillings_1,pennies_1,pounds_2,shillings_2,pennies_2):
    sum_pounds=pounds_1+pounds_2
    sum_shillings=shillings_1+shillings_2
    sum_pennies=pennies_1+pennies_2

    if sum_pennies>=12:
        sum_shillings=sum_shillings+(sum_pennies/12)
        sum_pennies=sum_pennies%12
    if sum_shillings>=20:
        sum_pounds=sum_pounds+(sum_shillings/20)
        sum_shillings=sum_shillings%20
    return(int(sum_pounds),int(sum_shillings),int(sum_pennies))



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


def rearranged(phrase1, phrase2): 

	if(sorted(phrase1)== sorted(phrase2)): print("True") 

	if(sorted(phrase1)!= sorted(phrase2)): print("False") 

def is_back_to_front(phrase): 

    phrase = phrase.replace(' ', '') 

    phrase = phrase.casefold() 

    if list(phrase) == list(reversed(phrase)): 

        return True 

    else: 

        return False










  
 
    
