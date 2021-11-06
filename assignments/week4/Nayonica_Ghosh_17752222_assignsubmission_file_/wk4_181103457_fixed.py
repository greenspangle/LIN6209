def signum(a_num):
	if a_num < 0:
		return -1
	if a_num > 0:
		return 1
	else:
		return 0


def middle(p1, p2, p3):
	my_list=[p1,p2,p3]
	sorted_list=sorted(my_list)
	middle_value=sorted_list[1]
	return middle_value
    

def isa_triangle(len1,len2,len3):
    if len1==len2 and len2==len3:
        return(3)
    elif len1==len2 or len2==len3 or len1==len3:
        return(2)
    else:
        return(3)
    if len1+len2>=len3 and len2+len3>=len1 and len3+len1>=len2:
	    return(0)


 



	    
def robberlingo(a_str):
    consonants = set("bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ")
    ret_str = ""
    for letter in a_str:
        if letter in consonants:
            ret_str += letter + ("o" if letter.islower() else "O") + letter
        else:
            ret_str += letter
    return ret_str



    
def pangram(a_str):
	
    a_str = a_str.replace(' ','')
    
    a_str = a_str.lower()
    
    s=set(a_str)
    l=list(s)
    if len(l)==26:
        return True
    else:return False



def merge2(str1,str2):
    s1= (str1)
    s2= (str2)
    # s=  s = "".join([s1[i] + s2[i] for i in range(len(s1))]) + s2[len(s1):]
    s = "".join([s1[i] + s2[i] for i in range(len(s1))])
    # print(s)
    return s


def merge3(str1,str2,str3):
    s1= (str1)
    s2= (str2)
    s3= (str3)
    # s = s = "".join([s1[i] + s2[i] + s3[i] for i in range(len(s1))]) + s2[len(s1) + s3[len(s2):]
    s = "".join([s1[i] + s2[i] + s3[i]  for i in range(len(s1)) ])
    # print (s)
    return s
                                                                            





def letter_count(a_str):
    ddict = {}
    for n in a_str:
        keys = ddict.keys()
        if n in keys:
            ddict[n] += 1
        else:
            ddict[n] = 1
    return ddict


