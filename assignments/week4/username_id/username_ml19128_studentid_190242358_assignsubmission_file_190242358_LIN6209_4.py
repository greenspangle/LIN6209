def signum (a_num):
    if a_num > 0:
        return 1
    if a_num < 0:
        return -1
    else:
        return 0

def middle (p1,p2,p3):
    a= (p1,p2,p3)
    b= sorted (a)
    return b[1]


def isa_triangle (len1, len2, len3):
    while len1>0 and len2>0 and len3>0:
        if len1==len2 == len3:
            return 3
        elif len1==len2 or len1==len3 or len2==len3:
            return 2
        elif len1>0 != len2>0 != len3>0:
            return 1
    else:
        return 0


def robberlingo (a_str):
    consonants = 'bcdfghjklmnpqrstvwxyz'
    a = print ("".join(i +'o'+ i if i in consonants else i for i in a_str))
    return a


def merge2 (str1, str2):
    s1 = str1
    s2 = str2
    the_result = ("".join(i + j for i, j in zip(s1, s2)for i in j))
    return the_result


def merge3 (str1,str2, str3):
    s1 = str1
    s2 = str2
    s3 = str3
    the_result = ("".join(i + j for i, j in zip(s1, s2, s3)for i in j))
    return the_result

def mergen_short():

def mergen_long():


def pangram (a_str):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    for char in alphabet:
        if char not in a_str:
            return False
        return True


def letter_count (a_str):
    dict = {}
    for n in a_str:
        keys = dict.keys ()
        if n in keys:
            dict[n]+=1
        else:
            dict [n] = 1
    return dict
    print (letter_count)


def runup (a_str):
    
