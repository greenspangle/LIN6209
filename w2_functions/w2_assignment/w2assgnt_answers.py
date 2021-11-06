""""PMcG answers to LIN6209 Week 2 Assignment."""


def magic7():
    """This function answers the integer 7 every time it is called"""
    return 7


def times2(parameter):
    """ This function takes any number or string and returns twice the value."""
    return parameter * 2  # '2 * parameter' does not work with strings!


def all_ops_pt1(int1, int2):
    """ This function returns the tuple int1 operator int2 for each od +, -, *, /, //, %"""
    return int1 + int2, int1 - int2, int1 * int2, int1 / int2, int1 // int2, int1 % int2


def all_ops_pt2(int1, int2):
    """ Same as all_ops_pt1 but this time with the operators <, <=, ==, !=, >=, and > """
    return int1 < int2, int1 <= int2, int1 == int2, int1 != int2, int1 >= int2, int1 > int2


def magic_number(a_num):
    """ Return True if a_num contains the digit 7 when written in denary notation, otherwise false."""
    return '7' in str(a_num)


def hms_to_s(hours, minutes, seconds):
    """Return the duration hours:minutes:seconds as seconds."""
    hours_as_seconds = hours * 60 * 60
    minutes_as_seconds = minutes * 60
    total_seconds = hours_as_seconds + minutes_as_seconds + seconds
    return total_seconds


def s_to_hms(seconds):
    """Convert a duration in seconds to hours:minutes:seconds in standard form."""
    # determine the number of whole hours in the given seconds, and the remaining seconds
    hours = seconds // (60 * 60)
    remaining_seconds = seconds % (60 * 60)  # or = seconds - hours*60*60
    # from the seconds remaining after hours have been extracted
    # extract the whole minutes and a new remaining seconds
    minutes = remaining_seconds // 60  # whole minutes left in remaining seconds after whole hours removed
    remaining_seconds = remaining_seconds - minutes * 60  # alternatively remaining_seconds = seconds % 60
    # and now we have all the component parts of the answer
    return hours, minutes, remaining_seconds  # return the result as


def add_hms(hr1, min1, sec1, hr2, min2, sec2):
    """Add two hour:minute:seconds time durations and answer the sum in standard form."""
    # convert both durations to seconds
    seconds1 = hms_to_s(hr1, min1, sec1)
    seconds2 = hms_to_s(hr2, min2, sec2)
    # add them together to get total seconds
    total_seconds = seconds1 + seconds2
    # convert back (h, m, s) tuple
    hms = s_to_hms(total_seconds)
    # and that's the result - so return it :-)
    return hms


def add_old_uk(pounds1, shillings1, pennies1, pounds2, shillings2, pennies2):
    """Add two pre-decimalisation amounts of UK currency"""
    # convert everything to pennies
    total_pennies = (pounds1 * 20 * 12 + shillings1 * 12 + pennies1) + \
                    (pounds2 * 20 * 12 + shillings2 * 12 + pennies2)
    # use modular arithmetic to convert that back to £SD
    whole_pounds = total_pennies // (20 * 12)  # whole pounds in that many pennies
    remaining_pennies = total_pennies % (20 * 12)  # and this many pennies left over
    whole_shillings = remaining_pennies // 12  # whole number of shillings after the whole pounds taken away
    remaining_pennies = remaining_pennies % 12  # and this is the pennies remaining at the end
    whole_pennies = remaining_pennies  # just wanted the return value names to be symmetrical
    # now just assemble the result from its parts and return it
    return whole_pounds, whole_shillings, whole_pennies


def lucky_fun(outer_int):
    """ Returns a function that accepts an int or float and answers True if the sequence of digits lucky_int occurs
    within its parameter value when both are written in denary notation, False otherwise."""

    # create the function to return
    def inner_function(inner_num):
        # transform both parameters to strings
        str_outer_int = str(outer_int)
        str_inner_num = str(inner_num)
        # the inner_num string may contain a decimal point so replace it with empty string
        str_inner_num = str_inner_num.replace('.', '')
        # Use the 'in' operator to check if str_lucky_int is present in str_inner_int
        result = str_outer_int in str_inner_num  # this evaluates to True or False
        return result

    # that's the required function constructed, now just return it to the calling code
    return inner_function


def rearranged(phrase1, phrase2):
    """  Answer True if parameters are anagrams. False otherwise."
    1. ANALYSIS
        Two strings are anagrams of each other if they contain the same letters, just in a different order.
    2. DESIGN
        remove spaces and capitalization
        sort letters into same order
        compare for equality
    3. WRITE CODE"""
    # first step = remove spaces (replace every single space with empty string)
    phrase1 = phrase1.replace(' ', '')
    phrase2 = phrase2.replace(' ', '')
    # second step = make lower case
    phrase1 = phrase1.lower()
    phrase2 = phrase2.lower()
    # third step = sort constituent characters into order
    phrase1 = sorted(phrase1)
    phrase2 = sorted(phrase2)
    # fourth step = turn sorted phrases back into strings (unnecessary, could compare now)
    phrase1 = str(phrase1)
    phrase2 = str(phrase2)
    # fifth step = now at last we can compare them
    result = (phrase1 == phrase2)  # evaluates to True or False
    return result  # and return the result to caller


def is_back_to_front_v1(phrase):
    """ If, ignoring spaces, parameter reads the same backwards as forwards return boolean True, else False."""
    # first step = remove spaces
    phrase = phrase.replace(' ', '')  # replaces every single-space with no-space empty string
    # second step = make lower case
    phrase = phrase.lower()
    # third step = reverse the phrase
    phrase_reversed = phrase[::-1]
    # Compare phrase and phrase_reversed for equality and return result
    return phrase == phrase_reversed


def is_back_to_front_v2(phrase):
    """ If, ignoring spaces, parameter reads the same backwards as forwards return boolean True, else False."""
    # first step = remove spaces
    phrase = phrase.replace(' ', '')  # replaces every single-space with no-space empty string
    # second step = make lower case
    phrase = phrase.lower()
    # third step = reverse the phrase
    phrase_reversed = reversed(phrase)  # found this built-in function that seems to do the job
    # according to the documentation reversed() has created an 'iterator' that will go backwards through phrase.
    # So searched str methods for methods that accept 'iterators' and output strings: str.join() does this
    # BUT it's a string method so has to be in form '_a_string'.join(phrase_reversed)
    # Some experimentation in python shell reveals answer is:
    phrase_reversed = ''.join(phrase_reversed)  # required string is empty string ''
    # now, at last, phrase and phrase_reversed are both strings so can be compared for equality.
    # If they are equal this will return True, else False
    return phrase == phrase_reversed


is_back_to_front = is_back_to_front_v1  # chose the simplest option as final answer
