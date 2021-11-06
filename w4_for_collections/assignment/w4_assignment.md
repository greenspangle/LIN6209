# Week 4 Assignment

Design, build and test the following functions: _{updated 19+22 October 2021}_\
Submit your python script with the filename 'w4_yourID.py'.\

## signum(a_num)

If a_num is greater than zero return 1. If it's less than zero return integer minus one. Otherwise, return
integer zero.\
For example:

parameter values | return value
:---------:|:-------:|
`11` | `1`
`0.000702` | `1`
`-1/2` | `-1`
`0` | `0`

**Hints:**\
A few `if` statements should get the job done.

## middle(p1, p2, p3)

Return the middle value.\
All three parameters are guaranteed to be pairwise comparable using the operators <, <= !=, ==, >=, and >.\
For example:

parameter values | return value
:---------:|:-------:|
`1 , 2 , 3` | `2`
`2 , 3 , 1` | `2`
`'a' , 'x' , 'c'` | `'c'`
`'abra' , 'cad' , 'abra'` | `'abra'`

**Hints:**\
Use `if` statements with the logical operators `and`, `or` and `not`.\
Alternatively, you can solve this problem with a list and list methods - but I'll let you discover that
method for yourselves.

## isa_triangle(len1, len2, len3)

The three parameters are guaranteed to be numbers. If they are interpreted as the lengths of the sides of a
euclidean triangle, return an integer to indicate which type of triangle they would construct according to
this table:<br/><br/>

Return <br/>Value | Meaning
:---:|:----:
**0** | No triangle possible
**1** | Scalene
**2** | Isosceles
**3** | Equilateral

**Hints:**\
Triangles have three sides. If all are equal lengths then it's an equilateral. If only two are equal it's an
isosceles triangle. If all sides are different it's a scalene triangle. \
As with the first problem, `if / elif / else` statements combined with the boolean operators `and`, `or`
and `not` should do the job.\
Do remember though that there are four possibilities. For example what should `isa_triangle(2,17,2)` return?
If you can't see why that is a problematic triangle try sketching it to scale on a piece of paper.

## robberlingo(a_str)

Translate the text string `a_str` text into "rövarspråket" (Swedish for "robber's language"). That is,
double every consonant and place an occurrence of "o" in between. For example, translate("this is fun")
should return the string "tothohisos isos fofunon"

**Hints:**\
A consonant is any character in the alphabet `a..z` that is not a vowel. A vowel is any one of `'aeiou'`.
Create both of those as string variables. Might only need one, we can delete the other later.

The problem asks for a string containing the translation so start by creating an empty string to contain the
translation.

The question asks us to read each character of `a_str` in turn and act differently if the `current_char` is
a consonant or not.\

* Reading each character in turn is iteration and which means we need a `while` or a `for` loop.
* If the `current_character` in `a_str` is in `consonants` then
  add `current_character + 'o' + current_character` to the end of the translation so far
* If not, just add the `current_character`.

The keyword operator `in` can be used to test if a character is in a string. Try `'a' in 'syntax'` to see
how it works.

Here is some skeleton code you can build on:

```python
a_string = 'abracadabra'  # this will be provided by the function parameter
vowels = 'aeioi'
consonants = 'bcdfghjklmnpqrstvwxyz'  # check this is correct (I think it is)
translation = []
for current_char in a_string:
    # change this to the code that will build the translated string
    if current_char in consonants:
        print('add translated character to translation')
    else:
        print('just add character to translation')
```

When the `for` loop exits return the translated string.

## pangram(a_str):

Answer true if a_str is a pangram and false if not. Ignore capitalisation and punctuation, only consider the
characters a-z.\
For example:

parameter values | return value
:---------:|:-------:|
`'the quick brown fox jumps over the lazy dog'` | `True`
`'the quick brown fox jumped over the lazy dog'` | `False`

**Hints:**\
A pangram is a phrase that contains all the letters of the alphabet from 'a' to 'z' at least once. Other
characters in the phrase are effectively ignored. As long as a_str contains all the characters of the
alphabet, it's a pangram.

