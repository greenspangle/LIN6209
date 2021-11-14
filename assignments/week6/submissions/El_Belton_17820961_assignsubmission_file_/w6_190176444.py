def thermostat(temperature):
    if temperature < 19:
        return('on')
    elif temperature > 24:
        return('off')
    else:
       return('stat')

def score_2(dice_1, dice_2):
    if dice_1 == dice_2:
        score = (dice_1 + dice_2) + dice_1
    elif dice_1 == 6 and dice_2 == 6:
        score = (dice_1 + dice_2) + (dice_1 + dice_2)
    elif dice_1 + dice_2 == 7:
        score = (dice_1 + dice_2) + (dice_1 + dice_2)
    else:
        score = dice_1 + dice_2
    return score

def score_4(red1, red2, blue1, blue2):
    if red1 + blue1 == 7 or red1 + blue2 == 7 or red2 + blue1 == 7 or red2 + blue2 == 7:
        score = 7
    elif (red1 + blue1 == 7 and red2 + blue2 == 7) or (red2 + blue1 == 7 and red1 + blue2 == 7):
        score = 14
    elif (red1 == 3 and red2 == 3 and blue1 == 4 and blue2 == 4) or (red1 == 3 and red2 == 4 and blue1 == 3 and blue2 == 4) or (red1 == 3 and red2 == 4 and blue1 == 4 and blue2 == 3) or (red1 == 4 and red2 == 3 and blue1 == 3 and blue2 == 4) or (red1 == 4 and red2 == 3 and blue1 == 4 and blue2 == 3) or (red1 == 4 and red2 == 4 and blue1 == 3 and blue2 == 3):
        score = 21
    else:
        list = [red1, red2, blue1, blue2]
        list.sort()
        score = list[0]
    return score

def fizzbuzz(an_int):
    if an_int % 15 == 0:
        return str('Fizzbuzz')
    elif an_int % 5 == 0:
        return str('Buzz')
    elif an_int % 3 == 0:
        return str('Fizz')
    else:
        return str(an_int)

def num_seq_str(an_int):
    count = 0
    seq = ''
    while (count < an_int):
        count = (count + 1)
        seq = seq + str(count) + ', '
        sequence = seq.rstrip(', ')
    return sequence
        
def num_seq_list(an_int):
    count = 0
    list = []
    while count < an_int:
        count = count + 1
        list.append(count)
    return list

def num_seq_set(an_int):
    count = 0
    list1 = []
    while count < an_int:
        count = count + 1
        list1.append(count)
    set1 = set(list1)
    return set1

def num_seq_dict(an_int):
    count = 0
    dict1 = {}
    while count < an_int:
        count = count + 1
        if count % 15 == 0:
            value = 'Fizzbuzz'
        elif count % 5 == 0:
            value = 'Buzz'
        elif count % 3 == 0:
            value = 'Fizz'
        else:
            value = str(count)
        dict1.update({count: str(value)})
    return(dict1)

def get_chars_set(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
        chars = set(content)
        return chars

def count_chars(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
        return len(content)

def count_Q(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
        count = 0
        for char in range(len(content)):
            if (content[char]=='?'):
                count = count + 1
        return count

def count_and(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
        a = content.count('and')
        b = content.count(' and ')
        c = content.count('and, ')
        return a,b,c

def count_words(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
        lines = content.split()
        wordcount = len(lines)
        return wordcount  

def char_frequency(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
        char_dict = dict()
        for line in content:
            line = line.strip()
            line = line.lower()
            chars = line.split()
            for char in chars:
                if char in char_dict:
                    char_dict[char] = char_dict[char] + 1
                else:
                    char_dict[char] = 1
        return char_dict

def word_frequency(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
        word_dict = {}
        punctuation = '''!"£$%^&*()-_=+{[}]:;@'~#<,>.?/|\¬'''
        for line in content:
            line = content.lower()
            line = content.translate(content.maketrans("", "", punctuation))
        for word in line.lower().split():
            if word not in word_dict:
                word_dict[word] = 1
            else:
                word_dict[word] = word_dict[word] + 1
        return word_dict

def text_analysis_01(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
        sentence_count = 0
        lines = content.split()
        word_count = len(lines)
        characters = content.strip()
        char_count = len(characters)
        whitespace_count = (len(content)) - (len(characters))
        for char in range(len(content)):
            if (content[char]=='?') or (content[char]=='!') or (content[char]=='.'):
                sentence_count = (sentence_count + 1)
            else:
                sentence_count = sentence_count
        return (sentence_count, word_count, char_count, whitespace_count)

def write_Q(an_int, filename):
    with open(filename, 'w') as f:
        content = f.write('')
        count = 0
        seq = ''
        while (count < an_int):
            count = count + 1
            seq = seq + str(count) + ' ? '
            sequence = seq.rstrip(' ? ')
        content = sequence
        char_count = len(content)
        return char_count

def write_ints(an_int, filename): #could'nt work out
    with open(filename, 'r') as f:
        content = f.read()
        count = 0
        while count < an_int:
            count = (count + 1)
            while count < an_int:
                f.write(str((count) + ' ' + ((count + count))) + '/n')
        return f.read() 
