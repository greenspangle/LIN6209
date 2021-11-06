def signum(a_num):
    if a_num > 0:
        return 1
    elif a_num < 0:
        return -1
    else:
        return 0


def middle(p1,p2,p3):
    if p1 >= p2 and p1 <= p3 or p1<=p2 and p1>=p3:
        return p1
    elif p2 >= p1 and p2 <= p3 or p2<=p1 and p2>=p3:
        return p2
    else:
        return p3


def isa_triangle(len1,len2,len3):
    if len1+len2<=len3 or len2+len3<=len1 or len1+len3<=len2:
        return 0
    elif len1==len2==len3:
        return 3
    elif len1==len2 or len2==len3 or len3==len1:
        return 2
    else:
        return 1


def robberlingo(a_str):
    consonants=str('bcdfghjklmnpqrstvwxyz')
    translation=[]
    for current_character in a_str:
        if current_character in consonants:
            translation += current_character+'o'+current_character
        else:
            translation += current_character
    trans=''
    for x in translation:
        trans+=x
    return trans
    

def pangram(a_str):
    letters=set('abcdefghijklmnopqrstuvwxyz')
    a_str=a_str.lower()
    a_str=set(a_str)
    set1=((letters)-(a_str))
    if set1 == set():
        return True
    else:
        return False


def merge2(str1,str2):
    length_of_str = len(str1)
    result_str = ''
    for index in range(length_of_str):
        result_str+=(str1[index] + str2[index])
    return result_str


def merge3(str1,str2,str3):
    length_of_str = len(str1)
    result_str = ''
    for index in range(length_of_str):
        result_str+=(str1[index] + str2[index] + str3[index])
    return result_str


def letter_count(a_str):
    char_count_dict=dict.fromkeys(a_str,0)
    for char in a_str:
        char_count_dict[char]=char_count_dict[char]+1
        pass
    return char_count_dict
