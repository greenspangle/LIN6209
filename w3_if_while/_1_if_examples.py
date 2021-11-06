# You can type 'if' statements directly into the IDLE interactive shell and execute them.
# Try this:

#       >>> if 'three' > 'four':
#               print(“ 'three' > 'four' “)


# Wrapping a simple if statement into a function definition
def my_max_v1(a, b):
    """my first version of the built in max() function """
    if a > b:
        return a
    if b >= a:
        return b


def my_max_v2(a, b):
    """my second version of the built in max() function """
    if a > b:
        return a
    return b


def my_max_v3(a, b):
    """my third version of the built in max() function
    ### This executes OK but is FAULTY ### - what's wrong with it?"""
    if a > b:
        result = a
    result = b
    return result


my_max = my_max_v2


# test this works with (3,4), (‘three’,‘four) and other values

######################################################
# Define an equivalent of the built-in min() function.
def my_min(a, b):
    if a < b:
        return a
    return b


# more warm-up tasks for w3 = if, while & boolean algebra

def grade_v1(mark):
    """ Pass or Fail """
    if mark > 60:
        return 'Pass'
    return 'Fail'


def weather_v1(a_str):
    """ take umbrella? """
    if 'rain' in a_str:
        return 'Take umbrella'


def weather_v2(a_str):
    """ take umbrella? """
    if 'sun' in a_str:
        return 'Take sunscreen'


def exec_decider(deadline_today=True):
    if deadline_today:
        return 'Do it now!'
    return 'mañana'

# try this in the IDLE interactive shell
if 'three' > 'four':
    print("'three' is greater than 'four'")

# here is something a bit more challenging
def is_weekend_v1(day='Sunday'):
    """Is it the weekend yet?"""
    # This is a basic effort - can you improve it so that it works correctly?
    # create necessary internal constants
    weekdays = 'Monday Tuesday Wednesday Thursday '
    weekend = 'Friday Saturday '
    rest_day = 'Sunday '
    days_of_week = weekdays + weekend + rest_day
    # and now decide if it's a weekday, weekend, or rest day.
    day = day.capitalize()
    if day in weekdays:
        return 'weekday'
    if day in weekend:
        return 'weekend'
    if day in rest_day:
        return 'rest day'
