def signum(a_num):
    if a_num > 0:
        return 1
    if a_num < 0:
        return -1
    else:
        return 0

def middle(p1,p2,p3):
    my_list=[p1,p2,p3]
    sorted_list=sorted(my_list)
    middle_value=sorted_list[1]
    return middle_value

def merge2(str1,str2):
    str_1 = 'abc'
    str_2 = 'def'
    length_of_str = len(str_1)
    result_str = ''
    for index in range(length_of_str):
        return str1+str2

def merge3(str1,str2,str3):
    str_1 = 'abc'
    str_2 = 'def'
    str_3 = 'ghj'
    length_of_str = len(str_1)
    result_str = ''
    for index in range(length_of_str):
        return str1+str2+str3

def letter_count(a_str):
    dict = {}
    for c in a_str:
        keys= dict.keys()
        if c in keys:
            dict[c] += 1
        else:
            dict[c] =1
    return dict
    return(letter_count('abracdabra'))

#def isa_triangle(len1,len2,len3):
    #if len1+len2+len3 = 180 %3
    #return 3
#or:
    #if len1==len2 and != len3
    #return 2
#or:
    #if len1 != len2, len2 != len3 and len1 != len3
    #return 1
#else:
    #if len1+len2+len3 != 180
    #return 0

#len1+len2+len3=180

#def robberlingo(a_str):
    #a_str = 'robberlingo'
    #vowels= 'aeiou'
    #consonnts= 'bcdfghjklmnpqrstvwxyz'
    #translation =[]
    #for current_char in a_str:
        #if current_char in consonants:
            #print('current_char+''o''+current_char')
            #else:
                #print('current_char')
                #return translation

#def pangram(a_str):
     #A ={'t','h','e','q','u','i','c','k','b','r','o','w','n','f','o','x','j','u','m','p','s','o','v','e','r','t','h','e','l','a','z','y','d','o','g'}
     #B ={'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'}
     #print(A-B)
     #print(B-A)
     #return len(a_str)




