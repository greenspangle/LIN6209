def signum(a_num):
    if a_num >0:
        return 1
    if a_num <0:
        return -1
    else:
        return 0

def middle(p1,p2,p3):
    list = [p1,p2,p3]
    list.sort()
    return (list[1])

def isa_triangle(len1,len2,len3):
        if len1 <= 0 or len2 <= 0 or len3 <= 0:
            return 0
        elif len1 == len2 and len2 == len3:
            return 3
        elif (len1 == len2 and len3 != len2) or (len1 == len3 and len2 != len3) or (len2 == len3 and len2 != len1):
            return 2
        elif len1 != len2 and len2 != len3 and len3 != len1:
            return 1
        else:
            return 0

def robberlingo(a_str): #returns in looping segments rather than a single string
    """double every consonant and put an 'o' in between"""
    vowels = 'aeiou'
    consonants = 'bcdfghjklmnpqrstvwxyz'
    translation = ['']
    while len(a_str) >= 1:
        for current_char in a_str:
            translation = (current_char)
            if current_char in consonants:
                input(current_char + 'o' + current_char) in translation
            else:
                input(current_char) in translation
        if current_char not in a_str:
            return str(translation)
   
def merge2(str1,str2): #doesn't loop
   """Print the first and last characters of each string successively"""
   result_str = ''
   length_of_str = len(str1)
   for index in range(length_of_str):
      result_str =(str1[index] + str2[index])
      if len(str1) < 1:
          break
      return result_str
    
def merge3(str1,str2,str3): #doesn't loop
    """Print the first and last characters of each string successively"""
    result_str = ''
    length_of_str = len(str1)
    for index in range(length_of_str):
        result_str = (str1[index] + str2[index] + str3[index])
        if len(str1) < 1:
            break
        return result_str

def pangram(a_str):
    if 'a'and'b'and'c'and'd'and'e'and'f'and'g'and'h'and'i'and'j'and'k'and'l'and'm'and'n'and'o'and'p'and'q'and'r'and's'and't'and'u'and'v'and'w'and'x'and'y'and'z' in a_str:
        return True
    else:
        return False

def letter_count(a_str): #returning Nones/0
    """Return dictionary counting up every character in a string with a tally"""
    string = list(a_str)
    char_count_dict = dict.fromkeys(a_str, 0)
    for char in string:
        if char in {}:
            char_count_dict[1] += 1
        else:
            char_count_dict[1] = 1
    return char_count_dict
    
