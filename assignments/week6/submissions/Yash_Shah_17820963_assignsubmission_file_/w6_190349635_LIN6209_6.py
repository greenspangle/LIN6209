# Week 6 Assignment

def thermostat(temperature):
    if temperature < 19:
        return "on"
    if temperature > 24:
        return "off"
    else:
        return "stat"


def score_2(dice_1, dice_2):
    if dice_1 + dice_2 == 7:
        # double 7 -> 14
        return 14
    elif dice_1 + dice_2 == 12:
        # double 6 is 12 -> 14
        return 24
    elif dice_1 == dice_2:
        # both dice the same means it's a double
        # add one of the dice means any dice * 3
        return dice_1*3
    else:
        # base case -> sum of the two dice
        return dice_1 + dice_2


def score_4(red1, red2, blue1, blue2):
    # put all fo them in a list and sort eh list so that any permutation of 3 3 4 4 is easy to idneitify.
    sorted_list = sorted([red1, red2, blue1, blue2])

    if (sorted_list[0] == 3 and sorted_list[1] == 3) and (sorted_list[2] == 4 and sorted_list[3] == 4):
        # checks for 3 3 4 4 match
        return 21
    elif ((red1 + blue1 == 7) and (red2 + blue2 == 7)) or ((red1 + blue2 == 7) and (red2 + blue1 == 7)):
        # checks that the sum of any one blue and any one red is 7 and the remaining blue and red dice also sum to 7
        # could be b1+r1 and b2+r2 AND b1+r2 and b2+r1
        return 14
    elif (red1 + blue1 == 7 or red2 + blue2 == 7) or (red1 + blue2 == 7 or red2 + blue1 == 7):
        # checks that the sum of any one blue and any one read is 7
        # could be b1+r1 and b2+r2 OR b1+r2 and b2+r1
        return 7
    else:
        # base case, return smallest number which is index 0 in sorted list
        return sorted_list[0]


def fizzbuzz(an_int):
    # multiple of 3 AND 5
    if an_int % 3 == 0 and an_int % 5 == 0:
        return "FizzBuzz"
    elif an_int % 3 == 0:
        # only multiple of 3
        return "Fizz"
    elif an_int % 5 == 0:
        # only multiple of 5
        return "Buzz"
    else:
        # multiple of neither so return strign form of the number
        return str(an_int)


def num_seq_str(an_int):
    result = ""
    # itterate from 1 to an_int+1
    for i in range(1, an_int+1):
        if i == an_int:
            # last number so only add the number not the space or comma
            result += f"{i}"
            break
        # add the number, a commma and a space to the result
        result += f"{i}, "

    return result


def num_seq_list(an_int):
    # list comphrension that iterates frm 1 to an_int+1 and adds it to the list. it's same as the code below
    """
    result = []
    for i in range(1, an_int+1):
        result.append(i)
    return result
    """

    return [i for i in range(1, an_int+1)]


def num_seq_set(an_int):
    # same as num_seq_list except the list is wrapped in a set() which convert the list to a set
    return set([i for i in range(1, an_int+1)])


def num_seq_dict_(an_int):
    result = dict()
    # itterate from 1 to an_int+1 and add add the result of fizzbuzz(i) to the result dict
    for i in range(1, an_int+1):
        result[i] = fizzbuzz(i)

    return result


def get_chars_set(filename):
    with open(filename, "r", encoding="utf-8") as f:
        # read the file as a string, wrap the string in a set, removing duplicates, then rturn the set
        return set(f.read())


def count_chars(filename):
    with open(filename, "r", encoding="utf-8") as f:
        # read the file as a string and return the length of the string
        return len(f.read())


def count_Q(filename):
    with open(filename, "r", encoding="utf-8") as f:
        count = 0
        string = f.read()

        # iterate over the string and add 1 to the count if the current character (i) is a "?"
        for i in string:
            if i == "?":
                count += 1

    return count


def count_and(filename):
    with open(filename, "r", encoding="utf-8") as f:
        # read the file as a string and lowercase to remove case sensitivity
        string = f.read().lower()

        # count the occurences of each form of 'and' in the the sring
        no_space = string.count("and")
        with_space = string.count(" and ")
        with_comma = string.count(" and, ")

        # return all 3 as a a tuple
        return (no_space, with_space, with_comma)


def count_words(filename):
    with open(filename, "r", encoding="utf-8") as f:
        # read the file as a string and lowercase to remove case sensitivity
        string = f.read().lower()

        # if the file is empty then return 0
        if string == '':
            return 0

        # replace whitespaced characters with a single space
        string = string.replace('\n', " ").replace(
            '\t', " ").replace('\r', " ").replace('\cr', " ").replace('\b', " ")

        # split the string sing a space
        # word count is the length of that list containing all the words
        return len(string.split())


