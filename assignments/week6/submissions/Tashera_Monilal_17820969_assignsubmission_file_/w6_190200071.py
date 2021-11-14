def num_seq_str(an_int):
    result = ""
    for i in range(1,an_int +1):
        result += str(i) + ','
        #print("".strip())
    return result
#Still couldnt figure out how to get rid of the comma

def fizzbuzz(an_int):
    if an_int%15==0:
        return 'FizzBuzz'
    elif an_int%3==0:
        return 'Fizz'
    elif an_int%5==0:
        return 'Buzz'
    else:
        return str(an_int)

def thermostat(temperature):
    if temperature < 19:
        return 'on'
    elif temperature > 24:
        return 'off'
    else:
        return 'stat'

def char_frequency(filename):
    result = dict()
    with open(filename,'r', encoding = 'utf-8') as f:
        content = f.read().lower()
        for char in content:
            if value == result[char]:
                result[char]=value+1
            else:
                result[char]=1
    return result


def count_Q(filename):
    with open(filename,'r', encoding='utf-8') as f:
        content = f.read().lower()
        count=content.count('?')
        return count

def count_and(filename):
    with open(filename, 'r', encoding = 'utf-8') as f:
        content = f.read()
        and1=content.count('and')
        and2=content.count(' and ')
        and3=content.count('  and,  ')
    return content.count

def get_chars_set(filename):
    with open (filename, 'r',encoding = 'utf-8') as f:
        content = f.read()
        return set(content)

def num_seq_list(an_int):
    result=[]
    for i in range(1,an_int +1):
        result.append(i)
        return result

def num_seq_set(an_int):
    result=set()
    for i in range(1,an_int+1):
        return set(result)

def num_seq_dict(an_int):
    result=dict()
    for i in range(1,an_int+1):
        result.append(i)
        return result




