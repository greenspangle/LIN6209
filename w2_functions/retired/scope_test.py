a=5

def scope1():
    return a

def scope2():
    a = 27
    return a

def scope3():
    a = a + 1
    return a

def scope4(a):
    a = a + 1
    return a
