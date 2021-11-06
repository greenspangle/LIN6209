"""LIN6209 Week 4 Assignment"""


def signum(a_num):
    if a_num > 0:
        return 1
    if a_num < 0:
        return -1
    else:
        return 0


def middle(p1, p2, p3):
    a = (p1, p2, p3)
    b = sorted(a)
    middle = float(len(b)) / 2
    if middle % 2 != 0:
        return b[int(middle - .5)]
    else:
        return (b[int(middle)], b[int(middle - 1)])


def isa_triangle(len1, len2, len3):
    while len1 > 0 and len2 > 0 and len3 > 0:
        if len1 == len2 == len3:
            return 3
        elif len1 == len2 or len1 == len3 or len2 == len3:
            return 2
        elif len1 > 0 != len2 > 0 != len3 > 0:
            return 1
    else:
        return 0


def robberlingo(a_str):
    consonants = 'bcdfghjklmnpqrstvwyz'
    a = print("".join(i + 'o' + i if i in consonants else i for i in a_str))
    return a


def pangram(a_str):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    a1 = str.casefold(a_str)
    for char in alphabet:
        if char not in a1:
            return False
    return True


def merge2(str1, str2):
    s1 = str1
    s2 = str2
    the_result = ("".join(i for j in zip(s1, s2) for i in j))
    return the_result


def merge3(str1, str2, str3):
    s1 = str1
    s2 = str2
    s3 = str3
    the_result = ("".join(i for j in zip(s1, s2, s3) for i in j))
    return the_result


def letter_count(a_str):
    dict = {}
    for n in a_str:
        keys = dict.keys()
        if n in keys:
            dict[n] += 1
        else:
            dict[n] = 1
    return dict
    print(letter_count)

    ## the following questions are NOT ASSESSED but feel free to attempt them,
    ##  you will suffer no penality for not doing them.

    # def mergen_short():
    #    s = list(input())
    #    for i,c, in enumerate():
    #        s.insert(i*2,c)
    #        the_result = ("".join(s))
    #        return the_result

    # def mergen_long():

    # def runup(a_str):
    a_str.isalnum()
    a_str = ''
    current_char = ''
    previous_char = ''
    current_longest = ''
    previous_longest = ''
    for current_char in a_str:
        ##
        print(current_char)
