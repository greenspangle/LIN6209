def datafile(a_str, f_name='test_data.txt', mode='wt', encoding='utf-8'):
    """Create a file with suitable content for testing."""
    with open(f_name, mode=mode, encoding=encoding) as tf:  # open the file
        tf.write(a_str)  # write content
    # file automatically closed
    return f_name  # return the name of the file
