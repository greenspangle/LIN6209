def signum(a_num):
    if a_num > 0:
        return 1
    elif a_num < 0:
        return -1
    else:
        return 0


def middle(p1, p2, p3):
    lst = [p1, p2, p3]
    lst.sort()
    return lst[1]


def isa_triangle(len1, len2, len3):
    if len1 > len2 + len3 or len2 > len1 + len3 or len3 > len1 + len2:
        return 0
    elif len1 == len2 and len2 == len3 and len3 == len1:
        return 3
    elif len1 == len2 or len2 == len3 or len3 == len1:
        return 2
    else:
        return 1


def robberlingo(a_str):
    consonants = 'bcdfghjklmnpqrstvwxyz'
    translation = ''
    for current_char in a_str:
        if current_char in consonants:
            translation += current_char + "o" + current_char
        else:
            translation += current_char
    return translation


def pangram(a_str):
    str_set = set(a_str)
    letters = set("abcdefghijklmnopqrstuvwxyz")
    return len(letters - str_set) == 0


def merge2(str1, str2):
    length_of_str = len(str1)
    result_str = ''
    for index in range(length_of_str):
        result_str += str1[index] + str2[index]
    return result_str


def merge3(str1, str2, str3):
    length_of_str = len(str1)
    result_str = ''
    for index in range(length_of_str):
        result_str += str1[index] + str2[index] + str3[index]
    return result_str


def letter_count(a_str):
    char_count = dict.fromkeys(a_str, 0)
    for char in a_str:
        char_count[char] += 1
        pass
    return char_count
