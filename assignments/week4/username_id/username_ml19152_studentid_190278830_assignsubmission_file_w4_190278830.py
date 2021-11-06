def signum(a_num):
    if a_num > 0:
        signum = 1
    elif a_num < 0:
        signum = -1
    else:
        signum = 0
    return signum


def middle(p1, p2, p3):
    my_list = [p1, p2, p3]
    sorted_list = sorted(my_list)
    middle_value = sorted_list[1]
    return middle_value


def isa_triangle(len1, len2, len3):
     if (len1 == len2 and len2 == len3):
          triangle = 3
     elif (len1 == len2 and len2 == len3 or len1 == len3):
          triangle = 2
     elif (len1 + len2 < len3 or len1 + len3 < len2 or len2 + len3 < len1) :
          triangle = 0

     else:
          triangle = 1
     return triangle
    
def robberlingo(a_str):
     consonants = 'bcdfghjklmnpqrstvwxyz'
     translation = ''
     for char in a_str:
          if (char in consonants):
               translation += char
               translation += 'o'
               translation += char
          else:
               translation += char
     return translation


def pangram(a_str):
   alphabet = "abcdefghijklmnopqrstuvwxyz"
   for char in alphabet:
      if char not in a_str.lower():
         return False
   return True


def merge2(str1, str2):
     result = ''
     for i in range(len(str1)):
          result += str1[i] + str2[i]
     return result

    
def merge3(str1, str2, str3):
     result = ''
     for i in range(len(str1)):
          result += str1[i] + str2[i] + str3[i]
     return result



def letter_count(a_str):
     character_set = set(a_str)
     dictionary = {}

     for character in character_set:
          dictionary[character] = a_str.count(character)

          for character in dictionary:
               return {character : dictionary[character]}
     



