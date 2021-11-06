def signum(a_num):
    if a_num>0:
        return 1
    if a_num<0:
        return -1
    if a_num==0:
        return 0
    
    
def middle(p1,p2,p3):
    aList= [p1,p2,p3]
    aList.sort()
    return aList[1]

def isa_triangle(len1,len2,len3):
    if len1+len2<=len3 or len1+len3<=len2 or len3+len2<=len1:
        return 0
    elif len1==len2==len3:
        return 3
    elif len1==len2 or len1==len3 or len2==len3:
        return 2
    else :
        return 1
    

# 'rovarspraket'
# 'a'    result ='e'
def robberlingo(a_str):
    
    vowels="aeiou "
    result=""
    for cm in a_str:
        if cm in vowels:
            result=result+cm
        else: # cm bushi vowels
            result=result+cm+'o'+cm
    return result


def pangram(a_str):
    a=a_str
    b=a.replace(" ","")
    c=set(b)
    d=set("abcdefghijklmnopqrstuvwxyz")
    result=c==d
    return result

def merge2(str1,str2):
    a=str1
    b=str2
    result = ''
    for index in range(len(a)): 
        result=result+a[index]+b[index]
    return result
        
def merge3(str1,str2,str3):
    a=str1
    b=str2
    c=str3
    result=''
    for index in range(len(a)):
        result=result+a[index]+b[index]+c[index]
    return result

def letter_count(a_str):
    d=dict.fromkeys(a_str,0)
    for cm in a_str:
        d[cm]=d[cm] +1
    return d
