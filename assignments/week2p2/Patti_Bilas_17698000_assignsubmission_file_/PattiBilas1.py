#ID - 190254812

def magic7():
    return 7 


def times2(parameter):
    result = parameter + parameter 
    return result


def all_ops_pt1(int1, int2):
    num1 = int1 + int2
    num2 = int1 - int2 
    num3 = int1 * int2 
    num4 = int1 / int2 
    num5 = int1 // int2 
    num6 = int1 % int2
    return num1, num2, num3, num4, num5, num6


def all_ops_pt2(int1, int2):
    num1 = int1 < int2
    num2 = int1 <= int2 
    num3 = int1 == int2 
    num4 = int1 != int2 
    num5 = int1 >= int2 
    num6 = int1 > int2
    return num1, num2, num3, num4, num5, num6


def magic_number(a_num):
    return '7' in str(a_num)


def hms_to_s(hours, minutes, seconds):
    return int(hours) * 3600 + int(minutes) * 60 + int(seconds)


def s_to_hms(seconds):
    hours = seconds // 3600
    seconds %= 3600
    minutes = seconds // 60
    seconds %= 60
    return(hours, minutes, seconds)   


def add_hms(hr1, min1, sec1, hr2, min2, sec2):
    hours = hr1 + hr2
    minutes = min1 + min2
    seconds = sec1 + sec2

    if (minutes >= 60):
        hours += minutes // 60
        minutes = minutes % 60
    if (seconds >= 60):
        minutes += seconds // 60
        seconds = seconds % 60 

    return(hours, minutes, seconds)


def add_old_uk(pounds1, shillings1, pennies1, pounds2, shillings2, pennies2):
    pounds = pounds1 + pounds2
    shillings = shillings1 + shillings2
    pennies = pennies1 + pennies2

    if(shillings >= 20):
        pounds += shillings // 20
        shillings = shillings % 20

    if(pennies >= 12):
        shillings += pennies // 12
        pennies = pennies % 12

    return(pounds, shillings, pennies)


def lucky_fun(an_int):
    def another_fun(inner_num):
        return str(an_int) in str(inner_num).replace(".", "")

    return another_fun 


def rearranged(phrase1, phrase2):
    if sorted(phrase1) == sorted(phrase2):
        return True
    else:
        return False


def is_back_to_front(string):
    backstring = string[::-1]
    if string == backstring:
        return True
    else:
        return False