# Week 4/5 Assignment

def signum(a_num):
    if a_num > 0:
        return 1
    elif a_num < 0:
        return -1
    else:
        return 0


def middle(p1, p2, p3):
    sorted_list = sorted([p1, p2, p3])
    return sorted_list[1]


def isa_triangle(len1, len2, len3):
    arr = sorted([len1, len2, len3])

    if arr[0] < 0 or arr[2] >= arr[0] + arr[1]:
        return 0

    if len(set(arr)) == 1:
        # Equilateral
        return 3
    elif len(set(arr)) == 2:
        # Isosceles
        return 2
    else:
        # Scalene
        return 1


def robberlingo(a_str):
    chars = "aeiou "
    result = ""

    for i in a_str.lower():
        if i not in chars:
            result += f'{i}o{i}'
        else:
            result += i

    return result

def pangram(a_str):
    filter_chars = 'abcdefghijklmnopqrstuvwxyz'
    cleaned_str = ''

    for i in a_str.lower():
        if i in filter_chars:
            cleaned_str += i

    return True if len(set(filter_chars) - set(cleaned_str)) == 0 else False

def merge2(str1, str2):
    result = ''

    for i in range(len(str1)):
        result += f'{str1[i]}{str2[i]}'

    return result


def merge3(str1, str2, str3):
    result = ''

    for i in range(len(str1)):
        result += f'{str1[i]}{str2[i]}{str3[i]}'

    return result


def letter_count(a_str):
    letter_freq = {}

    for i in a_str:
        if i in letter_freq:
            letter_freq[i] += 1
        else:
            letter_freq[i] = 1

    return letter_freq

# non assessed
def runup(a_str):
    if a_str == '':
        return (0, -1)

    prev = ''
    curr = ''
    longest = ''

    cleaned_str = a_str.lower().replace(" ", '').replace('.', '')

    for letter in cleaned_str:
        if prev <= letter:
            curr += letter
            if len(curr) > len(longest):
                longest = curr
        else:
            curr = letter

        prev = letter

    return a_str.find(longest), len(longest)

def mergen_short(*strs):
    cleaned_list = [i.replace(" ", '') for i in strs]

    sorted_list = list(sorted(cleaned_list, key=len))
    result = ''

    for i in range(len(sorted_list[0])):
        for j in range(len(cleaned_list)):
            try:
                result += cleaned_list[j][i]
            except:
                result += ''

    return result


def mergen_long(*strs):
    cleaned_list = [i.replace(" ", '') for i in strs]

    sorted_list = list(sorted(cleaned_list, key=len))
    result = ''

    for i in range(len(sorted_list[-1])):
        for j in range(len(cleaned_list)):
            try:
                result += cleaned_list[j][i]
            except:
                result += ''

    return result
