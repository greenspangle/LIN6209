# the import statement
import starter

def times4(a_value):
    """demonstrate use of imported function"""
    return starter.times2(a_value)+starter.times2(a_value)

def times7(a_value):
    return starter.times3(a_value) + times4(a_value)

def times11(a_value):
    return times4(a_value) + times7(a_value)

def times99(a_value):
    nine_times = starter.times3(starter.times3(a_value))
    return times11(nine_times)

if __name__ == '__main__':
    a_var = 1
    print(times4(a_var),times7(a_var), times11(a_var),times99(a_var))
