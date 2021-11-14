def thermostat(temp):
    if temp <19:
        return 'on'
    elif temp >24:
        return 'off'
    else:
        return 'stat'
def score_2(d1, d2):
    score=d1+d2
    if score == 7:
        return 14
    elif d1==6 and d2==6:
        return 24
    elif d1==d2:
        return score+d1
    else:
        return score
def score_4(r1, r2, b1, b2):
    sortlist = (r1, r2, b1, b2)
    sortlist=sorted(sortlist)
    score=sortlist[0]
    threeCount=0
    fourCount=0
    for i in sortlist:
        if i == 3:
            threeCount=threeCount+1
        elif i ==4:
            fourCount=fourCount+1
    if threeCount==2 and fourCount==2:
        return 21
    if r1+b1 == 7:
        if r2+b2==7:
            return 14
        else:
            return 14
    elif r1+b2==7:
        if r2+b1==7:
            return 14
        else:
            return 7
    elif r2+b1==7:
        if r1+b2==7:
            return 14
        else:
            return 7
    elif r2+b2==7:
        if r1+b1==7:
            return 14
        else:
            return 7
    return score
def fizzbuzz(int1):
    if int1%15==0:
        return 'FizzBuzz'
    elif int1%3==0:
        return 'Fizz'
    elif int1%5==0:
        return 'Buzz'
    else:
        return str(int1)
def num_seq_str(int1):
    numberStr=''
    for i in range(int1):
        if i==0:
            numberStr=numberStr
        else:
            numberStr+=str(i)+', '
    numberStr+=str(int1)
    return numberStr
def num_seq_list(int1):
    seqList=[]
    for i in range(int1):
        if i==0:
            seqList=seqList
        else:
           seqList.append(i)
    seqList.append(int1)
    return seqList
def num_seq_set(int1):
    seqSet=set(())
    for i in range(int1):
        if i==0:
            seqSet=seqSet
        else:
           seqSet.add(i)
    seqSet.add(int1)
    return seqSet
def num_seq_dict(int1):
    seqDic={}
    for i in range(int1):
        if i==0:
            seqDic=seqDic
        else:
           seqDic[i] = fizzbuzz(i)
    seqDic[int1] = fizzbuzz(int1)
    return seqDic
def get_chars_set(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        content=set(f.read())
        return content
def count_chars(filename):
     with open(filename, 'r', encoding='utf-8') as f:
        result=len(f.read())
        return result
def count_Q(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        content=f.read()
        result=content.count('?')
        return result
def count_and(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        content=f.read()
        result1=content.count('and')
        result2=content.count(' and ')
        result3=content.count(' and, ')
        return result1, result2, result3
def count_words(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        content=f.read()
        wordCounter=0
        position=1
        for i in range(len(content)):
            if content[i].isspace() == True:
                if content[i-1].isspace() == False:
                    wordCounter+=1
            elif position == len(content):
                if content[i].isspace()== False:
                    wordCounter+=1
            position+=1
        return wordCounter
def char_frequency(filename):
    charDic={}
    with open(filename, 'r', encoding='utf-8') as f:
        content=f.read()
        for i in content:
            charDic[i] = content.count(i)
        return charDic
def word_frequency(filename):
    currentWord=''
    wordDic={}
    with open(filename, 'r', encoding='utf-8') as f:
        content=f.read()
        for i in range(len(content)):
            if content[i].isspace() == False:
                currentWord+=content[i]
                if i==len(content)-1:
                    if currentWord in wordDic:
                        wordDic[currentWord]+=1
                    else:
                        wordDic[currentWord]=1
            elif content[i].isspace() == True:
                if currentWord in wordDic:
                    wordDic[currentWord]+=1
                else:
                    wordDic[currentWord]=1
                currentWord=''
        return wordDic
def average_word_length(filename):
    numOfChars=0
    with open(filename, 'r', encoding='utf-8') as f:
        content=f.read()
        for i in content:
            if i.isspace()==False:
                numOfChars+=1
            else:
                numOfChars+=0
    return numOfChars/count_words(filename)
def text_analysis_01(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        content=f.read()
        whiteChars=0
        NwhiteChars=0
        Sentences=0
        position=0
        for i in content:
            if i.isspace()==False:
                NwhiteChars+=1
            else:
                whiteChars+=1
            if len(content) != position+1:
                    if i=='.' and content[position+1] ==' ':
                        Sentences+=1
            else:
                Sentences+=1
            position+=1
                
        result = (Sentences, count_words(filename), NwhiteChars, whiteChars)
        return result
def write_Q(int1, filename):
    String=''
    for i in range(int1):
        if i !=0:
            String+= str(i) + ' ? '
    String += str(int1)
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(String)
    with open(filename, 'r', encoding='utf-8') as f:
        return len(f.read())
def write_ints(int1, filename):
    with open(filename, 'w', encoding='utf-8') as f:
        for i in range(1, int1):
            for a in range(1, i+1):
                result=a*i
                f.write(str(result)+ ' ')
            f.write('\n')
        for a in range(1, int1+1):
                result=a*int1
                f.write(str(result)+ ' ')