def char_frequency(filename):
    with open(filename, "r", encoding="utf-8") as f:
        # read the file as a string and lowercase to remove case sensitivity
        string = f.read().lower()
        result = dict()

        # replace whitespaced characters with a single space
        string = string.replace('\n', " ").replace(
            '\t', " ").replace('\r', " ").replace('\cr', " ").replace('\b', " ")

        # iterate over each character in the string
        for i in string:
            # if the character already exists in the result dict then increment the value by 1
            if i in result:
                result[i] += 1
            # otherwise add a new entry into the result dict with the letter being the key and set the value to 1
            else:
                result[i] = 1

        return result


def word_frequency(filename):
    with open(filename, "r", encoding="utf-8") as f:
        # read the file as a string and lowercase to remove case sensitivity
        string = f.read().lower()
        result = dict()

        # replace whitespaced characters adn punctuation with a single space
        string = string.replace('\n', " ").replace('\t', " ").replace(
            '\r', " ").replace('\cr', " ").replace('\b', " ").replace('.', " ").replace('!', " ").replace('?', " ").replace(',', " ")

        # split the string into a list of words, split using a space
        words = string.split()

        # iterate over each word in the words list
        for i in words:
            if i in result:
                # if the word already exists in the result dict then increment the value by 1
                result[i] += 1
            else:
                # otherwise add a new entry into the result dict with the word being the key and set the value to 1
                result[i] = 1

        return result


def text_analysis_01(filename):
    with open(filename, "r", encoding="utf-8") as f:
        # read the file as a string and lowercase to remove case sensitivity
        string = f.read().lower()

        sentence_count = 0
        # iterrate over each character in the string
        for i in string:
            if i == "." or i == "!" or i == "?":
                # add 1 to the sentence count if the current character is a ".", "!" or "?" as they mark sentence boundaries
                sentence_count += 1

        # split the string sing a space
        # word count is the length of that list containing all the words
        total_words = len(string.split())

        non_ws_char_count = 0
        ws_char_count = 0

        char_dict = dict()
        # iterate over each character in the string
        for i in string:
            if i in char_dict:
                # if the character already exists in the result dict then increment the value by 1
                char_dict[i] += 1
            else:
                # otherwise add a new entry into the result dict with the letter being the key and set the value to 1
                char_dict[i] = 1

        # iterate over the char_dict
        for key in char_dict:
            if key in " \t\r\b\cr\n":
                # if the character is a whitespace then add it's value stored inside char_dict to ws_char_count
                ws_char_count += char_dict[key]
            else:
                # otehrise if the character is NOT a whitespace then add it's value stored inside char_dict to non_ws_char_count
                non_ws_char_count += char_dict[key]

        # return the sentence count, total words, non whitespace character count, whitespace character count as a tuple
        return (sentence_count, total_words, non_ws_char_count, ws_char_count)


def write_Q(an_int, filename):
    with open(filename, "w", encoding="utf-8") as f:
        result = ""
        # itterate from 1 to an_int+1
        for i in range(1, an_int+1):
            if i == an_int:
                # if it's the last number in the list then add a only the number to the result string and exit loop the statement below doesn't execute
                result += f"{i}"
                break

            # add the current number to the result string with a space and questionmark and another space
            result += f"{i} ? "

        # write the result string to the file
        f.write(result)
        return len(result)


def write_ints(an_int, filename):
    with open(filename, "w", encoding="utf-8") as f:
        result = ""
        write_list = []

        # if an_int is 1 then write '1' to the file and exit the function
        if an_int == 1:
            f.write('1')
            return

        # itterate from 1 to an_int+1
        for i in range(1, an_int+1):
            # itterate from 1 to the current number in the loop
            for j in range(1, i+1):
                if i == an_int and j == an_int:
                    # if i and j both equal an_int then add them to the result string without spaces or lines since it's the last value that will be added
                    result += f"{i*j}"
                    # go back to the start of the loop to prevent the code below from excecuting
                    continue
                elif i == j:
                    # if both i an j are the same then multiply the numbers generated by the inner and outer loop and add them to the result with a new line (to build the triangle lookign shape)
                    result += f"{i*j}\n"
                    # go back to the start of the loop to prevent the code below from excecuting
                    continue

                # multiply the numbers generated by the inner and outer loop and add them to the result with a space
                result += f"{i*j} "

            # in the inner loop add the result to the list
            write_list.append(result)
            # set result to an empty string so it can be added to in the next pass of the inner loop
            result = ""

        # finally write each line to the file using write lines which adds multiple lines
        f.writelines(write_list)


