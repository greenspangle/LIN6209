# W6 LIN 6209 Assignment.
# Design, build and test the following functions.
# Submit your python script with the filename 'w6_yourID.py'.
# This is one version of the answers."""
import string


def thermostat(temperature):
    """If the temperature is less that 19 turn the heat on, If it's more than 24 turn the heat off. If it's
    neither, leave the heat setting as it is. Return the string `'on'`, `'off'` or `'stat'` respectively."""
    # the three clauses in this compound if statement include all possible values of temperature
    # therefore one of them must return a value
    if temperature < 19:
        return 'on'
    elif temperature > 24:
        return 'off'
    else:
        return 'stat'


def score_2(dice_1, dice_2):
    """The parameters are guaranteed to be integers between 1 and 6 inclusive and represent the face values on the
    throw of two six-sided dice. Calculate the score according to this rule:
        1 The score is the sum of both dice
        2 unless it is a 'double' (both dice the same) in which case add one of the dice to the score again
        3 unless it is 'double six' (both dice six) in which case add both dice to the score again
        4 unless the sum of the two dice is seven in which case double it"""
    # a sequence of if statements covers all possibilities
    score = dice_1 + dice_2  # rule 1
    if score == 7:  # rule 4 = sum is seven
        score = 14
    if dice_1 == dice_2:  # rule 2 = it's a double
        score = dice_1 + dice_2 + dice_1
    if dice_1 == 6 and dice_2 == 6:  # rule 3 = double six!
        score = dice_1 + dice_2 + dice_1 + dice_2
    # all options considered, return the score
    return score


def score_4(red1, red2, blue1, blue2):
    """The parameters are guaranteed to be integers between 1 and 6 inclusive. They represent the face values on
    the throw of four six-sided dice, two coloured red and two coloured blue. Calculate the score according to
    the rule:
        1 The score is the face value of the lowest of all four dice
        2 Unless the sum of any one red dice and any one blue dice is seven in which case score 7
        3 Unless the sum of any one red dice and any one blue dice is seven, and the sum of the remaining red and
          blue dice is also seven, in which case score 14
        4 Unless the four dice are any permutation of (3,3,4,4), in which case score 21 """
    # a sequence of if statements covers all possibilities
    # rule 1 - create a tuple (or list or set) and apply min(). This also ensures that score always has a value
    score = min((red1, red2, blue1, blue2))
    # rule 2 - the sum of any one red dice and any one blue dice is seven
    if red1 + blue1 == 7 or red1 + blue2 == 7 or red2 + blue1 == 7 or red2 + blue2 == 7:
        score = 7
    # rule 3 - sum of any one red dice and any one blue dice is seven,
    #          and the sum of the remaining red and blue dice is also seven
    if (red1 + blue1 == 7 and red2 + blue2 == 7) or (red1 + blue2 == 7 and red2 + blue1 == 7):
        score = 14
    # rule 4 - the four dice are any permutation of (3,3,4,4),
    if (red1 == 3 and red2 == 3 and blue1 == 4 and blue2 == 4) or \
            (red1 == 3 and red2 == 4 and blue1 == 3 and blue2 == 4) or \
            (red1 == 3 and red2 == 4 and blue1 == 4 and blue2 == 3) or \
            (red1 == 4 and red2 == 3 and blue1 == 3 and blue2 == 4) or \
            (red1 == 4 and red2 == 3 and blue1 == 4 and blue2 == 3) or \
            (red1 == 4 and red2 == 4 and blue1 == 3 and blue2 == 3):
        score = 21
    return score


def fizzbuzz(an_int):
    """The parameter is guaranteed to be a positive integer or zero.
        1 if `an_int` is a multiple of 3 return `'Fizz'`
        2 if it is a multiple of 5 return `'Buzz'`
        3 if it is a multiple of 15 return `'FizzBuzz'`.
        4 if it is none of those then return `str(an_int)`."""
    # set result to empty string so that it exists
    result = ''
    # rule 1
    if an_int % 3 == 0:  # an_int is divisible by three
        result += 'Fizz'  # append 'Fizz' to result which has a current value of ''
    # rule 2
    if an_int % 5 == 0:  # an_int is divisible by five
        result += 'Buzz'  # append 'Fizz' to result  which has a current value of either '' or 'Fizz')
    # rule 3 - this is covered by the combination of statements '# rule 1' and '# rule 2'
    # rule 4
    if result == '':  # result is still empty so apply default rule
        result = str(an_int)
    return result


