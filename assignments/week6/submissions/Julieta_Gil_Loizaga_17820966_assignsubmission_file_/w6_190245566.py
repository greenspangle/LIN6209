def thermostat(temperature):
    
    setting = ''

    if temperature >24:
        setting = 'off'
    elif temperature < 19:
        setting = 'on'
    else:
        setting = 'stat'

    return setting



def score_2(dice_1, dice_2):

    score = dice_1 + dice_2
    
    if dice_1 + dice_2 == 7:
        score = 14
    elif dice_1 == 6 and dice_2 == 6:
        score = 24
    elif dice_1 == dice_2:
        score = dice_1 + dice_2 * 2

    return score




def score_4(red1,red2,blue1,blue2):

    dice_list = [red1, red2, blue1, blue2]

    if dice_list.count(3)==2 and dice_list.count(4)==2:
        score = 21
    elif red1+blue1 == 7 and red2+blue2 == 7:
        score = 14
    elif red1+blue2 == 7 and red2+blue1 == 7:
        score = 14
    elif red1+blue1 == 7 or red1+blue2 == 7 or red2+blue1 == 7 or red2+blue2 == 7:
        score = 7
    else:
        score = min(red1,red2,blue1,blue2)

    return score



def fizzbuzz(an_int):

    value = ''

    if an_int % 15 == 0:
        value = 'FizzBuzz'
    elif an_int % 5 == 0:
        value = 'Buzz'
    elif an_int % 3 == 0:
        value = 'Fizz'
    else:
        value = str(an_int)

    return value



def num_seq_str(an_int):

    seq = []

    for i in range(an_int +1):
        seq.append(i)
        seq.append(', ') 

    del seq[0:2]
    del seq[-1]
    
    seq_s = ''
    
    for i in seq:
        seq_s += str(i)
    
    return seq_s



def num_seq_list(an_int):

    seq = []

    for i in range(an_int +1):
        seq.append(i)

    del seq[0]

    return seq



def num_seq_set(an_int):

    return set(num_seq_list(an_int))



def num_seq_dict(an_int):

    d = {}

    for i in num_seq_list(an_int):
        d[i] = fizzbuzz(i)


    return d



def get_chars_set(filename):

    with open(filename,'r',encoding='utf-8') as f:
        content = f.read()

    return set(content)


def count_chars(filename):

    return len(get_chars_set(filename))



def count_Q(filename):

    with open(filename,'r',encoding='utf-8') as f:
        content = f.read()    

    return content.count("?")



def count_and(filename):

    with open(filename,'r',encoding='utf-8') as f:
        content = f.read()

    return content.count('and'),content.count(' and '), content.count(' and, ')



def count_words(filename):
    
    import re
    
    with open(filename,'r',encoding='utf-8') as f:
        content = f.read()

        content = re.sub(r'[^\w\s]','',content)
        w = re.findall("(\S+)", content)
        

    return len(w)

def char_frequency(filename):

    with open(filename,'r',encoding='utf-8') as f:
        content = f.read()

        d ={}

        for i in list(content):
            if i not in d.keys():
                d[i] = 1
            else:
                d[i] = d[i]+1

    return d



def word_frequency(filename):

    import re
    
    with open(filename,'r',encoding='utf-8') as f:
        content = f.read().lower()

        content = re.sub(r'[^\w\s]','',content)
        w = re.findall("(\S+)", content)

        d={}
        for i in w:
            if i not in d.keys():
                d[i] = 1
            else:
                d[i] = d[i]+1

    return d

        

def average_word_length(filename):

    words = word_frequency(filename).keys()
    sum_len = 0
    wordcount = count_words(filename)

    for w in words:
        sum_len = sum_len+len(w)

    return sum_len/wordcount



def text_analysis_01(filename):
    
    words = count_words(filename)       #number of words

    with open(filename,'r',encoding='utf-8') as f:      #reading file
        content = f.read()

        sentences = len(content.split('. ')) +1         #number of sentences


        non_w_char = 0                  #counting characters
        w_char = 0

        for i in content:                   
            if i.isspace()==True:
                w_char = w_char+1

            else:
                non_w_char = non_w_char+1
    

    return sentences, words, non_w_char, w_char
    
    
    

def write_Q(an_int, filename):

    #the sequence to write onto the file
    seq = []

    for i in range(an_int +1):
        seq.append(i)
        seq.append(' ? ') 

    del seq[0:2]
    del seq[-1]
    
    seq_s = ''
    
    for i in seq:
        seq_s += str(i)

    #writing to file        
    with open(filename,'w',encoding='utf-8') as f:
        f.write(seq_s)
        f.close()

    #count chars
    with open(filename,'r',encoding='utf-8') as f:
        length = len(f.read())

    return length



def write_ints(an_int, filename):
    
    #sequence of integers, number of lines
    seq = []
    for i in range(an_int+1):
        seq.append(i)
    del seq[0]

    #list of lines to write
    line_list = []

    for i in seq:

        #numbers i need to multiply by
        mult_seq = []
        for x in range(i+1):
            mult_seq.append(x)
        del mult_seq[0]

        #content of each line after multiplications
        for y in mult_seq:
            line.append(i*y)
            line.append(' ')
        del line[-1]

        #transform into a string
        line_s = ''
        for l in line:
            line_s += str(l)

        #add to list of lines to write
        line_list.append(line_s)


    #write into file
    with open(filename,'w',encoding='utf-8') as f:
        f.writelines(line_list)
        f.close()

    #reading to check results
    with open(filename,'r',encoding='utf-8') as f:
        c = f.read()        

    return c












        