# Extra Credit

def adjacency(filename):
    with open(filename, "r", encoding="utf-8") as f:
        # read the file as a string and lowercase to remove case sensitivity
        string = f.read().lower()

        # replace whitespaced characters adn punctuation with a single space
        string = string.replace('\n', " ").replace('\t', " ").replace(
            '\r', " ").replace('\cr', " ").replace('\b', " ").replace('.', " ").replace('!', " ").replace('?', " ").replace(',', " ")

        # split the string into a list of words, split using a space
        words = string.split()

        result = dict()
        # itterate over each word in the words list
        for i in range(len(words)):
            # set current to be the ith word in the list
            current = words[i]
            # set prev and next to be none since setting prev to words[i-1] will throw an IndexError
            prev = None
            next = None

            # this is mostly for the first word in the list as words[i-1] when the index is 0
            try:
                prev = words[i-1]
            except IndexError:
                pass

            # this is mostly for the last word in the list as words[i+1] when the index
            try:
                next = words[i+1]
            except IndexError:
                pass

            # if current is in the result dict then we can assume that it will have both list as values : [[before], [before]
            if current in result:
                # if taking the prev/next words was successful then add them to their respective lists
                if prev is not None:
                    # before list is 0th index of the result dict
                    before_list = result[current][0]
                    before_list.append(prev)
                elif next is not None:
                    # after list is 1st index of the result dict
                    after_list = result[current][1]
                    after_list.append(next)
            else:
                # if current is not the result dict then we can assume that it not have the 2 lists so we need to add it ourselves add the first prev/next vales to them
                result[current] = [[], []]
                if prev is not None:
                    # before list is 0th index of the result dict
                    result[current][0].append(prev)
                if next is not None:
                    # after list is 1st index of the result dict
                    result[current][1].append(next)

        return result


def predict_next(word, filename):
    # get all adjasent words from adjacency() function
    dict = adjacency(filename)

    if word in dict:
        # if the word exists inside the dict then create a word frequency dict and select the 'after' words list
        freq = {}
        words = dict[word][1]

        # itterate over each word in the words list
        for i in words:
            if i in freq:
                # if the word is in the freq dict then add 1 to it's value
                freq[i] += 1
            else:
                # else add the word as the key and set 1 as it's value
                freq[i] = 1

        # sort the freq dict
        # set the most common word as most_likely string
        # return the most likely word
        return sorted(freq)[-1]
    else:
        # this gets run if input word isn't in the dict of adjasent words
        with open(filename, "r", encoding="utf-8") as f:
            string = f.read().lower()

            for char in string:
               if not char.isalpha():
                   string = string.replace(char, " ")

            words = string.split()

            # returns the word directly after the input word (100% accuracy, since there is no data to generate possible proceding words this is the only we 'predict' the next word without using a statistical model with a large corpus)
            return words[words.index(word)+1]


def pluralizer(a_str):
    # dict of most common irregular plural words
    word_dict = {"aircraft": "aircraft",
                 "analysis": "analyses",
                 "antithesis": "antitheses",
                 "appendix": "appendices ",
                 "child": "children",
                 "corpus": "corpora",
                 "crisis": "crises",
                 "deer": "deer",
                 "diagnosis": "diagnoses",
                 "die": "dice",
                 "fish": "fish",
                 "foot": "feet",
                 "formula": "formulae",
                 "fungus": "fungi",
                 "goose": "geese",
                 "half": "halves",
                 "hoof": "hooves",
                 "hypothesis": "hypotheses",
                 "index": "indices",
                 "loaf": "loaves",
                 "locus": "loci",
                 "louse": "lice",
                 "man": "men",
                 "matrix": "matrices",
                 "moose": "moose",
                 "mouse": "mice",
                 "nucleus": "nuclei",
                 "parenthesis": "parentheses",
                 "phenomenon": "phenomena",
                 "sheep": "sheep",
                 "shrimp": "shrimp",
                 "species": "species",
                 "stimulus": "stimuli",
                 "synopsis": "synopses",
                 "thief": "thieves",
                 "tooth": "teeth",
                 "vertex": "vertices",
                 "wife": "wives",
                 "wolf": "wolves",
                 "woman": "women"}

    # if strign is empty, there's noting to pluralize
    if a_str == '':
        return ''

    if a_str in word_dict:
        # if the word is in the word_dict then return it's pluarl
        return word_dict[a_str]
    elif a_str[-1] == 'z' or a_str[-1] == 'x':
        # if it ends with a z or x like 'fox' or 'box' then add -es to it
        return f'{a_str}es'
    else:
        # base case - use the default -s plural suffix
        return f'{a_str}s'
