def thermostat(temperature):
    if 19<=temperatscoure<=24:
        return 'stat'
    if temperature<19:
        return 'on'
    if termperature > 24:
        return 'off'

def score_2(dice_1,dice_2):
    if dice_1+dice_2==7:
        sum=14
        return sum
    while dice_1==dice_2:
        if dice_1==dice_2!=6:
            sum=dice_1*3
            return sum
        if dice_1==6==dice_2:
            sum=(dice_1+dice_2)*2
            return sum
    else:
        sum=dice_1+dice_2
        return sum

def score_4(red1,red2,blue1,blue2):
    s=(red1,red2,blue1,blue2)
    if red1+blue2==7 and red2+blue1!=7:
        return 7
    if red1+blue1==7 and red2+blue2!=7:
        return 7
    if red1+blue1!=7 and red2+blue2==7:
        return 7
    if red1+blue2!=7 and red2+blue1==7:
        return 7
    while red1+blue1==7 and red2+blue2==7:
        if s.count(3)==2 and s.count(4)==2:
            return 21
        else:
            return 14
    while red1+blue2==7 and red2+blue1==7:
        if s.count(3)==2 and s.count(4)==2:
            return 21
        else:
            return 14
    else:
        a=sorted(s)
        return a[0]

def fizzbuzz(an_int):
    if an_int%15==0:
        return 'FizzBuzz'
    elif an_int%5==0:
        return 'Buzz'
    elif an_int%3==0:
        return 'Fizz'
    else:
        return an_int

def num_seq_str(an_int):
    n=int(an_int)
    a=[i for i in range(1,n+1)]
    return a

def num_seq_list(an_int):
    n=int(an_int)
    a=set(i for i in range(1,n+1))
    return a

def num_seq_dict_(filename):
    return {i:fizzbuzz(i) for i in range(1,an_int+1)}
        
def get_chars_set(filename):
    with open(filename,encoding='utf-8') as f:
        a=f.read()
        return set(a)
    
def count_chars(filename):
    with open(filename,encoding='utf-8') as f:
        a=f.read()
        return len(a)

def count_Q(filename):
    with open(filename,encoding='utf-8') as f:
        a=f.read()
        return a.count('?')

def count_and(filename):
    with open(filename,encoding='utf-8') as f:
        a=f.read().lower()
        return a.count('and'),a.count(' and'),a.count(' and, ')

def count_words(filename):
    with open(filename,encoding='utf-8') as f:
        a=f.read().lower()
        accepted_chars='abcdefghijklmnopqrstuvwxyz1234567890 'and '\t','\n','\cr'
        for i in a:
            if i not in accepted_chars:
                a.replace(i,'')
        return len(a.split())

def char_frequency(filename):
    with open(filename,encoding='utf-8') as f:
        a=f.read()
        return {i:a.count(i) for i in set(a)}

def word_frequency(filename):
    with open(filename,encoding='utf-8') as f:
        a=f.read()
        return {word:a.count(word) for word in set(a.split())}

def average_word_length(filename):
    with open(filename,encoding='utf-8') as f:
        a=f.read().lower()
        b=a.split()
        if not b:
            return 0
        else:
            return sum([len(word) for word in b])/len(b)

def text_analysis_01(filename):
    with open(filename,encoding='utf-8') as f:
        a=f.read().lower()
        sens_count=a.count('.')
        accepted_chars='abcdefghijklmnopqrstuvwxyz1234567890 'and '\t','\n','\cr'
        for i in a:
            if i not in accepted_chars:
                s=a.replace(i,'')
                words_count=len(s.split())
                nonwhite_count=a.count(i for i in a not in accepted_chars)
                white_count=len(a)-nonwhite_count
    return sens_count,words_count,nonwhite_count,white_count

def write_Q(an_int, filename):
    with open(filename,'w',encoding='utf-8') as f:
        a=' ? '.join([str(i) for i in range(1,an_int+1)])
        f.write(a)
        return len(a)

def write_ints(an_int,filename):
    with open(filename,'w',encoding='utf-8') as f:
        for n in range(1,an_int+1):
            a=[str(i*n) for i in range(1,n+1)]  # fixed by PMcG from a=[str(i*n) for in in range(1,n+1)]
            s=' '.join(a)
            f.write(f'{s}\n')

    
    
