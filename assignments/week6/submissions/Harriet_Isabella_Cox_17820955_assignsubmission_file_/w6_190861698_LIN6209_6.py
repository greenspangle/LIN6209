""" Week 6 Assignment. This assignment is worth 15% and is due on Nov 14th.
It is formed of two sections, Section 1 has 18 questions and Section 2 has 3
questions that will be awarded as extra credit (only if Section 1 is completed
to a high standard)"""

# Section 1

# Week 6 Assignment Practice
# Section 1

def thermostat(temperature):
    if temperature < 19:
        return 'on'
    if temperature > 24:
        return 'off'
    else:
        return 'stat'
    
def score_2(dice_1,dice_2):
    if dice_1 + dice_2 ==7:
        sum = 14
        return sum
    if dice_1 == dice_2 !=6:
        sum = dice_1*3
        return sum
    if dice_1==6==dice_2:
        sum = (dice_1 == dice_2) *2
        return sum
    else:
        sum = dice_1 + dice_2
        return sum

def score_4(red1,red2,blue1,blue2):
    s = (red1, red2, blue1, blue2)
    if red1 + blue2 == 7 and red2 + blue1!=7:
        return 7
    if red1 + blue1 == 7 and red2 + blue2 !=7:
        return 7
    if red2 + blue2 == 7 and red1 + blue1 !=7:
        return 7
    if red2 + blue1 == 7 and red1 + blue2 != 7:
        return 7
    elif red1 + blue1 ==7 and red2 + blue2 ==7:
        if s.count(3) ==2 and s.count(4) ==2:
            return 21
        else:
            return 14
    elif red1 + blue2 ==7 and red2 + blue1 ==7:
        if s.count(3) == 2 and s.count(4) ==2:
            return 21
        else:
            return 14
    else:
        a = sorted(s)
        return a[0]

def fizzbuzz(an_int):
    if an_int % 3 ==0 and an_int % 5==0:
        return 'FizzBuzz'
    elif an_int % 3==0:
        return 'Fizz'
    elif an_int % 5==0:
        return 'Buzz'
    else:
        return str(an_int)

def num_seq_str(an_int):
    result = ""
    for i in range(1, an_int +1):
        if i == an_int:
            result+= str(i)
        else:
            result += str(i) + ', '
    return result    

def num_seq_list(an_int):
    result = []
    for i in range(1, an_int +1):
        result.append(i)
    return result

def num_seq_set(an_int):
    result = []
    for i in range(1, an_int +1):
       result.append(i)
    return set(result)

def num_seq_dict(an_int):
    result = dict()
    for i in range(1, an_int +1):
        value = fizzbuzz(i)
        result[i] = value
    return result
    
def get_chars_set(filename):
    with open(filename, 'r', encoding = 'utf-8') as f:
        content = f.read()
    return set(content)

def count_chars(filename):
    with open(filename, 'r', encoding = 'utf-8') as f:
        content = f.read()
        result = len(content)
    return result

def count_Q(filename):
    with open(filename, 'r', encoding = 'utf-8') as f:
        content = f.read()
    return content.count('?')

def count_and(filename):
    with open(filename, 'r', encoding = 'utf-8') as f:
        content = f.read()
        and1 = content.count('and')
        and2 = content.count(' and ')
        and3 = content.count(' and, ')
    return (and1, and2, and3)

def count_words(filename):
    with open(filename, 'r', encoding = 'utf-8') as f:
        content = f.read().lower()
        content = content.replace('\n', '')
    return content

def char_frequency(filename):
    result = dict()
    with open(filename, 'r', encoding = 'utf-8') as f:
        content = f.read().lower()
        for char in content:
            if char in result:
                value = result[char]
                result[char] = value +1
            else:
                result[char] = 1
    return result

def word_frequency(filename):
    result = dict()
    with open(filename, 'r', encoding = 'utf-8') as f:
        content = f.read().lower()
        content = content.replace(' ', '')
        for word in content:
            if word in result:
                value = result[word]
                result[word] = value +1
            else:
                result[word] = 1
    return result

def text_analysis_01(filename):
    with open(filename, 'r', encoding = 'utf-8') as f:
        content = f.read()
        sentence_count = 0
        word_count = 0
        character_count = 0
        whitespace_count = 0
        full_stop = content.count('.')
        Q_count = content.count('?')
        exclamation_count = content.count('!')
        sentence_count = full_stop + Q_count + exclamation_count
        word_list = content.split()
        word_count = len(word_list)
        for char in content:
            if char in '\n\t\r\b':
                whitespace_count += 1
            else:
                character_count + 1
    return sentence_count, word_count, character_count, whitespace_count

def write_Q(an_int, filename):
        result = ""
        for i in range (1, an_int+1):
            if i == an_int:
                result+= str(i)
            else:
                result += str(i) + ' ? '
        with open(filename, 'w') as f:
            content = f.write(result)
        with open(filename, 'r') as f:
            content = f.read()
            result = len(content)
        return result

def write_ints(an_int, filename):
    result = ""
    for i in range(1, an_int):
        print(an_int, 'x', i, '=', an_int*i)
    next_integer = an_int +1
    for i in range(next_integer, next_integer*next_integer):
        print(next_integer, 'x', i, '=', next_integer*i)
    with open(filename, 'w') as f:
        content = f.writelines(result)
    return result


# the following in Section 2 are Extra Credit and are NOT part of the assignment,
# if attempted and having completed Section 1 to a good standard, extra credit
# will be awarded

# Section 2
#def adjacency(filename)

#def predict_next(word,filename)

#def pluralizer(a_str)
