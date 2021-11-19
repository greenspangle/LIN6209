def datafile(a_str, f_name='test_data.txt', mode='wt', encoding='utf-8'):
    """Create a file from a string and return the file name."""
    with open(f_name, mode=mode, encoding=encoding) as tf:  # open the file
        tf.write(a_str)  # write content
    # file automatically closed at end of indentation block
    return f_name  # return the name of the file
