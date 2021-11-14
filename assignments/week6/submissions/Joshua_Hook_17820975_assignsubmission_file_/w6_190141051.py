def thermostat(temperature):
    if temperature < 19:
        return "on"
    if temperature > 24:
        return "off"
    else:
        return "stat"

def score_2(dice_1, dice_2):
    if dice_1 + dice_2 == 7:
        return (dice_1 + dice_2) * 2
    elif dice_1 == 6 and dice_2 == 6:
        return dice_1 * 4
    elif dice_1 == dice_2:
        return dice_1 * 3
    else:
        return dice_1 + dice_2

def score_4(red1, red2, blue1, blue2):
    dice_list = [red1, red2, blue1, blue2]
    if sorted(dice_list) == [3,3,4,4]:
        return 21
    elif (red1 + blue1 == 7 and red2 + blue2 == 7) or (red1 + blue2 == 7 and red2 + blue1 == 7):
        return 14
    elif red1 + blue1 == 7 or red1 + blue2 == 7 or red2 + blue1 == 7 or red2 + blue2 == 7:
        return 7
    else:
        return min(dice_list)

def fizzbuzz(an_int):
    if an_int % 15 == 0:
        return "FizzBuzz"
    elif an_int % 5 == 0:
        return "Buzz"
    elif an_int % 3 == 0:
        return "Fizz"
    else:
        return str(an_int)

def num_seq_str(an_int):
    seq_str = ""
    for i in range(1, an_int+1):
        seq_str = seq_str + str(i)
        if i != an_int:
            seq_str = seq_str + ", "
    return seq_str

def num_seq_list(an_int):
    seq_list = []
    for i in range(1, an_int+1):
        seq_list.append(i)
    return seq_list

def num_seq_set(an_int):
    seq_set = set()
    for i in range(1, an_int+1):
        seq_set.add(i)
    return seq_set

def num_seq_dict(an_int):
    seq_dict = dict()
    for i in range(1, an_int+1):
        seq_dict[i] = fizzbuzz(i)
    return seq_dict

def get_chars_set(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
        return set(content)

def count_chars(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
        return len(content)

def count_Q(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
        return content.count("?")

def count_and(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
        content = content.lower()
        return content.count("and"), content.count(" and "), content.count(" and, ")

def count_words(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
        words = content.split()
        return len(words)

def char_frequency(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
    chars_dict = dict.fromkeys(set(content), 0)
    for char in chars_dict.keys():
        chars_dict[char] = content.count(char)
    return chars_dict

def word_frequency(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
        words = content.split()
        words_dict = dict.fromkeys(words, 0)
        for word in words_dict.keys():
            words_dict[word] = content.count(word)
        return words_dict

def text_analysis_01(filename):
    def count_sentences(filename):
        import re
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
            sentences = re.split("\. |\? |\! ", content)
            return len(sentences)

    def count_non_ws(filename):
        count = 0
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
            text = str(content)
            for char in text:
                if char.isspace() == False:
                    count = count + 1
            return count

    def count_ws(filename):
        count = 0
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
            text = str(content)
            for char in text:
                if char.isspace() == True:
                    count = count + 1
            return count
        
    return count_sentences(filename), count_words(filename), count_non_ws(filename), count_ws(filename)

def write_Q(an_int, filename):
    with open(filename, 'w+', encoding='utf-8') as f:
        for i in range(1, an_int+1):
            f.write(str(i))
            if i != an_int:
                f.write(" ? ")
    return count_chars(filename)


def write_ints(an_int, filename):
    with open(filename, 'w', encoding='utf-8') as f:
        for i in range(1, an_int+1):
            for j in range (1, i+1):
                f.write(str(i*j))
                if j != i:
                    f.write(" ")
            if i != an_int:
                f.write("\n")
