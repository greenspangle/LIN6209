def lucky_fun(an_int):
     """ This function accepts an integer parameter (outer_int) and returns a function.
    The returned function accepts an int or float parameter (inner_num) and answers boolean True if the
    sequence of digits in outer_int occurs within inner_num, False otherwise. """
    def lucky_fun(an_int):
        lucky_fun = set(str(an_int))
        def unlucky_fun(inner_num):
            unlucky_fun = set(str(inner_num))
            if str(an_int) in str(inner_num):
                print ("True")
            else:
                print ("False")
        return (unlucky_fun)

