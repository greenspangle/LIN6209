def signum(a_num):
    if (a_num > 0):
        return 1

    if (a_num < 0):
        return -1

    else:
        return 0

def middle(p1,p2,p3):
    #return middle value
    #middle value is in alphabetical order
    #if (p1 < p2 < p3) and (p1 <= != p2 <= != p3) and (p1 == p2 == p3) and (p1 >= p2 >= p3) and (p1 > p2 > p3)
    if (p1 < p2 < p3) and (p1 != p2 != p3) and (p1 == p2 == p3) and (p1 >= p2 >= p3) and (p1 > p2 > p3):
        result = sum ((p1 < p2 < p3) and (p1 != p2 != p3) and (p1 == p2 == p3) and (p1 >= p2 >= p3) and (p1 > p2 > p3))

    return result 

def isa_triangle(len1,len2,len3):
    if (len1 == len2 == len3):
        return 3

    if(len1 == len2) or (len1 == len3)or (len2==len3):
        return 2

    if (len1, len2, len3):
        return 1

    if (len1 < len2 == len3) and (len1 == len2 < len3):
        return 0

def robberlingo(a_str):
    a_str = 'abracadrabra'
    vowels = 'aeiou'
    consonants = 'bcdfghjklmnpqrstvwxyz'
    translation : []
    for current_char in a_str:
        s = 'bcdfghjklmnpqrstvwxyz'
        n = 'o'
        if current_char in consonants:
         ''.join([char*n for char in s])
        else:
         print('just add character to translation')


def pangram(a_str):
    a_str = a_str.lower()
    set('a_str')
    set('abcdefghijklmnopqrstuvwxyz')
    result = set('a_str')- set('abcdefghijklmnopqrstuvwxyz')
    if result == set():
        return true
    else:
        return false

def merge2(str1,str2):
    str_1 = str
    str_2 = str
    length_of_str = len(str_1)
    for index in range(length_of_str):
        result = len(str_1[index] + str_2[index])
        return result
    
