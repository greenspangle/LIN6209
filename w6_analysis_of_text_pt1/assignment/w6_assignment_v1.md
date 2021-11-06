# Week 4 Assignment

Design, build and test the following functions:
Submit your python script with the filename 'w6_yourID.py'.\

## thermostat(temperature)

If the temperature is less that 19 turn the heat on, If it's more than 24 turn the heat off. If it's
neither, leave the heat setting as it is. Return `'on'`, `'off'` or `'stat'` respectively.\
For example:

temperature | return value
:---------:|:-------:|
`21` | `stat`
`16` | `on`
`34` | `off`
`19` | `stat`
`24` | `stat`

**Hints:**\
A few `if` statements with possibly some `elif` and `else`, should get the job done.

## score_2a(dice_1, dice_2)

The parameters are guaranteed to be integers between 1 and 6 inclusive and represent the face values on the
throw of two six-sided dice. Calculate the score according to this rule:

* The score is the sum of both dice unless it is a 'double' (both dice the same) in which case add one of
  the dice to the score again, unless it is 'double six' in which case both dice to the score again.

For example:

parameter values | return value
:---------:|:-------:|
`1, 5` | `6`
`5, 1` | `6`
`3, 4` | `7`
`1, 1` | `3`
`2, 2` | `6`
`6, 6` | `24`

**Hints:**\
A few `if` statements with possibly some `elif` and `else`, should get the job done.

## score_2b(dice_1, dice_2)

Unchanged from score_2a() except that if the sum of both dice is seven, double it.\
For example:

parameter values | return value
:---------:|:-------:|
`1, 5` | `6`
`5, 1` | `6`
`3, 4` | `14`
`5, 2` | `14`
`1, 1` | `3`
`2, 2` | `6`
`6, 6` | `24`

**Hints:**\
Same again: `if`,  `elif` and `else` statements. This is just another condition to consider.

## score_4a(red1, red2, blue1, blue2)

The parameters are guaranteed to be integers between 1 and 6 inclusive. They represent the face values on
the throw of four six-sided dice, two coloured red and two coloured blue. Calculate the score according to
the rule:

* The score is the sum of both red dice.
* If the sum of the red dice is seven add the lowest blue dice to the score.
* If the two red dice are the same but not both six, add the highest blue dice to the score.
* If the two red dice are both six then add both blue dice to the score.\
  For example:

parameter values | return value
:---------:|:-------:|
`1, 5, 6, 6` | `6`
`3, 2, 3, 3` | `5`
`2, 5, 2, 6` | `9`
`1, 1, 2, 6` | `8`
`6, 6, 3, 2` | `17`

**Hints:**\
Same again: `if`, `elif` and `else`. Just be careful you cover all the options and test them.

## score_4b(red1, red2, blue1, blue2)

The parameters are guaranteed to be integers between 1 and 6 inclusive. They represent the face values on
the throw of four six-sided dice, two coloured red and two coloured blue. Calculate the score according to
the rule:

**TBA**\

* If the sum of any one red dice and any one blue dice is seven, score 7.
* If the sum of any one red dice and any one blue dice is seven, and the sum of the remaining red and blue
  dice is also seven, score 21.
* Otherwise, score the face value of the lowest of all four dice.\
  For example:

parameter values | return value
:---------:|:-------:|
`1, 5, 6, 6` | `7`
`3, 2, 3, 3` | `2`
`2, 6, 1, 5` | `21`
`1, 1, 2, 6` | `7`
`6, 6, 6, 6` | `6`

**Hints:**\
Same again: `if`, `elif` and `else`. Just be careful you cover all the options and test them.

## fizzbuzz(an_int)

The parameter is guaranteed to be a positive integer or zero. If `an_int` is a multiple of 3 return `'Fizz'`
, if it is a multiple of 5 return `'Buzz'` and if it is a multiple of 15 return `'FizzBuzz'`. If it is none
of those then return `str(an_int)`.\
For example:

parameter value | return value
:---------:|:-------:|
`1` | `'1'`
`5` | `'Buzz'`
`33` | `Fizz`
`45` | `'FizzBuzz'`
`13` | `'13'`

