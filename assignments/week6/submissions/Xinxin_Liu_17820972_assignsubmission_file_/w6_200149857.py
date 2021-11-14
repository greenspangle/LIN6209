def thermostat(temperature):
    if temperature < 19:
        return 'on'
    if temperature > 24:
        return 'off'
    if temperature >=19 and temperature <= 24:
        return 'stat'

def score_2(dice_1,dice_2):
    if dice_1+dice_2==7:
        return (dice_1+dice_2) * 2
    if dice_1==6 and dice_2==6:
        return dice_1*2+dice_2*2
    if dice_1==dice_2:
        return dice_1+dice_2+dice_1
    return dice_1+dice_2

def score_4(red1,red2,blue1,blue2):
    d=dict.fromkeys([1,2,3,4,5,6],0)
    d[red1] = d[red1]+1
    d[red2] = d[red2] + 1
    d[blue1] = d[blue1] + 1
    d[blue2] = d[blue2] + 1
    if d[4]==2 and d[3]==2:
        return 21
    if (red1+blue1==7 and red2+blue2==7) or (red1+blue2==7 and red2+blue1==7):
        return 14
    if red1+blue1==7 or red1+blue2==7 or red2+blue1==7 or red2+blue2==7:
        return 7
    return min(red1,red2,blue1,blue2)

def fizzbuzz(an_int):
    if an_int%15==0:
        return 'FizzBuzz'
    if an_int%3==0:
        return 'Fizz'
    if an_int%5==0:
        return 'Buzz'
    return str(an_int)

def num_seq_str(an_int):
    s = num_seq_list(an_int)
    s=str(s)
    s1=s.replace("[","")
    s2=s1.replace("]",'')
    return s2


#range(5) [0, 1, 2, 3, 4]
# [] -> [1]
#[1] -> [1, 2]
# [1,.., b-1] -> [1, ..,b-1] + [b]
def num_seq_list(an_int):
    s=[]
    for b in range(1,an_int+1):
        s = s + [b]
    return s

def num_seq_set(an_int):
    s=set()
    for b in range(1,an_int+1):
        s.add(b)
    return s

def num_seq_dict_(an_int):
    d=dict()
    for b in range(1,an_int+1):
        d[b] = fizzbuzz(b)
    return d

def get_chars_set(filename):
    with open(filename,'r',encoding='utf-8') as f:
        content=f.read()
        return set(content)

def count_chars(filename):
    with open(filename,'r',encoding='utf-8')as f:
        content=f.read()
        return len(content)

def count_Q(filename):
    with open(filename,'r',encoding='utf-8')as f:
        content=f.read()
        c=str(content)
        b=c.count('?')
        return b

def count_and(filename):
    with open(filename,'r',encoding='utf-8')as f:
        content=f.read()
        c=str(content)
        d=c.lower()
        b=d.count('and')
        s=d.count(' and ')
        y=d.count(' and, ')
        return b,s,y

def count_words(filename):
    with open(filename,'r',encoding='utf-8')as f:
        content=f.read()
        c=str(content)
        d=c.split()
        f=len(d)
        return f

def char_frequency(filename):
    with open(filename,'r',encoding='utf-8')as f:
        content=f.read()
        s=str(content)
        d=dict.fromkeys(s,0)
        for sb in s:
            d[sb]=d[sb]+1
        return d

def word_frequency(filename):
    with open(filename,'r',encoding='utf-8')as f:
        content=f.read()
        s=str(content)
        b=s.split()
        d=dict.fromkeys(b,0)
        for word in b:
            d[word]=d[word]+1
        return d

def text_analysis_01(filename):
    with open(filename,'r',encoding='utf-8')as f:
        content=f.read()
        s=str(content)
        s=s.replace('?','.')
        s=s.replace('!','.')
        f=s.split('.')
        sentence=len(f)-1
        g=s.replace('.','')
        g=g.split()
        word=len(g)
        h=str(content)
        all=len(h)
        i=h.split()
        j=''.join(i)
        non=len(j)
        white=all-non
        return sentence,word,non,white

def write_Q(an_int,filename):
    l=[]
    for s in range(1,(an_int+1)):
        l=l+[str(s)]
    r = ' ? '.join(l)
    f = open(filename,'w',encoding='utf-8')
    return f.write(r)

def write_ints(an_int,filename):
    x = an_int
    s = ''
    for i in range(1,x+1):
        ihang = []
        for j in range(1,i+1):
            ihang = ihang + [str(i*j)]
        sihang = ' '.join(ihang)
        s = s + sihang + '\n'
    f= open(filename,'w',encoding='utf-8')
    f.write(s)
    return
