
def magic7():
    return(7)

def times2(a_value):
    """ Return twice a_value  """
    the_result = ((a_value)+ (a_value))
    return the_result

def all_ops_pt1 (int1, int2):
    	""" This function takes any two integers and returns the tuple" """
    	return ( int1 + int2, int1 - int2, int1 * int2, int1 / int2, int1 // int2, int1 % int2,)

    	
def all_ops_pt2(int1, int2):
    return ( int1 < int2, int1 <= int2, int1 ==int2, int1!= int2, int1 >=int2, int1 > int2,)

def magic_number(a_num):
    return "7" in str(a_num)
      


def hms_to_s(hours, minutes, seconds):
        tot_s =((hours)*(3600) + ((minutes)*60) + (seconds))
        return tot_s
    

def s_to_hms(seconds):
    num= (seconds)
    hour= (num//3600)
    hour1= (num%3600)
    minute= (hour1//60)
    second = (hour1%60)
    return (hour,minute,second)


##def add_hms(hr1, min1, sec1, hr2, min2, sec2):
##return (hr1,+min1,+sec1, + hr2,+min2,+sec2)

    

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



##def lucky_fun(an_int):""" This function accepts an integer parameter (outer_int) and returns a function.  The returned function accepts an int or float parameter (inner_num) and answers boolean True if the sequence of digits in outer_int occurs within inner_num, False otherwise.For example:
   

# def rearranged(phrase1, phrase2):
#     phrase = phrase.replace(' ', '')
#
#     phrase = phrase.casefold()
#
#     if(sorted(phrase1)== sorted(phrase2)): print("True")
#
#     if(sorted(phrase1)!= sorted(phrase2)): print("False")
	

def is_back_to_front(phrase): 

    phrase = phrase.replace(' ', '') 

    phrase = phrase.casefold() 

    if list(phrase) == list(reversed(phrase)): 

        return True 

    else: 

        return False










  
 
    
