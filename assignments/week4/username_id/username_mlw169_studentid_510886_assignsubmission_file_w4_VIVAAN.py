# Vivaan's Week 4 functions







# Note: Sorry this is not finished, but I am going to keep working on it after the deadline just to try and figure it out myself.









def signum(a_num):
    if a_num > 0:
        return 1
    if a_num < 0:
        return -1
    else:
        return a_num

def middle(p1, p2, p3):
    sortedvals = sorted([p1, p2, p3])
    return sortedvals[1]

def isa_triangle(len1, len2, len3):
    if len1 + len2 + len3 >= 3:
        if len1 == len2 == len3:
            return 3
        elif len1 == len2 or len2 == len3 or len1 == len3:
            return 2
        elif len1 != len2 and len2 != len3 and len1 != len3:
            return 1
    else:
        return 0

def robberlingo(a_str):
    place = -1
    newstr = ''
    for character in a_str:
        place += 1
        if character == 'a' or character == 'e' or character == 'i' or character == 'o' or character == 'u':
            newstr += a_str[place]
        elif character == ' ':
            newstr += ' '
        else:
            newstr += a_str[place]
            newstr += 'o'
            newstr += a_str[place]
    return newstr

def merge2(str1, str2):
    merged = ''
    for str1piece, str2piece in zip(str1, str2):
        merged += "".join(str1piece + str2piece)
    return merged

def merge3(str1, str2, str3):
    merged = ''
    for str1piece, str2piece, str3piece in zip(str1, str2, str3):
        merged += "".join(str1piece + str2piece + str3piece)
    return merged

def mergen_short(*args):
    merged = ''
    for (pieces) in zip(*args):
        merged += "".join(pieces)
    return merged


def pangram(a_str):
    alphletters = []
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    alphdict = [character for character in alphabet]
    for letter in alphabet:
        if letter in a_str:
            if letter not in alphletters:
                alphletters += letter
        else:
            return False
    if alphdict == alphletters:
        return True

def letter_count(a_str):
    str_dict = {}
    for character in a_str:
        if character in str_dict:
            str_dict[character] += 1
        else:
            str_dict[character] = 1
    return str_dict
def runup(a_str):
    if a_str == '':
        return (-1, 0)
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    numbers = '0123456789'
    numberdict
    alphadict = { 'a' : 1, 'b' : 2, 'c' : 3, 'd' : 4, 'e' : 5, 'f' : 6, 'g' : 7, 'h' : 8, 'i' : 9, 'j' : 10, 'k' : 11, 'l' : 12, 'm' : 13, 'n' : 14, 'o' : 15, 'p' : 16, 'q' : 17, 'r' : 18, 's' : 19, 't' : 20, 'u' : 21, 'v' : 22, 'w' : 23, 'x' : 24, 'y' : 25, 'z' : 26 }
    char = 0
    nextchar = 1
    startsub = 0
    lensub = 0
    counter = 0
    while alphadict[a_str[char]] > alphadict[a_str[nextchar]]:
        lensub += 1
        char += 1
        nextchar += 1
    return (startsub, lensub)
