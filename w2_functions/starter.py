def two():
    """ Always return the integer 2  """
    return 2

def times2(a_value):
    """ Return twice a_value  """
    the_result = a_value + a_value
    return the_result

def times3(a_value):
    """ Return thrice a_value  """
    return a_value * 3

def first_last(a_string):
    return a_string[0] + a_string[-1]



# part II
def times5(a_number):
    """ Return five times a_number  """ 
    return times2(a_number) + times3(a_number)

def times6(a_number):
    """ Return six times a_number  """ 
    return times2( times3( a_number ) )