**Hints:**\
Same again: `if`, `elif` and `else`. Just be careful you cover all the options and test them.

## get_sequence_as_str(an_int)

The parameter is guaranteed to be a positive integer greater than zero. Return a string containing the
integers 1 to an_int inclusive, separated by spaces.

parameter value | return value
:---------:|:-------:|
`1` | `'1'`
`2` | `'1 2'`
`5` | `'1 2 3 4 5'`

**Hints:**\
The first part of the problem is to generate the sequence from 1 to `an_int` inclusive. There many ways to
do this but two of the most straightforward are a `while` loop:

```python
an_int = 5  # this value will come from parameter
count = 0
while count < an_int:  # check this produces the correct sequence
    print(count, an_int)
```

Alternatively, a `for` loop using `range()`

```python
an_int = 5  # this value will come from parameter
for i in range(an_int):  # check this produces the correct sequence
    print(i, an_int)
```

Choose whichever you prefer, or even something else. Once you know how to generate the sequence of numbers
then you can work out how to assemble the string this function must return. Two useful facts: you can turn
anything into a string with `str(anything)` and you can add strings together to create bigger strings by
using `+`.

## get_sequence_as_list(an_int)

The parameter is guaranteed to be a positive integer greater than zero. Return a list containing the
integers 1 to an_int.

parameter value | return value
:---------:|:-------:|
`1` | `[1]`
`2` | `[1, 2]`
`5` | `[1, 2, 3, 4, 5]`
`11` | `[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]`

**Hints:**\
Same problem as the previous function except this time you need to return a list rather than a string.\
Create an empty list witht the statement `[]` and append items to the end of the list with the list
method `list.append()`

## get_sequence_as_set(an_int)

The parameter is guaranteed to be a positive integer greater than zero. Return a set containing the integers
1 to an_int.

parameter value | return value
:---------:|:-------:|
`1` | `{1}`
`2` | `{1' 2}`
`5` | `{1, 2, 3, 4, 5}`

**Hints:**\
Same problem as the previous function except this time you need to return a `set()` rather than a string.

## get_sequence_as_dict_v1(an_int)

