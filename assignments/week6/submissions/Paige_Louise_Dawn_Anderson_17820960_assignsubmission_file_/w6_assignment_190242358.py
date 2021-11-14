''' W6 Assignment'''

def thermostat(temperature):
    if temperature > 24:
        return 'off'
    if temperature < 19:
        return 'on'
    else:
        return 'stat'


def score_2(dice_1, dice_2):
    if dice_1 + dice_2==7:
        sum = 14
        return sum
    if dice_1 == dice_2 != 6:
        sum = dice_1*3
        return sum
    if dice_1==6==dice_2:
        sum = (dice_1 == dice_2)*2
        return sum
    else:
        sum = dice_1 + dice_2
        return sum

    
def score_4(red1, red2, blue1, blue2):
    s =  (red1, red2, blue1, blue2)
    a = sorted (s)

    if red1 + blue2 ==7 and red2+ blue1 !=7:
        return 7
    
    if red1 + blue1 == 7 and red2 + blue2 != 7:
        return 7
    
    if red1 + blue1 != 7 and red2+blue2==7:
        return 7
    
    if red1+blue2!=7 and red2+blue1==7:
        return 7
    
    while red1+blue1 ==7 and red2 +blue1 ==7:
        if s.count (3) ==2 and s.count(4)==2:
            return 21
        else:
            return 14
        
    while red1+blue2 ==7 and red2+blue1 ==7:
        if s.count(3) ==2 and s.count (4)==2:
            return 21
        else:
            return 14
    else:
        return a [0]
    

def fizzbuzz (an_int):
    while an_int % 3==0:
        if an_int% 3==0 and an_int % 5!=0:
            return 'Fizz'
        else:
            return 'FizzBuzz'
    while an_int % 5==0:
        if an_int % 5 ==0 and an_int %3 !=0:
            return 'Buzz'
        else:
            return 'FizzBuzz'
    else:
        return an_int


def num_seq_str (an_int): # space after 5
    result = ""
    for i in range(1, an_int + 1):
        result += str(i)+", "
    return result


def num_seq_list (an_int):
    a = list (i for i in range (1, an_int + 1))
    return a


def num_seq_set(an_int):
    a = set (i for i in range (1, an_int + 1))
    return a


def num_seq_dict_(an_int): 
    my_dict= dict()
    for i in range(1, an_int+1):
        my_dict[i] = fizzbuzz (i)
    return my_dict


def get_chars_set(filename): 
    with open(filename, 'r', encoding='utf-8') as f:  
        content = f.read()
        a = set(content)
        return a


def count_chars(filename):
    with open(filename, 'r', encoding='utf-8') as f:  
        content = f.read()
        a = len (content)
        return a


def count_Q(filename):
    with open(filename, 'r', encoding='utf-8') as f:  
        content = f.read()
        str = content
        sub = '?'
        a= str.count(sub)
        return a


def count_and(filename):
    with open(filename, 'r', encoding='utf-8') as f:  
        content = f.read().lower()
        str = content
        sub1 = 'and'
        sub2 = ' and '
        sub3 = ' and, '
        a1= str.count(sub1)
        b1= str.count(sub2)
        c1= str.count(sub3)
        return a,b,c


def count_words(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read().lower()
        accepted= 'abcdefghijklmnopqrstuvwxyz1234567890'
        for i in content:
            if i not in accepted:
                content.replace(i,'')
        words = content.split()
        return len(words)

def char_frequency(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
        d = {}
        for i in content:
            d[i] = d.get(i,0)+1
    return d


def word_frequency(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read().lower()
        words = content.split()
        d = {}
        for i in words:
            d[i] = d.get(i,0)+1
    return d

def text_analysis_01(filename): #look at sent and non ws
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
        #sentence_count = 0
        for i in content:
            
            ws_char = len (content)
        non_ws_char = ws_char - words
        words = len (content.split())

    return sent, words, ws_char, non_ws_char
    

def write_Q(an_int, filename):
    with open(filename, 'w', encoding='utf-8') as f:
        result = ""
        for i in range(1, an_int + 1):
            if i == an_int:
                 result += str(i)
            else:
                 result += str(i) + " ? "
        f.write(result)
        return len (result)


def write_ints(an_int, filename): #g
    pass
