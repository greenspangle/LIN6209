def count_words(filename):

    with open(filename, 'r', encoding='utf-8') as f:

        content = f.read().lower()

        content = content.replace('\t', '')

        content = content.replace('\n', '')

        content = content.replace('\r', '')

        words = content.split()

        return len(words)





def char_frequency(filename):

    with open(filename, 'r', encoding='utf-8') as f:

        content = f.read().lower()

        ddict = {}

        for char in content:

            if char in ddict:

                ddict[char] += 1

            else:

                ddict[char] = 1

        return ddict





def word_frequency(filename):

    with open(filename, 'r', encoding='utf-8') as f:

        content = f.read().lower()

        content = content.replace('\t', '')

        content = content.replace('\n', '')

        content = content.replace('\r', '')

        content = content.replace('?', '')

        content = content.replace('!', '')

        content = content.replace(',', '')

        content = content.replace('.', '')

        words = content.split()

        ddict = dict()

        for word in words:

            if word in ddict:

                ddict[word] += 1

            else:

                ddict[word] = 1

        return ddict





def thermostat(temperature):

    if (temperature) < 19:

        return 'on'

    if (temperature) > 24:

        return 'off'

    else:

        return 'stat'





def score_2(dice_1, dice_2):

    a = (dice_1)

    b = (dice_2)

    if a != 6 and b != 6 and a == b and b == a:

        return (2*a) + b

    if a == 6 and b == 6:

        return 24

    if (a+b == 7):

        return 14

    else:

        return (a+b)





def fizzbuzz(an_int):

    if (an_int) % 3 == 0 and (an_int) % 5 == 0:

        return 'FizzBuzz'

    elif (an_int) % 3 == 0:

        return 'Fizz'

    elif (an_int) % 5 == 0:

        return 'Buzz'

    else:

        return str(an_int)





def num_seq_str(an_int):

    result = ""

    for i in range(1, an_int+1):

        if i == (an_int):

            result += str(i)

        else:

            result += str(i)+', '

    return result





def num_seq_list(an_int):

    result = []



    for i in range(1, an_int+1):

        result.append(i)



    return result





def num_seq_set(an_int):

    result = []

    for i in range(1, an_int+1):

        result.append(i)

    return set(result)





def num_seq_dict_(an_int):

    result = dict()

    for i in range(1, an_int+1):

        value = fizzbuzz(i)

        result[i] = value

    return result





def get_chars_set(filename):

    filename = (filename)

    with open(filename, 'r', encoding='utf-8') as f:

        content = f.read().lower()

        return set(content)





def count_chars(filename):

    with open(filename, 'r', encoding='utf-8') as f:

        content = f.read().lower()

        return len(content)





def count_Q(filename):

    with open(filename, 'r', encoding='utf-8') as f:

        content = f.read().lower()

        count = content.count('?')

    return count





def count_and(filename):

    with open(filename, 'r', encoding='utf-8') as f:

        content = f.read().lower()

        and1 = content.count("and")

        and2 = content.count(" and ")

        and3 = content.count(" and, ")

        return(and1, and2, and3)





def write_Q(an_int, filename):

    with open(filename, "w", encoding="utf-8") as f:

        result = ""

        for i in range(1, an_int+1):

            if i == an_int:

                result += str(i)

            else:

                result += str(i) + " ? "

        f.write(result)

        return len(result)





# def score_4(red1, red2, blue1, blue2):

        #a= (red1)

        #b= (red2)

        #c= (blue1)

        #d= (blue2)

        # if a+c==7 or a+d==7 or b+c==7 and b+d==7:

        # return 7

        # if a+c==7 and b+d==7 and a+d==7 and b+c==7:

        # return 14

        # if a==3 and b==3 and c==4 and c==4:

        # return 21

        # if c==3 and d==3 and a==4 and b==4 or a==3 and b==4 and c==4 and d==3 and a==4 and b==3:

        # return 21



        # else:

        # return lowest number

