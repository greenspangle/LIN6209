a=5

def scope2():
    """define and return an internal variable 'a'
    This masks/hides the external name 'a' and its value.
    After executing this function the value of external 'a' is
    unaffected"""
    a = 27
    return a
