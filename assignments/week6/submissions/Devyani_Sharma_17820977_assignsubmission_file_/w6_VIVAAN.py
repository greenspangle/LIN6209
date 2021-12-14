def thermostat(temperature):
    if temperature < 19:
        heat = 'on'
    elif temperature > 24:
        heat = 'off'
    else:
        heat = 'stat'
    return heat

def score_2(dice_1, dice_2):
    if dice_1 == dice_2 == 6:
        score = dice_1 + dice_2 + dice_1 + dice_2
    elif dice_1 == dice_2:
        score = dice_1 + dice_2 + dice_1
    elif dice_1 + dice_2 == 7:
        score = (dice_1 + dice_2) * 2
    else:
        score = dice_1 + dice_2
    return score

def score_4(red1, red2, blue1, blue2):
    if sorted([red1, red2, blue1, blue2]) == [3, 3, 4, 4]:
        score = 21
    elif (red1 + blue1) == 7 and (red2 + blue2) == 7 or (red1 + blue2) == 7 and (red2 + blue1) == 7:
        score = 14
    elif (red1 + blue1) == 7 or (red1 + blue2) == 7 or (red2 + blue1) == 7 or (red2 + blue2) == 7:
        score = 7
    else:
        score = min([red1, red2, blue1, blue2])
    return score

def fizzbuzz(an_int):
    if an_int % 15 == 0:
        return 'FizzBuzz'
    elif an_int % 3 == 0:
        return 'Fizz'
    elif an_int % 5 == 0:
        return 'Buzz'
    else:
        return str(an_int)

def num_seq_str(an_int):
    count = 0
    string = ''
    if an_int != 1:
        for i in range(an_int):
            string += str(count + 1)
            if (count + 1) != an_int:
                string += ", "
            else:
                string += ""
            count += 1
    else:
        string = '1'
    return string

def num_seq_list(an_int):
    count = 0
    thelist = []
    for i in range(an_int):
        thelist.append(count + 1)
        count += 1
    return thelist

def num_seq_set(an_int):
    count = 0
    theset = set()
    for i in range(an_int):
        theset.add(count + 1)
        count += 1
    return theset

def num_seq_dict(an_int):
    count = 0
    thedict = dict()
    for i in range(an_int):
        thedict[count + 1] = fizzbuzz(count + 1)
        count += 1
    return thedict

def get_chars_set(filename):
    setofchars = set()
    with open(filename, 'r') as f:
        for line in f.readlines():
            for char in line:
                if char not in setofchars:
                    setofchars.add(char)
    return sorted(setofchars)

def count_chars(filename):
    lenofchars = 0
    with open(filename, 'r') as f:
        for line in f.readlines():
            for char in line:
                lenofchars += 1
    return lenofchars

def count_Q(filename):
    lenofq = 0
    with open(filename, 'r') as f:
        for line in f.readlines():
            for char in line:
                if char == '?':
                    lenofq += 1
    return lenofq

def count_words(filename):
    word_list = list()
    words = 0
    with open(filename, 'r') as f:
        for line in f.readlines():
            word_list += line.split()
    words = len(word_list)
    return words

def char_frequency(filename):
    dictofchars = dict()
    with open(filename, 'r') as f:
        for line in f.readlines():
            for char in line:
                if char not in dictofchars:
                    dictofchars[char] = 1
                else:
                    dictofchars[char] += 1
    return dictofchars

def word_frequency(filename):
    dictofwords = dict()
    with open(filename, 'r') as f:
        for line in f.readlines():
            line = line.strip().lower()
            words = line.split(" ")
            for word in words:
                if word in dictofwords:
                    dictofwords[word] = dictofwords[word] + 1
                else:
                    dictofwords[word] = 1
    return dictofwords

def write_Q(an_int, filename):
    chars = 0
    with open(filename, 'w') as f:
        for i in range(an_int):
            if i + 1 != an_int:
                f.write(str(i + 1) + " ? ")
            else:
                f.write(str(i + 1))
    f.close()
    with open(filename, 'r') as f:
        for line in f.readlines():
            for char in line:
                chars += 1
    return chars    

def write_ints(an_int, filename):
    with open(filename, 'w') as f:
        for i in range(an_int):
            for q in range(i + 1):
                if q != i:
                    f.write(str((q + 1) * (i + 1)) + ' ')
                else:
                    f.write(str((q + 1) *  (i + 1)))
                    f.write('\n')
                    pass
