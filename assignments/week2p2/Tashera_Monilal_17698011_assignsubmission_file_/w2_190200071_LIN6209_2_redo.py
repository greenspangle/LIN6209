def magic7():
    return 7

def times2(a_value):
    the_result = a_value + a_value
    return the_result

def all_ops_pt1(int1,int2):
    the_result = ( int1 + int2, int1 - int2, int1 * int2, int1 / int2, int1 // int2, int1 % int2,)
    return the_result

def all_ops_pt2(int1,int2):
    the_result = ( int1 < int2, int1 <= int2, int1 == int2, int1 != int2, int1 >= int2, int1 > int2,)
    return the_result

def magic_number(a_num):
    any_number = set(str(a_num))
    magic_number = "7"
    if magic_number in any_number:
        return True
    else:
        return False

def hms_to_s(hours,mintues,seconds):
    s = (hours*36000) + (mintues*60) + seconds
    return s

def s_to_hms(seconds):
    hours=seconds//3600
    seconds%=3600
    mintues=seconds//60
    seconds=seconds%60
    return (hours,mintues,seconds)

def add_hms(hr1,min1,sec1,hr2,min2,sec2):
    hours = hr1+hr2
    mintues = min1+min2
    seconds = sec1+sec2
    hours = seconds //3600
    #seconds %= seconds = 3600
    mintues = seconds//60
    seconds = seconds % 60
    return (hours,minutes,seconds)

def add_old_uk(pounds1, shillings1, pennies1, pounds2, shillings2, pennies2):
    shillings_to_pounds = (shillings1+shillings2)//20
    pounds = (pounds1+pounds2) + shillings_to_pounds
    pennies_to_shillings = (pennies1+pennies2)//12
    shillings = ((shillings1+shillings2)%20) + pennies_to_shillings
    pence = (pennies1+pennies2)%12
    return pounds,shillings,pence

#def rearranged(phrase1, phrase2):
    #if sorted (phrase1) = sorted (phrase2):
        #return True
    #else:
        #return False
    
def is_back_to_front(phrase):
    pass
    #if phrase[:]==phrase[::]:
        #return True
    #else:
        #return False

#def lucky_fun(an_int):
    #def lucky_fun(an_int):
        #lucky_fun = set(str(an_int))
        #def unlucky_fun(inner_num):
            #unlucky_fun = set(str(inner_num))
            #if str(an_int) in str (inner_num):
                #return True
            #else:
                #return False
            #else:
                #return (unlucky_fun)
    

        
        



        
    
