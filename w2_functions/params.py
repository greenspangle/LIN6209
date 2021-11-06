# exploring parameters - part I

def parms_v1(num1, num2, num3):
    """ there can be any number of parameters """
    return num1 + (num2 * num3)

def parms_v2(num1, num2, num3 = 1):
    """ Third parameter is optional """ 
    return num1 + (num2 * num3)

print('Testing params_v2.py,', \
parms_v2(4,5,6),
parms_v2(4,5),
parms_v2(1, num3 = 0, num2 = 11),
parms_v2(0, 17, 2),
parms_v2(num2 = 17, num3 = 2, num1 = 0)\
)



# exploring parameters - part II
def mod00hash(object1, hash=hash):
    return hash(object1)%100

print('Testing mod00hash.py',\
mod00hash(5),
mod00hash('5'),
mod00hash('six'),
mod00hash('six', hash),
mod00hash('six', id)
)