def num_seq_str_v1(an_int):
    """The parameter is guaranteed to be a positive integer greater than zero. Return a string containing the
    integers 1 to an_int inclusive. Successive integers are separated by a comma and a space. Note that there is
    no trailing comma or space at the end of the string. """
    result = ''  # will build return value as a string
    for i in range(1, an_int + 1):
        result += str(i) + ','  # append next integer with trailing comma
    # result contains required return value - PLUS a trailing comma
    result = result[:-1]  # drop the trailing comma
    return result


def num_seq_str_v2a(an_int):
    """Exactly the same pattern as v1, but entirely with lists"""
    result = []  # will build return value as a list of strings
    for i in range(1, an_int + 1):
        result.append(str(i) + ',')  # each element is an integer followed by a comma
    # all component parts of result are now assembled in list
    # use str.join() method to assemble list elements into a string
    result = ' '.join(result)
    return result[:-1]  # and return result minus the trailing comma


def num_seq_str_v2b(an_int):
    """Exactly the same pattern as v1, but entirely with lists"""
    int_list = []  # first build the list of integers
    for i in range(1, an_int + 1):
        int_list.append(str(i))  # each element is an integer
    # all component parts of result are now assembled in list
    # use str.join() method to assemble list elements into a string separated by comma-space
    result_str = ", ".join(int_list)
    return result_str  # and return result


def num_seq_str_v2c(an_int):
    """Exactly the same pattern as 2b, but with a list comprehension"""
    int_list = [str(i) for i in range(1, an_int + 1)]
    # assemble list of integers into a string separated by comma-space and done
    return ', '.join(int_list)


# I like v2c best as it's concise and to the point.
# best use v1 as that's the most 'obvious'
num_seq_str = num_seq_str_v1


def num_seq_list(an_int):
    """The parameter is guaranteed to be a positive integer greater than zero. Return a list containing the
    integers 1 to an_int inclusive."""
    return [i for i in range(1, an_int + 1)]


def num_seq_set(an_int):
    """The parameter is guaranteed to be a positive integer greater than zero. Return a set containing the integers
    1 to an_int."""
    return {i for i in range(1, an_int + 1)}  # create set using a comprehension


def num_seq_dict_v1(an_int):
    """The parameter is guaranteed to be a positive integer greater than zero. Return a dictionary containing the
    integers 1 to an_int as the keys of the dictionary. The value associated with each key should be the string
    returned by fizzbuzz(key)."""
    return {i: fizzbuzz(i) for i in range(1, an_int + 1)}


def num_seq_dict_v2(an_int):
    """Make the assembly of the dictionary explicit"""
    result_dictionary = {}  # an empty dictionary
    for i in range(1, an_int + 1):
        result_dictionary[i] = fizzbuzz(i)  # add the integer keys and set value to fizzbuzz
    # all done so just return the assembled dictionary
    return result_dictionary


# the list comprehension is especially neat :-) but stick with the simpler v2
num_seq_dict = num_seq_dict_v2


def count_chars(filename):
    """The parameter is guaranteed to be the name of a text file encoded as utf-8. Read the file and return number
    of characters in the file. There is no need to be concerned as to what constitutes a 'character'. Count
    everything."""
    with open(filename, 'r', encoding='utf_8') as f:
        # assume the file is not too big to chomp in a single mouthful ....
        contents = f.read()
    # file contents are now in 'content'. Number of characters is its length
    return len(contents)


