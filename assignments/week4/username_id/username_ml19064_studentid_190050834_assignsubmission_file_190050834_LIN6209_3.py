def signum(a_num):
    if a_num > 0:
        return 1
    elif a_num == 0:
        return 0
    else:
        return -1
def middle(p1, p2, p3):
    unordered=(p1, p2, p3)
    ordered=sorted(unordered)
    return ordered[1]
def isa_triangle(len1, len2, len3):
    if len1 + len2 > len3 and len2 + len3 > len1 and len1 + len3 > len2:
        if len1 == len2 == len3:
            return 3
        elif len1==len2 and len1 != len3 or len2 == len3 and len2 != len1 or len3 == len1 and len3 != len2:
            return 2
        else:
            return 1
    else:
        return 0
def robberlingo1(a_str):
    vowels = ('aieou ')
    res=''
    for i in a_str:
        if i not in vowels:
            res+=i+'o'+i
        else:
            res+=i
    return res       
def pangram(a_str):
    alphaBank='abcdefghijklmnopqrstuvwxyz'
    for i in alphaBank:
        if i not in a_str:
            return False
    return True
def letter_count(a_str):
    record=dict.fromkeys(a_str)
    print(record)
    for i in a_str:
        record[i] = 0 #changing from NoneType to int 0
    for i in a_str:
        record[i] = record[i]+1
    return record
def merge3(str1, str2, str3):
    newstr=''
    for i in range(len(str1)):
        newstr+=str1[i] +str2[i]+str3[i]
    return newstr
def merge(str1, str2):
    newstr=''
    for i in range(len(str1)):
        newstr+=str1[i] +str2[i]
    return newstr
















