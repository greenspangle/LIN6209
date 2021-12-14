def signum(a_num):
    if a_num > 0:
        return 1
    elif a_num < 0:
        return -1
    else:
        return 0

def middle(p1, p2, p3):
    if p1 <= p2 <= p3 or p3 <= p2 <= p1:
        return p2
    elif p2 <= p1 <= p3 or p3 <= p1 <= p2:
        return p1
    else:
        return p3

def isa_triangle(len1, len2, len3):
    if (len1+len2<len3 or len1+len3<len2 or len2+len3<len1):
        return 0
    elif (len1 == len2 and len2 == len3):
        return 3
    elif (len1 == len2 or len1 == len3 or len2 == len3):
        return 2
    else:
        return 1

def robberlingo(a_str):
    a_str = 'abracadabra'
    vowels = 'aeiou'
    consonants = 'bcdfghjklmnpqrstvwxyz'
    translation = str()
    for current_char in (a_str):
        if (current_char in consonants):
            return str() + current_char + 'o' + current_char
        else:
            return str() + current_char
    return transation 
                        
def pangram(a_str):
    a_str = set(a_str.lower().replace(' ', ''))
    alphabet = set('a-z')
    if len(a_str) == len(alphabet):
        return True
    else:
        return False

def merge2(str1, str2):
    result = ''
    for i in range(len(str1)):
        result += str1[i] + str[i]
    return result

def merge3(str1, str2, str3):
    result = ''
    for i in range(len(str1)):
        result =+ str1[i] + str2[i] + str3[i]
    return result

def letter_count(a_str):
    d = dict().fromkeys(a_str,0)
    for char in a_str:
        if char in d.keys():
            d[char] += 1
        else:
            d[char] = 1
        return d