The question says to ignore capitalisation so a good first step is to convert str_1 to lower case with the
lower() or casefold() string methods described
at [Python.org Text Sequence Type - str](https://docs.python.org/3/library/stdtypes.html#str) and
at [w3schools](https://www.w3schools.com/python/python_strings_methods.asp).

As repetitions make no difference to a phrase being a pangram or not, and sets ignore repetitions, they are
probably going to be useful in solving this problem. Logically, if all the characters in a_str are placed in
a set and that set contains every letter in the alphabet, then a_str is a pangram. That sounds like a way to
solve the problem so let's try it.

Start by creating two sets:

* A set containing all the characters in a_str.
* A set containing all the letters of the alphabet `'abc ... xyz'`.

To explore how to create these sets start IDLE and execute the statement `set('foobar')` and see what you
get.

The next step is to remove every character in set of characters in a_str from the alphabet set and check how
many characters are left. If the answer is none then a_str must contain every letter in the alphabet and
hence is a pangram.

Problem solved - provided sets can be 'subtracted' and there is a way of determining if a set is empty.

Subtracting one set from another is one of
the [set methods and operations](https://docs.python.org/3/library/stdtypes.html#set-types-set-frozenset).
Scan through the list of methods and operations available and you should soon spot how to do it.
Alternatively, just try subtracting one set from another in IDLE and see what the result is.

The built-in function `len()` returns the number of elements in a collection. It works on sets just as well
as it does strings.

## merge2(str1, str2)

Interleave the successive characters of **two** strings of the same length into a single string and return
the result.\
For example:

parameter values | return value
:---------:|:-------:|
`'' , ''` | `''`
`'a' , 'x'` | `'ax'`
`'abc' , 'def'` | `'adbecf'`

**Hints:**\
Strings can be indexed: `s[0]` is the first character, `s[1]` the second, `s[2]` the third and so on.
Extending that logic to two lists is easy: `str_1[0]` and `str_2[0]`, then `str_1[1]` and `str_2[1]`,
then `str_1[2]` and `str_2[2]`, and so on.

The key to this problem is instead of iterating through the successive characters of the strings, iterate
through the index numbers that can be used to access the characters of the two strings. As indexing applies
to all strings these integer index values will enable synchronised access to BOTH strings at the same time.

How best to generate that sequence of index numbers? We could use a `while` loop with a counter but far
easier is to use a `range()` object and combine that with a `for` loop. Here is the beginnings of some
skeleton code. Execute it in IDLE to understand what it is doing:

```python
for index in range(11):
    print(index, index)
```

We are now in a position to solve the problem:

* Replace the `11` with the length of the strings by using `len(str_1)` (either will do as they are both the
  same length)
* Create a variable to contain the result string `result_str = ''`
* On every iteration of the `for` loop add the indexed characters from both strings to the end
  of `result_str`

Here an outline for you to build upon.

```python
str_1 = 'abc'  # dummy value. This will be parameter value
str_2 = 'xyz'  # dummy value. This will be parameter value
length_of_str = len(str_1)  # either will do as they are guaranteed to be same length
result_str = ''
for index in range(length_of_str):
    print(str_1[index] + str_2[index])  # change this to code to modify result_str
```

Replace the print() statement with your code to add the two characters from str_1 and str_2 to `result_str`,
wrap it in a function, remove my two dummy strings and use parameters instead, test the final code, and
done.

## merge3(str1, str2, str3)

Interleave the successive characters of **three** strings of the same length into a single string and return
the result.\
For example:

parameter values | return value
:---------:|:-------:|
`'', '', ''` | `''`
`'a',  'b',  'c'` | `'abc'`
`'abc',  'def',  'ghj'` | `'adgbehcfj'`

**Hints:**\
Same logic and design as for merge2(). The only difference is that this time there are now three strings
instead of two.

## letter_count(a_str)

Return a dictionary with every character (including spaces and punctuation) in a_str as a key in the
dictionary with a value equal to the number of occurrences of that character in a_str. Only characters in
a_str are keys in the returned dictionary.

For example:

parameter values | return value
:---------:|:-------:|
`''` | `{}`
`'a'` | `{'a' : 1}`
`'aaa'` | `{'a' : 3}`
`'abbabab'` | `{'a' : 3, 'b': 4}`
`'abracadabra'` | `{'a' : 5, 'b': 2, 'c': c, 'd': c}`

**Hints:**\
First create a dictionary to contain the result. There are several ways to do this but the easiest options
are probably `d = dict()` which creates an empty dictionary and `d = dict.fromkeys('abcd', 0)` which creates
a dictionary with a _key_ for every character in `'abcd'` associated with a _value_ of `0`. Try both in IDLE
to explore what they do and decide which is best for this problem.

Now that the dictionary is created, we need to iterate through a_str and update the values associated with
each letter. A `for` loop is ideal for this. For each of the characters look up its entry in the dictionary
and increment its value by 1. Something like the code I have outlined below should do the job:

```python
a_str = 'abracadabra'  # parameter value
char_count_dict = dict.fromkeys(a_str)
for char in a_str:
    # get current value in char_count_dict for char
    #     char_count_dict[char]
    # and increment its value by 1
    #     char_count_dict[char] = previous value + 1
    pass  # dummy statement just to make my syntax correct
# and that's it so just return the dictionary char_count
```

Find the dictionary methods you need
at [Python.org dictionary](https://docs.python.org/3/library/stdtypes.html#mapping-types-dict)
or on [W3Schools.com dictionaries](https://www.w3schools.com/python/python_dictionaries_change.asp).

# Too difficult for now - NOT assessed

These last questions are not assessed. I have left them in this script only so that you have continuity with
the previous version. If you attempt them I will mark your work, but you suffer no penalty for not doing
them.

## runup(a_str)

The parameter a_str is guaranteed to be a string made entirely of alphanumeric [a...z][0...9] characters.
Answer the starting position and length of the longest non-decreasing substring within a_str. If there are
multiple such substrings, report the first. If a_str is empty return (
-1, 0).\
For example:

parameter values | return value | substring
:---------:|:-------:|:---:
`''` | `-1, 0` | `''`
`'z'` | `0, 1` | `'z'`
`'ababcb'` | `2, 3` | `'abc'`
`'bus27herenow'` | `1, 4` | `'us27'`
`'bus21herenow'` | `8, 4` | `'enow'`
`'27991'` | `0, 4` | `'2799'`

**Hints:**\
_There are many ways to solve this problem. This is just one._

It is often very helpful when trying to solve these more difficult problems to first try and think how it
might be solved with 'paper & pencil'. Doing that 'paper & pencil' exercise (yes I actually did do that)
shows that just one iteration through the list is all that is needed but there are several things to keep
track of at the same time which means it can be tricky keeping everything synchronised.

Starting from the assumption that it would be a `for` loop, the items to keep track of are:

Variable | meaning
---|---
current_char | the character currently being evaluated<br/> in this iteration of the `for` loop
previous_char| the immediately preceding character in `a_str`
current_longest| the characters in this current non-decreasing run
previous_longest| the longest sequence of non-decreasing<br/> characters found so far

To start with these are all empty so create them and make them all equal to the empty string `''`.

Next, iterate through `a_str` with a `for` loop. Something like this:

```python
a_str = 'abracadabra'  # in the function this will be the parameter value
current_char = ''
previous_char = ''
current_longest = ''
previous_longest = ''
for current_char in a_str:
    ## do things
    print(current_char)  # just a placeholder    
```

Inside the `for` loop we need an `if` statement to cope with two alternative situations:

1. The current non-descending sequence has ended because `current_char` < `previous_char`.<br/>Set
   the `current_longest` to just the `current_char`
2. The current non-decreasing sequence is still OK because `current_char` >= `previous_char`. <br/> The
   current run is still good so add the `current_char` to the end of the `current_longest`.<br/> Compare the
   current_longest to the previous_longest and if it's longer make it the `previous_longest`.

After the `if` statement assign `current_char` to `previous_char` because it needs to be available for the
next iteration.

When the for loop finishes the longest run will be held in the variable `previous_longest`.

The question asks for the starting position of the longest run. We could do that by iterating
through `a_str` again to look for it, but there is an easier way - use the string method `find()`. The
question also asks for the length of the longest run - but that's easy, just use `len()`.

```
result = a_str.find(previous_longest), len(previous_longest)
```

This code works for all inputs EXCEPT for the empty string. To fix that add an `if` statement to check:

```
if a_str == '':  # parameter value is empty string
    result = (-1, 0)
```

Finally, add `return result` statement to function

## mergen_short()

Interleave the successive characters of **any number** of strings of **any length** into a single string and
return the result.\
Interleaving is halted when the shortest string is exhausted.\
For example:

parameter values | return value
:---------:|:-------:|
`'', '', ''` | `''`
`'abc',  'd',  'ef'` | `'ade'`
`'abc_', 'defg', 'hjkmn', 'pqr', 'stuv'` | `'adhpsbejqtcfkru'`

**Hints:**\
The problem has many similarities to the previous `mergeX()` problems but this time there can be any number
of parameter strings, and they can all be different lengths. So some immediate problems to solve are:

1. How do functions that take any number of parameters work?
2. How to stop the iteration when the shortest string is exhausted?
3. How to merge an arbitrary number of strings?

Functions that take an arbitrary number of argument parameters are described in the Python tutorial
at [4.8.4. Arbitrary Argument Lists](https://docs.python.org/3/tutorial/controlflow.html#arbitrary-argument-lists)
and at [w3schools](https://www.w3schools.com/python/python_functions.asp) (a little way down the page). The
short explanation is that the function definition should look like:

```python
def f_name(*args):
    # code
    return 
```

The strings will then be available within the function body as the elements of a list called `args`. So this
function will have an outline structure like this:

```python
def merge_short(*args):  # 'args' is traditional, it can be any variable name
    # args is now available as a variable within the function body
    # args is a list of the strings to be interleaved
    result_str = []  # destination for result
    # code goes here . . . 
    return result_str
```

For part (2) we need to find the shortest string in the list of strings in `args`. There are many ways to do
this but perhaps the simplest is to create another list and put all the lengths of the strings in that. Then
we can use the built-in function `min()` to evaluate `min(list_of_lengths)`. Some code along the lines of
this should do the job:

```python
args = ['1st str', 'next str', 'one after that']  # this is just an example, args is automatically created 
list_of_lengths = []  # the list of string lengths will go here
for each_string in args:
    list_of_lengths.append(len(each_string))
# all the lengths of all the strings in args are now in list_of_lengths
shortest_string_length = min(list_of_lengths)
```

The answer to part (3) is that as all the strings are in a single list, we can use a `for` loop
with `range()` to iterate through it, adding one character from each successive string as the list is
traversed. Something like:

```
result = []
for index in range(shortest_string_length):
    for each_str in args:
        result.append(each_str[index])
# for loops ended. Assemble list of characters in result into a single string
result = ''join(result)
# and return the result
```

## mergen_long()

Interleave the successive characters of **any number** of strings of **any length** into a single string and
return the result.\
As individual strings become exhausted, continue interleaving with the remaining strings until all are
exhausted.\
For example:

parameter values | return value
:---------:|:-------:|
`'', '', ''` | `''`
`'abc',  'd',  'ef'` | `'adebfc'`
`'abc_', 'defg', 'hjkmn', 'pqr', 'stuv'` | `'adhpsbejqtcfkru_gmvn'`

**Hints:**\
Much of the structure of the function mergen_long()is similar to mergen_short() but with an additional check
before a character is added to the result.\
The value of the variable `index` used to access elements of the strings will start at zero and successively
increment to the last element of the longest string. Because some strings may be shorter than the longest
string, we need to check that `[index]` is not beyond the end of the string before attempting to access any
string. 