def thermostat(temperature):
    if temperature < 19:
        heat = 'on'
    elif temperature > 24:
        heat = 'off'
    else:
        heat = 'stat'
    return heat


def score_2(dice_1, dice_2):
    if dice_1 == 6 and dice_2 == 6:
        score = (dice_1 + dice_2) + dice_1 + dice_2

    elif dice_1 == dice_2:
        score = (dice_1 + dice_2) + dice_1 or dice_2
        
    elif dice_1 + dice_2 == 7:
        score = dice_1 + dice_2 + dice_1 + dice_2

    else:
        score = dice_1 + dice_2
    
    return score

def score_4(red1, red2, blue1, blue2):
    score = 0
    numb = [red1, red2, blue1, blue2]
    numb.sort()
    if numb == [3,3,4,4]:
        score = 21
    elif red1 + blue2 == 7 or red1 + blue1 == 7:
        if red1 + blue2 == 7 and red2 + blue1 == 7:
            score = 14
        else:
            score = 7
    elif red2 + blue2 == 7 or red2 + blue1 == 7:
        if red2 + blue2 == 7 and red1 + blue1 == 7:
            score = 14
        else:
            score = 7
    else:
        score = numb[0]
    return score
    

def fizzbuzz(an_int):
    if an_int %3 == 0 and an_int %5 == 0:
        value = 'Fizzbuzz'
    elif an_int %5 == 0:
        value = 'Buzz'
    elif an_int %3 == 0:
        value = 'Fizz'
    else:
        value = str(an_int)
    return value

def num_seq_str(an_int):
     sequence = ''
     for i in range(1, an_int + 1):
          sequence += str(i) + ','
     return sequence


def num_seq_list(an_int):
    mylist = []
    for i in range(an_int+1):
         mylist.append(i)
    return mylist


def num_seq_set(an_int):
    myset = []
    for i in range(an_int+1):
         myset.append(i)
    return myset

def num_seq_dict(an_int):
    result = dict()
    for i in range(1, an_int+1):
         value = fizzbuzz(i)
         result[i] = value
    return result

def get_chars_set(filename):
    with open(filename , 'r', encoding='utf-8') as f:
        content = f.read()
    return set([ch for ch in content])

def count_chars(filename):
    with open(filename , 'r', encoding='utf-8') as f:
        chars = f.read()
    return len([ch for ch in chars])

def count_Q(filename):
    with open(filename , 'r', encoding='utf-8') as f:
        chars = f.read()
    return len([ch for ch in chars if ch=='?'])

def count_and(filename):
     with open(filename , 'r', encoding='utf-8') as f:
        chars = f.read()
        count = [0,0,0]
        for x in range(len(chars)):
            if x < len(chars) - 2 and str(chars[x:x+3]).lower() == 'and':
                count[0] += 1
            if x < len(chars) - 4 and str(chars[x:x+5]).lower() == ' and ':
                count[1] += 1
            if x < len(chars) - 2 and str(chars[x:x+6]).lower() == ' and, ':
                count[2] += 1
        return count

def count_words(filename):
    with open(filename , 'r', encoding='utf-8') as f:
        data = f.read()
        words = data.split()
        return len(words)
            
def char_frequency(filename):
    with open(filename , 'r', encoding='utf-8') as f:
        chars = f.read()
        charf = dict()
        for x in chars:
            if x in charf.keys():
                charf[x] += 1
            else:
                charf[x] = 1
        return charf


def word_frequency(filename):
     with open(filename , 'r', encoding='utf-8') as f:
        words = f.read()
        wordfreq = {}
        for word in words.replace(',', ' ').split():
            wordfreq[word] = wordfreq.setdefault(word, 0) + 1
     return wordfreq

def average_word_length(filename):
    word_dict = word_frequency(filename)
    count = 0
    total_leng = 0
    for key, value in word_dict.items():
        count += value
        total_leng += len(key) * value
    return total_leng/count
    
