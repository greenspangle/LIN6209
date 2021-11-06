#!/usr/bin/env python
# coding: utf-8

# In[81]:


def signum(a_num):
    if a_num > 0:
        return 1
    elif a_num < 0:
        return -1
    else:
        return 0


# In[82]:


def middle(p1, p2, p3):
    list = [p1,p2,p3]
    list.sort()
    return list[1]


# In[83]:


def isa_triangle(len1, len2, len3):
    if len1 + len2 < len3 or len2 + len3 < len1 or len1 + len3 < len2:
        return 0 #triangle inequality theorem for 4th case
    if len1 == len2 and len2 == len3:
        return 3
    elif len1 == len2 or len2 == len3 or len3 == len1:
        return 2
    elif len1 != len2 and len2 != len3 and len3 != len1:
        return 1


# In[84]:


def robberlingo(a_str):
    vowels = 'aeiou'
    consonants = 'bcdfghjklmnpqrstvwxyz'
    str1 = ''
    for character in a_str:
        if character in consonants:
            str1+=character+'o'+character
        elif character in vowels:
            str1+=character
        elif character == ' ':
            str1+=' '
    return str1


# In[85]:


def pangram(a_str):
    alphabet = 'aeioubcdfghjklmnpqrstvwxyz'
    alphlist = list(alphabet)
    for character in a_str:
        if character in alphlist:
            alphlist.remove(character)
        else:
            next
    if len(alphlist)== 0:
        return True
    return False


# In[86]:


def merge2(str1, str2):
    if len(str1) != len(str2): #question said strings should be same length this is just a check
        return
    string = ''
    for i in range(len(str1)):
        string+=str1[i]
        string+=str2[i]
    return string


# In[87]:


def merge3(str1, str2, str3):
    if len(str1) != len(str2) or len(str1)!=len(str3): #question said strings should be same length this is just a check
        return
    string = ''
    for i in range(len(str1)):
        string+=str1[i]
        string+=str2[i]
        string+=str3[i]
    return string


# In[88]:


def letter_count(a_str):
    dictio = {}
    for character in a_str:
        try:
            dictio[character] = dictio[character] + 1
        except:
            dictio[character] = 1
        
    return dictio


# In[ ]:




