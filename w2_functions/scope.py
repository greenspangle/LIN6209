# define a variable that is external to all functions
a = 5

# and now explore what happens when we use the same name INSIDE function definitions
def scope1():
    """return the variable 'a' that exists only in external namespace"""
    return a

def scope2():
    """define and return an internal variable 'a'
    This masks/hides the the external name 'a' and its value.
    After executing this function the value of external 'a' is unaffected"""
    a = 27
    return a

def scope3():  # throws syntax error when called
    """Attempt to increment value of variable named 'a'
    This fails with syntax error "local variable 'a' referenced before assignment"

    Reading the expression left to right (as Python does) we are asking Python to
    create a variable named 'a' which masks external 'a' and then assign it a
    value of one more than its current value. But at that point the new 'a' doesn't
    properly exist and certainly doesn't have a value - hence Python objects that
    we are trying to use (reference) 'a' before it has been assigned a value"""
    a = a + 1
    return a

def scope4():  # use of the global keyword is a rich source of bugs - AVOID 
    """Use of the 'global' keyword to link the name 'a' to external scope.
    The variable name 'a' can be used and assigned values but it is actually
    changing the external 'a'
    Check the value of external 'a' after running this function"""
    global a
    a = a + 1
    return a
