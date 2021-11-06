def signum(a_num):

    result = 0
    if a_num > 0:
        result = 1
    elif a_num < 0:
        result = -1
    else:
        result = 0

    return result
        


def middle(p1, p2, p3):
    
    params = [p1,p2,p3]
    params.sort()
    
    return params[1]



def isa_triangle(len1, len2, len3):
    triangle = 0
    
    #is it a triangle? 2 sides always greater than thrid side
    if (len1+len2)>len3 and (len2+len3)>len1 and (len1+len3)>len2:
        if len1==len2==len3:
            triangle = 3
        elif len1==len2 or len1==len3 or len2==len3:
            triangle = 2
        elif len1!=len2!=len3:
            triangle = 1

    return triangle
        


def robberlingo(a_str):
    new_sent = ""

    for i in range(len(a_str)):
        if a_str[i] not in "aeiou":
            new_sent = new_sent + a_str[i] + "o" + a_str[i]
        else:
            new_sent = new_sent + a_str[i]

    return new_sent



def pangram(a_str):
    alphabet = {"a","b",'c','d','e','f','g','h','i','j','k','l',"m",'n','o','p','q','r','s','t','u','v','w','x','y','z'}
    set_str = set((a_str.lower()))

    return len(alphabet.difference(set_str)) == 0




def merge2(str1, str2):
    merged_sent = ""

    for i in range(len(str1)):
        merged_sent = merged_sent + str1[i] + str2[i]

    return merged_sent



def merge3(str1, str2, str3):
    merged_sent = ""

    for i in range(len(str1)):
        merged_sent = merged_sent + str1[i] + str2[i] + str3[i]

    return merged_sent
        


def letter_count(a_str):
    d = dict()
    
    for char in a_str:
        if char not in d.keys():
            d[char] = 1
        else:
            d[char]= d[char] + 1


    return d