The parameter is guaranteed to be a positive integer greater than zero. Return a dictionary containing the
integers 1 to an_int as the keys of the dictionary, all associated with a value of twice the key`.

parameter value | return value
:---------:|:-------:|
`1` | `{1: 2}`
`2` | `{1: 2, 2: 4}`
`5` | `{1: 2, 2: 4, 3: 6, 4: 8, 5: 10}`

**Hints:**\
Same problem as the previous function except this time you need to return a dictionary rather than a string.
This has the added complexity that every entry in a dictionary has two parts, a 'key' and an associated '
value'.\
The simplest approach is to create the dictionary first with the correct keys but all with just a single
default value. Then iterate through the dictionary, key-by-key, setting the 'value' part to the correct
value. You will find the dictionary methods you need in
the [Python dictionary documentation](https://docs.python.org/3/library/stdtypes.html#typesmapping)

## get_sequence_as_dict_v2(an_int)

The parameter is guaranteed to be a positive integer greater than zero. Return a dictionary containing the
integers 1 to an_int as keys. The value associated with each key should be the string returned by fizzbuzz()
.

parameter value | return value
:---------:|:-------:|
`1` | `{1: '1'}`
`2` | `{1: '1', 2: '2'}`
`3` | `{1: '1', 2: '2', 3: 'Fizz'}`
`5` | `{1: '1', 2: '2', 3: 'Fizz', 4: '4', 5: 'Buzz'}`

**Hints:**\
Same as get_sequence_as_dict_v1. Just a different value calculation for each key.

## get_all_chars(filename)

The parameter is guaranteed to be the name of a text file encoded as utf-8. Read the file and return the set
of all characters present in the file.

**Hints:**\
Read the file into a single string then convert that to a set.

## count_Q(filename);

The parameter is guaranteed to be the name of a text file encoded as utf-8. Read the file and count the
number of occurrences of the character '?' (a question mark, unicode 63 decimal or 3F hexadecimal).

file content | return value
:---------:|:-------:|
`question` | `0`
`?-?` | `2`
`any???thing` | `3`

**Hints:**\
Open the file with a `with open():` statement making sure to specify the encoding as `encoding='utf-8'`.
Read the whole file into a text string and then
use [string methods](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str) to get the
counts.

## count_and(filename)

The parameter is guaranteed to be the name of a text file encoded as utf-8. Read the file and count the
number of occurrences of each of the character strings `'and'`, `' and '`, and `' and, '`(the string 'and';
same but with spaces both sides; same again but with a space before and a comma and a space after). Ignore
the case of the text. Return the respective counts as integers.

file content | return value
:---------:|:-------:|
`''` | `0, 0, 0`
`'and and and, '` | `3, 1, 1`
`'Andover and shandy'` | `3, 1, 0`

**Hints:**\
Much the same as count_Q().

## write_Q_v1(an_int, filename)

The parameters are guaranteed to be a positive integer **greater than zero** and a legal filename. Write the
sequence of integers from 1 to an_int inclusive to the file, with each integer followed by the string '
? ' (space, question mark, space). The return value should be `an_int`, the integer passed in as a parameter
value.

parameter values | file content | return value
:---------:|:-------:|:----:
`1, 'file.txt'` | `1 ? `| `1`
`3, 'file.txt'` | `1 ? 2 ? 3 ? `| `3`
`5, 'file.txt'` | `1 ? 2 ? 3 ? 4 ? 5 ? `| `5`

**Hints:**\
A `for` or `while` loop to generate the sequence of integers, and the space-?-space while iterating.

## write_Q_v2(an_int, filename)

The parameters are guaranteed to be a positive integer **or zero** and a legal filename.

Create the file if it does not already exist and write `an_int` lines to the file. The structure of the
successive lines of the file is: the next integer in the sequence from 1 to an_int inclusive, followed by a
space, followed by that `an_int` number of successive '?' characters.

parameter value | file content
:---------:|:-------:|
`0` | empty
`1` | `1 ?`
`2` | `1 ?`<br/>`2 ??`
`5` | `1 ?`<br/>`2 ??`<br/>`3 ???`<br/>`4 ????`<br/>`5 ?????`

.\
.\
.\
.

# Section 2 - Extra Credit

These last questions are more difficult. They are not required for a 'good pass' grade. If you attempt them
I will mark your work and, providing you have completed section 1 to a good standard, I will award extra
credit

## get_all_words(infile, outfile)

The parameter is guaranteed to be the name of a text file encoded as utf-8. Read the file, replace all
punctuation with a space and write the result to outfile encoded as utf-8. I will test your implementation
using 244-0.txt so use that as your baseline for testing.

**Hints**\
This is trickier than it first seems as the answer depends entirely on what is defined as punctuation.
Symbols such as `! ? . ,` are not too problematic but apostrophes and single quotation marks can get
confused, as can hyphenated words, words hyphenated for page wrap and hyphens used as a general purpose
separator.

Rather than searching through a large outfile looking for 'punctuation' symbols that have slipped through,
think about writing a function that puts the words in outfile into a set, then you have a much smaller
collection to deal with

## get_all_non_ascii(filename)

The parameter is guaranteed to be the name of a text file encoded as utf-8. Read the file and return the set
of all non-ASCII characters present in the file. A non-ASCII character is one for which ord(character)
returns a value of outside the range 0-127 decimal.

## pluraliser(a_str)

The parameter is guaranteed to be a word. A string with no spaces. Return the plural of that word.

**Test Data**
Banana, Leaf, Trolley, Lorry, Sheep, Church, Sausage, Monkey, Knife, Child, Match, Poppy

## stemmer(a_str)

The parameter is guaranteed to be a word. A string with no spaces.

Industry Industries Industrial Industrious industrialise Industrialist Industrialising Industrialised
Industrialisation Deindustrialised Post-industrial Reindustrialised Unindustrialised 