def count_Q_for(filename):
    """The parameter is guaranteed to be the name of a text file encoded as utf-8. Read the file and count the
    number of occurrences of the character ‘?’ (a question mark, unicode 63 decimal or 3F hexadecimal)."""
    with open(filename, 'r', encoding='utf_8') as f:
        # assume the file is not too big to chomp in a single mouthful ....
        contents = f.read()
    # file contents are now in 'content'. Iterate through list counting '?'
    q_count = 0
    for char in contents:
        if char == '?':
            q_count += 1
    # count of '?' occurrences is now in q_count, so just return that
    return q_count


def count_Q_while(filename):
    """Essentially the same as count_Q_for except using a 'while' loop."""
    with open(filename, 'r', encoding='utf_8') as f:
        # assume the file is not too big to chomp in a single mouthful ....
        contents = f.read()
    # file contents are now in 'content'. Iterate through list counting '?'
    # set counters to zero
    q_count = 0
    i = 0
    while i < len(contents):  # from first character to last character
        if contents[i] == '?':  # check if it is a '?'
            q_count += 1
        i += 1  # move to next character
    # count of '?' occurrences is now in q_count, so just return that
    return q_count


def count_Q_method(filename):
    """The parameter is guaranteed to be the name of a text file encoded as utf-8. Read the file and count the
    number of occurrences of the character ‘?’ (a question mark, unicode 63 decimal or 3F hexadecimal)."""
    with open(filename, 'r', encoding='utf_8') as f:
        # assume the file is not too big to chomp in a single mouthful ....
        content = f.read()
    # file contents are now in 'content'. Use the string count() method to count the question marks.
    return content.count('?')


# all versions work (I hope!). Definitely always use ready-made object methods
count_Q = count_Q_method


def count_and(filename):
    """ The parameter is guaranteed to be the name of a text file encoded as utf-8. Read the file and count the
    number of occurrences of each of the character strings `'and'`, `' and '`, and `' and, '`(the string 'and';
    same but with spaces both sides; same again but with a space before and a comma and a space after).Ignore
    the case of the text.Return the respective counts as integers. """
    with open(filename, 'r', encoding='utf_8') as f:
        # assume the file is not too big to chomp in a single mouthful ....
        content = f.read()
    # file contents are now in 'content'.
    # As before, could use a 'for' or 'while' loop to iterate through file contents and count
    # but definitely always try and re-use existing software/functionality
    return content.count('and'), content.count(' and '), content.count(' and, ')


def count_words(filename):
    """The parameter is guaranteed to be the name of a text file encoded as utf-8.
    Read the file and return number of words in the file."""
    with open(filename, 'r', encoding='utf_8') as f:
        # assume the file is not too big to chomp in a single mouthful ....
        contents = f.read()
    # file contents are now in 'content'.
    # use the helper function _count_words_in_str(a_str)
    result = _count_words_in_str(contents)
    return result


def _count_words_in_str(a_str):
    # replace all whitespace by true whitespace ' '
    for char in string.whitespace:
        a_str.replace(char, ' ')
    # split that string on spaces (default behaviour of split() method)
    contents = a_str.split()
    # every word is an element in that list  so number of words is length of that list
    return len(contents)


def char_frequency(filename):
    """Return a dictionary with every character in filename as a key with a value equal to
    the number of its occurrences with filename."""
    # Read the file
    with open(filename, 'r', encoding='utf_8') as f:
        # assume the file is not too big to chomp in a single mouthful ....
        contents = f.read()
    # file contents are now in 'content'. Iterate through it counting character occurrences into a dictionary
    # create an empty dictionary
    char_freq = dict()  # an empty dictionary
    # for every character, increment its entry in dictionary, creating an entry if it is not already present
    for char in contents:
        if char in char_freq:
            char_freq[char] += 1
        else:
            char_freq[char] = 1
            # all done, just return the dictionary containing the frequency information
    return char_freq


