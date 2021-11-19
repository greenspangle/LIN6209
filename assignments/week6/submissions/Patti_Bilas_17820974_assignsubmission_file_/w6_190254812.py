# Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)] on win32
# Type "help", "copyright", "credits" or "license()" for more information.
def thermostat (temperature):
    if temperature < 19:
        return 'on'
    elif temperature > 24:
        return 'off'
    return 'stat'

def score_2 (dice_1, dice_2):
    score = dice_1 + dice_2
    if (dice_1 == dice_2 and dice_1 == 6):
        score += dice_1 + dice_2
    elif (dice_1 == dice_2):
        score += dice_1
    elif (dice_1 + dice_2 == 7):
        score *= 2
    return score

def score_4 (red1, red2, blue1, blue2):
    score = 0
    arr = [red1, red2, blue1, blue2]
    arr.sort()
    if arr == [3, 3, 4, 4]:
        score = 21
    elif red1+blue2 == 7 or red1+blue1 == 7:
        if red1+blue2 == 7 and red2+blue1 == 7:
            score = 14
        else:
            score = 7
    elif red2 + blue2 == 7 or red2+blue1 == 7:
        if red2+blue2 == 7 and red1+blue1 == 7:
            score = 14
        else:
            score = 7
    else:
        score =arr[0]
    return score

def fizzbuzz (an_int):
    if an_int == 0:
        return str(an_int)
    elif an_int % 15 == 0:
        return 'FizzBuzz'
    elif an_int % 3 == 0:
        return 'Fizz'
    elif an_int % 5 == 0:
        return 'Buzz'
    else:
        return str(an_int)

    
def num_seq_str(an_int):
    num_seq = ''
    count = 1
    while (count < an_int):
        num_seq += str(count) + ', '
        count += 1
    num_seq =+ str(an_int)
    return num_seq

def num_seq_list(an_int):
    return [i for i in range(1, an_int+1)]

def num_seq_set(an_int):
    return set([i for i in range(1, an_int+1)])

def num_seq_dict(an_int):
    val_dict = dict()
    for i in range(1, an_int+1):
        val_dict[i] = fizzbuzz(i)
    return val_dict
# SyntaxError: invalid syntax
def get_chars_set(filename):
    with open(filename, 'r', encoding= 'utf-8') as f:
        content = f.read()
    return set ([c for c in content])

def count_chars(filename):
    with open(filename, 'r', encoding= 'utf-8') as f:
        chars = f.read()
    return len([c for c in chars])

def count_Q(filename):
    with open(filename, 'r', encoding= 'utf-8') as f:
        chars = f.read()
    return len([c for c in chars if c=='?'])

def count_and(filename):
    with open(filename, 'r', encoding= 'utf-8') as f:
        chars = f.read()
    count = [0,0,0]  ## PMcG assignment symbol was missing
    for i in range(len(chars)):
        if i < len(chars)-2 and str(chars[i:i+3]).lower() == 'and':
            count[0] += 1
        if i <len(chars)-4 and str(chars[i:i+5]).lower() == 'and':
            count[1] += 1
        if i < len(chars)-5 and str(chars[i:i+6]).lower() == 'and':
            count[2] += 1
    return count
# SyntaxError: invalid syntax
def count_words(filename):
    with open(filename, 'r', encoding= 'utf-8') as f:
        chars = f.read()
    count = 0
    if len(chars) !=0:
        for i in range(len(chars)-1):
            if chars[i].isspace() and not chars[i+1].isspace():
                count =+ 1
        if not chars [-1].isspace():
            count +=1
    return count

def char_frequency(filename):
    with open(filename, 'r', encoding= 'utf-8') as f:
        chars = f.read()
    memo = dict()
    for c in chars:
        if c in memo.keys():
            memo[c] += 1
        else:
            memo[c] = 1
    return memo

def word_frequency(filename):
    with open(filename, 'r', encoding= 'utf-8') as f:
        chars = f.read()
    memo = dict()
    i = 0
    word = ''
    while i < len(chars)+1:
        if i < len(chars) and not chars[i].isspace():
            word += chars[i]
        else:
            if word != '':
                if not word in memo.keys():
                    memo[word] = 1
                else:
                    memo[word] += 1
            word = ''
        i += 1

        
def word_frequency(filename):
    with open(filename, 'r', encoding= 'utf-8') as f:
        chars = f.read()
    memo = dict()
    i = 0
    word = ''
    while i < len(chars)+1:
        if i < len(chars) and not chars[i].isspace():
            word += chars[i]
        else:
            if word != '':
                if not word in memo.keys():
                    memo[word] = 1
                else:
                    memo[word] += 1
            word = ''
        i += 1
    return memo

def text_analysis_01(filename):
    with open(filename, 'r', encoding= 'utf-8') as f:
        chars = f.read()
    num_sentences = str(chars).count(". ") + 1
    num_words = count_words(filename)
    total_chars = len(chars)
    num_whitespace = 0
    for i in range(len(chars)):
        if chars[i].isspace(): num_whitespace =+ 1
    num_non_whitespace = total_chars - num_whitespace
    return num_sentences, num_words, num_non_whitespace, num_whitespace

def write_Q(an_int, filename):
    with open(filename, 'w', encoding= 'utf-8') as f:
        str_seq = ''
        if an_int == 1:
            str_seq = '1'
        else:
            for i in range (1, an_int):
                str_seq +=str(i) + '?'
            str_seq += str(an_int)
        f.write(str_seq)
    return len(str_seq)

def write_ints(an_int, filename):
    with open(filename, 'w', encoding= 'utf-8') as f:
        str_seq = ''
        if an_int !=0:
            for i in range (1, an_int+1):
                str_seq += ' ' +str(i)
                j=2
                prod= i*j
                while (j <= i):
                    str_seq += str(prod)
                    j += 1
                    prod = i*j
                    f.write(str_seq)
    return len(str_seq)
