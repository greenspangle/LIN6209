# ID - 190254812

from collections import Counter


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


def magic_nubmer(a_num):
    while (a_num > 0):
        i = a_num % 10
        a_num = a_num // 10

        if i == 7:
            return True    

    return False


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

    hours = seconds // 3600
    seconds %= 3600
    minutes = seconds // 60
    seconds %= 60

    return(hours, minutes, seconds)


def add_old_uk(pounds1, shillings1, pennies1, pounds2, shillings2, pennies2):
    pound = pounds1 + pounds2
    shillings = shillings1 + shillings2
    pennies = pennies1 + pennies2

    if(shillings > 20):
        shillings = 0
        pound = pound + 1
    
    elif(pennies > 12):
        pennies = 0
        shillings = shillings + 1

    elif(pennies > 240):
        pound = pound + 1   

    return(pound, shillings, pennies)


def lucky_fun(an_int):
    outerint = input("Input a Value for a ")
    print(outerint)


def rearranged(phrase1, phrase2):
    words = Counter(filter(str.isalnum, phrase1)) == Counter(filter(str.isalnum, phrase2))
    return(words)


def is_back_to_front(phase):
    for i in range(len(phase) // 2):
        if phase[i] != phase[-1-i]:
            return False

    return True