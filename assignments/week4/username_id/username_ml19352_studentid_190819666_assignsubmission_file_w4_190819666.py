def signum(a_num):
    if a_num>0:
        return 1
    if a_num<0:
        return -1
    else:
        return 0

def middle(p1,p2,p3):
    a=(p1,p2,p3)
    b=sorted(a)
    return b[1]

def isa_triangle(len1,len2,len3):
    while len1>0 and len2>0 and len3>0:
        if len1==len2==len3:
            a=print('Equilateral')
            return a
        elif len1==len2 or len1==len3 or len2==len3:
            a=print('Isosceles')
            return a
    while len1!=len2!=len3:
        if len1**2+len2**2>=len3**2:
            a=print('Scalene')
            return a
    else:
        a=print('No triangle possible')
        return a


def robberlingo(a_str):
    consonants='bcdfghklmnpqrstvwxyz'
    a=print("".join(i+'o'+i if i in consonants else i for i in a_str))
    return a

def pangram(a_str):
    x=a_str.replace(' ','')
    s=x.lower()
    alphabet='abcdefghijklmnopqrstuvwxyz'
    for i in alphabet:
        if i not in s:
            return bool(0)

    return bool(1)

def merge2(str1,str2):
    a=list(str1)
    b=list(str2)
    c=a+b
    c[::2]=a
    c[1::2]=b
    x=''.join(c)
    return x

def merge3(str1,str2,str3):
    a=list(str1)
    b=list(str2)
    c=list(str3)
    d=a+b+c
    d[0::3]=a
    d[1::3]=b
    d[2::3]=c
    x=''.join(d)
    return x


def letter_count(a_str):
    result={s:a_str.count(s) for s in a_str}
    return result


    

    


        


    


    

