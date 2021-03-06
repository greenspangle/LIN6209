# Week 4 Assignment


def signum(a_num):
    """If a_num is greater than zero return 1. If it's less than zero return integer minus one. Otherwise, return
    integer zero."""
    if a_num > 0:
        return 1
    elif a_num < 0:
        return -1
    else:
        return 0


def middle_v1(p1, p2, p3):
    """Return the middle value"""
    if p1 >= p2 >= p3 or p1 <= p2 <= p3:  # chained comparison
        return p2
    elif ((p2 <= p3) and (p3 <= p1)) or ((p2 >= p3) and (p3 >= p1)):
        return p3
    else:
        return p1


def middle_v2(p1, p2, p3):
    """Return the middle value"""
    # put parameters into a list
    p_list = [p1, p2, p3]
    # sort the list
    p_list.sort()
    # return the middle value from the list
    return p_list[1]


# choose the logic version rather than the more general sorting version
middle = middle_v1


def isa_triangle(len1, len2, len3):
    """The three parameters are guaranteed to be numbers. If they are interpreted as the lengths of the sides of a
    euclidean triangle, return an integer to indicate which type of triangle they would construct according to this
    table:
    ** 0 ** | No triangle possible
    ** 1 ** | Scalene
    ** 2 ** | Isosceles
    ** 3 ** | Equilateral
    """
    if len1 > (len2 + len3) or len2 > (len1 + len3) or len3 > (len1 + len2):
        # no triangle possible
        return 0
    elif len1 == len2 and len2 == len3 and len1 == len3:
        # equilateral
        return 3
    elif len1 == len2 or len2 == len3 or len3 == len1:
        # isosceles
        return 2
    else:
        # only option left ia a scalene triangle
        return 1


def robberlingo(a_str):
    """Translate a_str text into “rövarspråket” (Swedish for “robber’s language”).
    That is, double every consonant and place an occurrence of “o” in between. For example, robberlingo(“this is fun”)
    should return the string tothohisos isos fofunon”.
    """
    # Example in problem statement is all lower-case and statement says nothing about upper case.
    # Assume therefore that uppercase is just copied verbatim into the result
    #
    # create a list to build result in
    robber_lst = []
    # consonants are characters that are not vowels
    consonants = set('abcdefghijklmnopqrstuvwxyz') - set('aeiou')
    # iterate through string, testing for consonants and constructing result as we go.
    for char in a_str:
        # all characters in a_str are retained in translated text
        robber_lst.append(char)
        if char in consonants:
            # consonants are repeated with an 'o' between them
            robber_lst.append('o')
            robber_lst.append(char)
    # All of input string processed. Assemble result into a string and return it
    result = ''.join(robber_lst)
    return result


def pangram_v1(a_str: str):
    """Answer true if a_str is a pangram and false if not. Ignore capitalisation and punctuation, only consider
    the characters a-z."""
    # a pangram contains all the letters 'a' to 'z' so construct that set
    alphabet = set('abcdefghijklmnopqrstuvwxyz')
    # convert string to lower-case and then cast to a set
    a_str_as_set = set(a_str.lower())
    # get the set of alphabetical characters in a_str_set by intersecting it with alphabet
    a_str_alphachars_set = a_str_as_set.intersection(alphabet)
    # if a_str_alphachars_set is equal to the alphabet then a_str is a pangram, else it is not
    return a_str_alphachars_set == alphabet


def pangram_v2(a_str: str):
    """Answer true if a_str is a pangram and false if not. Ignore capitalisation and punctuation, only consider
    the characters a-z."""
    # a pangram contains all the letters 'a' to 'z' so construct that set
    alphabet = set('abcdefghijklmnopqrstuvwxyz')
    # convert string to lower-case and then cast to a set
    a_str_as_set = set(a_str.lower())
    # remove all the characters in a_str_as_set from alphabet
    remainder = alphabet - a_str_as_set
    # if remainder is empty set then string contains all letters of alphabet and hence is a pangram
    return not len(remainder)


# both options are good but I have to choose one of them so
pangram = pangram_v2


def merge2(str1, str2):
    """Interleave the successive characters of two strings of the same length into a single string and return
    the result."""
    # the two strings are stated to be the same length but let's check regardless
    len1 = len(str1)
    len2 = len(str2)
    if len1 != len2:
        print("please stop breaking the function contract and expecting me to cope!")
        return ''
    # build result as a list of strings
    result = []
    for i in range(len1):
        result.append(str1[i] + str2[i])
    # both strings processed, now transform the result from list to a single string
    result = ''.join(result)
    # and return it
    return result


def merge3(str1, str2, str3):
    """Interleave the successive characters of three strings of the same length into a single string and return
    the result."""
    # exactly the same logic as merge2()

    # the the strings are stated to be the same length but let's check regardless
    len1 = len(str1)
    len2 = len(str2)
    len3 = len(str3)
    if len1 != len2 or len2 != len3:
        print("please stop breaking the function contract and expecting me to cope!")
        return ''
    # build result as a list of strings
    result = []
    for i in range(len1):
        result.append(str1[i] + str2[i] + str3[i])
    # all 3 strings processed, now transform the result from list to a single string
    result = ''.join(result)
    # and return it
    return result


def letter_count(a_str):
    """Return a dictionary with every character (including spaces and punctuation) in a_str as a key with a value
    equal to the number of occurrences of that character in a_str. Only characters in a_str are keys in the
    returned dictionary."""
    # create the dictionary with the key entries associated with a value of 0
    letter_dict = dict.fromkeys(a_str, 0)
    # now iterate through string, incrementing the respective entry for every character encountered
    for each_char in a_str:
        letter_dict[each_char] += 1
    # all letters done, return the resulting dictionary
    return letter_dict

# end #
