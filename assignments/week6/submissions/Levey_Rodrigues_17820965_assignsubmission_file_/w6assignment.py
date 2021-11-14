def thermostat(temperature):
    if (temperature < 19):
        return'on'

    if (temperature > 24):
        return 'off'

    else:
        return 'stat'

def fizzbuzz (an_int):
    result = str(an_int)
    if (an_int % 3) == 0:
        result = 'Fizz'

    if(an_int % 5) == 0:
        result = 'Buzz'

    if (an_int % 15) == 0:
        result = 'Fizzbuzz'

    return result

def score_2(dice_1, dice_2):
    result = sum = (dice_1 + dice_2)
    
    if (dice_1 == 6 and dice_2 == 6):
        return 24
    if (dice_1 == dice_2):
        result = sum + (dice_1) or (dice_2)
        return result
    if (dice_1 + dice_2) == 7:
        return 14

    return result

def score_4(red1, red2, blue1, blue2):
    result = min(red1, red2, blue1, blue2)

    if red1 + blue1 == 7 and red2 + blue2 == 7 or red1 + blue2 == 7 and red2 + blue1 == 7:
        return 14

    if red1 + blue1 == 7 or red2 + blue2 == 7 or red2 + blue1 == 7 or red1 + blue2 == 7:
        return 7

    
    return result
    

def num_seq_str(an_int):
    #sequence
    a = str()
    for i in range(an_int):
        a = a + str(1 + i) + ',' + ' '
    return a[:-2]

def num_seq_list(an_int):
    b_list = []
    for i in range(an_int):
        b = b_list.append(1 + i)
    return b_list

def num_seq_set(an_int):
    c_set = {}
    for i in range(an_int):
        c = (1 + i)
        d = c_set.union(c)
    return (d)
        
def write_Q(an_int, filename):
    with open("file.txt", "w") as a:
        a = str()
    for i in range(an_int):
        a = a + str(1 + i) + ' ' + '?' + ' '
    az = (a[:-3])
    for char in az:
        return len(az)

def get_chars_set(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
        for char in content:
            return set(char)
      

   
    
