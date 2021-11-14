def thermostat(temperature):
    if temperature <19:
        return 'on'
    elif temperature >24:
        return 'off'
    else:
        return 'stat'


def score_2(dice_1,dice_2):
    if dice_1 and dice_2 == 6:
        return 24
    elif dice_1==dice_2:
        return (dice_1)*3
    elif dice_1+dice_2 == 7:
        return 14
    else:
        return dice_1+dice_2


def score_4(red1,red2,blue1,blue2):
    if (red1 == 3 and red2 == 3 and blue1 == 4 and blue2 == 4) or (red1 == 3 and red2 == 4 and blue1 == 4 and blue2 == 3) or (red1 == 3 and red2 == 4 and blue1 == 3 and blue2 == 4) or (red1 == 4 and red2 == 4 and blue1 == 3 and blue2 == 3) or (red1 == 4 and red2 == 3 and blue1 == 3 and blue2 == 4) or (red1 == 4 and red2 == 3 and blue1 == 4 and blue2 == 3):
        return 21
    elif red1+blue1 and red2+blue2 == 7:
        return 14
    elif red1+blue2 and red2+blue1 == 7:
        return 14
    elif (red1+blue1) ==7:
        return 7
    elif(red1+blue2) ==7:
        return 7
    elif(red2+blue1) ==7:
        return 7
    elif(red2+blue2) == 7:
        return 7
    elif red1<= red2 and red1 <= blue1 and red1 <= blue2:
        return red1
    elif red2<= (red1 and blue1 and blue2):
        return red2
    elif blue1<= (red1 and red2 and blue2):
        return blue1
    else:
        return blue2


    

def fizzbuzz(an_int):
    if an_int%15 == 0:
        return 'FizzBuzz'
    elif an_int%5 == 0:
        return 'Buzz'
    elif an_int%3 == 0:
        return 'Fizz'
    else:
        return str(an_int)
        

def num_seq_str(an_int):
    count=''
    for i in range(an_int-1):
        i=i+1
        count=(count+str(i)+', ')
    count=count+str(an_int)
    return count


def num_seq_list(an_int):
    count=[]
    for i in range(an_int-1):
        i=i+1
        count.append(i)
    count.append(an_int)
    return count


def num_seq_set(an_int):
    count=set()
    for i in range(an_int-1):
        i=(i+1)
        count.add(i)
    count.add(an_int)
    return count


def num_seq_dict(an_int):
    fizzbuzz = dict()
    count=0
    for i in range(an_int):
        if (i+1)%15 == 0:
            i1='Fizzbuzz'
        elif (i+1)%5==0:
            i1='Buzz'
        elif (i+1)%3==0:
            i1='Fizz'
        else:
            i1=str(i+1)
        fizzbuzz[count+1]=i1
        count=count+1
    return fizzbuzz


def get_chars_set(filename):
    with open(filename, 'r', encoding='utf-8') as f:  # open the file for read
        content = f.read()
    content=set(content)
    return content


def count_chars(filename):
    with open(filename, 'r', encoding='utf-8') as f:  # open the file for read
        content = f.read()
        content=str(content)
    return len(content)


def count_Q(filename):
    with open(filename, 'r', encoding='utf-8') as f:  # open the file for read
        content = f.read().lower
        content=str(content)
        count=content.count('?')
        return count
#this will not count the question mark, but it will count other letters, eg 'i'
#i have tried a for loop and str.count() and neither would work
#it worked when i first wrote it so im unsure why not, when im checking it, it wont work
#in char_frequency, it will even tell me that there is x question marks

def count_and(filename):
    with open(filename, 'r', encoding='utf-8') as f:  # open the file for read
        content = f.read().lower
        content=str(content)
        plain=content.count('and')
        space=content.count(' and ')
        comma=content.count(' and, ')
    return plain, space, comma
#i do not understand why this wont work same as above


def count_words(filename):
    with open(filename, 'r', encoding='utf-8') as f:  # open the file for read
        content = f.read().lower()
        content=str(content)
        content=content.replace('.','').replace('1', '').replace('2', '').replace('3', '').replace('4', '').replace('5', '').replace('6', '').replace('7', '').replace('8', '').replace('9', '').replace('0', '')
        content=content.replace('  ',' ')
        content=content.replace('\n','').replace('\t','').replace('\cr','').replace('\r','').replace('\v','').replace('\f','')
        content=content.split(' ')
    return len(content)



def char_frequency(filename):
    with open(filename, 'r', encoding='utf-8') as f:  # open the file for read
        content = f.read() #not lowercase because capitals could be important
        content =str(content)
        freq={}
        for i in content:
            key=i
            if i in freq:
                freq[i]=freq[i]+1
            else:
                freq[i]=1
        return freq




def word_frequency(filename):
    with open(filename, 'r', encoding='utf-8') as f:  # open the file for read
        content = f.read().lower()
        content=str(content)
        content=content.replace('.','').replace('1', '').replace('2', '').replace('3', '').replace('4', '').replace('5', '').replace('6', '').replace('7', '').replace('8', '').replace('9', '').replace('0', '')
        content=content.replace('  ',' ')
        content=content.replace('\n','').replace('\t','').replace('\cr','').replace('\r','').replace('\v','').replace('\f','')
        words=content.split(' ')
        freq={}
        for i in words:
            key=i
            if i in freq:
                freq[i]=freq[i]+1
            else:
                freq[i]=1
        return freq


def text_analysis_01(filename):
    with open(filename, 'r', encoding='utf-8') as f:  # open the file for read
        content = f.read().lower()
        content=str(content)
        sentences=0
        space=0
        char=0
        for i in content:
            if i.isspace()==True:
                space+=1
            else:
                char+=1
        words=content.replace('.','').replace('1', '').replace('2', '').replace('3', '').replace('4', '').replace('5', '').replace('6', '').replace('7', '').replace('8', '').replace('9', '').replace('0', '')
        words=words.replace('  ',' ')
        words=words.replace('\n','').replace('\t','').replace('\cr','').replace('\r','').replace('\v','').replace('\f','')
        words=words.rstrip()#removing whitespace so the list doesn't have anything extra in it
        words=words.split(' ')
        content=content.replace(content[-1],content[-1]+' ')#adding whitespace at the end to detect sentences
        sentences=content.count('. ')+content.count('! ')+content.count('? ')
        return sentences,len(words),char,space



def write_Q(an_int,filename):
    with open(filename, 'w') as f:
        question=''
        for i in range(1,an_int):
            i=str(i)
            question=question.replace(question,question+i+' ? ')
        an_int=str(an_int)
        question=question.replace(question,question+an_int)
        f.write(question)
    return len(question)


def write_ints(an_int,filename):
    with open(filename, 'w') as f:  # open the file for writing
        lines=[]
        line=str()
        for i in range(1,an_int+1): #this is the number of lines
            line=''
            for j in range(1,i+1):
                line=line.replace(line,line+str(i*j)+' ')
            line=line.rstrip()
            f.write(line+'\n')
        return



#i wanted to do the extra credit, but had other assignments so just ran out of time!
#pluraliser, add a space at the end of the words so you can then look for suffixes
#once you have found your suffixes, do an if statement to make the plural eg ch or x adds es, y or ey changes to ies, else add s
