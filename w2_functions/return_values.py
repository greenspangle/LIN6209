# exploring return values - part I

def no_return():
    """ no return statement"""
    pass

def empty_return():
    """an empty return statement"""
    return

def single_return():
    """a single return value"""
    return 'single value returned'

def many_return():
    """many return values, sperated by commas"""
    return 'as', 'many', 'values', 'as', 'is', 'needed'

print('types of objects returned',\
type(no_return()),
type(empty_return()),
type(single_return()),
type(many_return())
)
print()
print('len() of return values:',\
len(single_return()),
single_return()[7:12],
len(many_return()),
many_return()[2][3]
)

# exploring return values - part II
# functions returning functions

def nopoints():
    def inner_function():
        return 'zero points'
    return inner_function

print('testing the function returned by nopoints()')
f = nopoints()
print(\
type(f),
type(f()),
f()
)