def word_frequency(filename):
    """Return a dictionary with every word in filename as a key and the associated value the number
     of its occurrences within filename."""
    # open the file and read it's contents
    with open(filename, 'r', encoding='utf_8') as f:
        # assume the file is not too big to chomp in a single mouthful ....
        contents = f.read()
    # file contents are now in 'content'.
    # replace all whitespace by true whitespace ' '
    for char in string.whitespace:
        contents.replace(char, ' ')
    words = contents.split()  # split content on spaces (default behaviour of split() method)
    w_freq = {}  # create an empty dictionary to hold results
    # for every character, increment its entry in dictionary, creating an entry if it is not already present
    for word in words:
        if word in w_freq:  # if this word is in dictionary
            w_freq[word] += 1  # increase its count by one
        else:  # if it's not in dictionary
            w_freq[word] = 1  # add an entry to dictionary with a count of 1
    # all done, just return the dictionary containing the frequency information
    return w_freq


def text_analysis_01(filename):
    """The parameter is guaranteed to be the name of a text file encoded as utf-8. Read the file and return a tuple
    containing:
    * Total number of sentences
    * Total number of words
    * Total number of non-whitespace characters
    * Total number of whitespace characters
    Assume that:
    * All sentences are terminated by a period (full stop) or '!' or '?' followed by a space except for the last sentence in
      the file which might be terminated by the end of the file or just a '.' or '!' or '?' mark.
    * The file contents are entirely prose-like text. There are no tables, diagrams or any other complexities of
      any kind."""

    # open the file and read it's contents
    with open(filename, 'r', encoding='utf_8') as f:
        # assume the file is not too big to chomp in a single mouthful ....
        contents = f.read()
    # file contents are now in 'content'

    # count sentences
    s_count = 0
    s_end = {'.', '!', '?'}
    # count occurrences of {'.', '?', '!'} followed by space
    for i in range(len(contents) - 1):
        if contents[i] in s_end and contents[i + 1] == ' ':
            s_count += 1
    # check end of sentence
    if contents[-1] in s_end:
        s_count += 1

    # count words - have already done this so just call function
    w_count = _count_words_in_str(contents)

    # count whitespace and non-whitespace characters
    w_char = 0
    w_char_not = 0
    for char in contents:
        if char not in string.whitespace:
            w_char += 1
        else:
            w_char_not += 1


################################

def write_Q(an_int, filename):
    """The parameters are guaranteed to be a positive integer **greater than zero** and a legal filename.
    Write the sequence of integers from 1 to an_int inclusive to a text file, with each integer separated
    from the next by the string ' ? ' (space, question mark, space). The return value should be the count
    of the total number of characters written to the file."""


def write_ints(an_int, filename):
    """The parameters are guaranteed to be a positive integer **or zero** and a legal filename.
    Create the file if it does not already exist and write `an_int` lines to the file.
    The successive lines of the file each start with the `next integer` in the ascending sequence from 1
    to `an_int` followed by the sequence of integer multiples of `next_integer` up to and including
    `next_integer * next_integer`.
    All the integers in the same line are separated by a single space.
    No space is added at the beginning or the end of the line."""
    pass


# Section 2 - Extra Credit

def adjacency(filename):
    """The parameter is guaranteed to be the name of a text file encoded as utf-8.
    Read the file and return adictionary containing every word as a key.
    Associated with each key are two lists:
        * The words that have occurred immediately **before** the key word in `filename`
        * The words that have occurred immediately **after** the key word in `filename`"""
    pass


def predict_next(word, filename):
    """The parameter word is a string with no punctuation or spaces. The `filename` is guaranteed to be
    the name of a text file encoded as utf-8. Read the file and provided `word` occurs within it, return
    the word most likely to follow `word` based upon the corpus of text within `filename`.
    If `word` is not present in filename return `None`."""
    pass


def pluralizer(a_str):
    """The parameter is guaranteed to be a word. Return the plural of that word.
    **Test Data:** Banana, Leaf, Trolley, Lorry, Sheep, Church, Sausage, Monkey, Knife, Child, Match, Poppy
    **Hints:**
    Given the variability and irregular structure of natural language there is no perfect version of
    this function and a balance needs to be struck between coverage and the ever-increasing complexity
    of the code."""
    pass
