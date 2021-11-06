

def print_vowels(a_str='the quick brown fox jumps over the lazy dog'):
    """Print the vowels and spaces, every other character print as underscore"""
    vowels = 'a e i o u'
    index = 0
    while index < len(a_str):
        if a_str[index] in vowels:
            print(a_str[index], end=' ')
        else:
            print('_', end=' ')
        index = index + 1
