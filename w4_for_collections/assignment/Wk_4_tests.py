# Week 4 Assignment
from assignments.week4.Patti_Bilas_17752225_assignsubmission_file_.w4_190254812    import *


def test_signum():
    assert signum(11) == 1
    assert signum(0.000702) == 1
    assert signum(0) == 0
    assert signum(-0) == 0
    assert signum(-1 / 2) == -1
    assert signum(-11) == -1


def test_middle():
    """In theory should also test for negative numbers - but not now"""
    assert middle(0, 0, 0) == 0
    assert middle(1, 1, 1) == 1
    assert middle(3, 3, 3) == 3
    assert middle(3, 3, 2) == 3
    assert middle(3, 2, 3) == 3
    assert middle(2, 3, 3) == 3
    assert middle(1, 2, 3) == 2
    assert middle(2, 3, 1) == 2
    assert middle(1, 3, 2) == 2
    assert middle('a', 'x', 'c') == 'c'
    assert middle('abra', 'cad', 'abra') == 'abra'


def test_isa_triangle():
    """Should really test for sides of zero value? Better - write a tighter function definition."""
    assert isa_triangle(1, 1, 1) == 3
    assert isa_triangle(55, 55, 55) == 3
    assert isa_triangle(2, 2, 1) == 2
    assert isa_triangle(2, 1, 2) == 2
    assert isa_triangle(1, 2, 2) == 2
    assert isa_triangle(3, 4, 5) == 1
    assert isa_triangle(2, 17, 2) == 0


def test_robberlingo():
    assert robberlingo('') == ''
    assert robberlingo('this is fun') == 'tothohisos isos fofunon'
    assert robberlingo('here is some robberlingo') == \
           'hoherore isos sosomome rorobobboberorlolinongogo'


def test_pangram():
    assert pangram('the quick brown fox jumps over the lazy dog') == True
    assert pangram('The quick brown Fox jumps over the lazy Dog') == True  # ignore capitalisation
    assert pangram('the quick brown fox, jumps over the lazy dog.') == True  # ignore punctuation
    assert pangram('The quick brown Fox jumps over the lazy Dog!') == True  # ignore both caps and punctuation
    assert pangram('the quick brown fox jumped over the lazy dog') == False


def test_merge2():
    assert merge2('', '') == ''
    assert merge2('a', 'x') == 'ax'
    assert merge2('abc', 'def') == 'adbecf'


def test_merge3():
    assert merge3('', '', '') == ''
    assert merge3('a', 'b', 'c') == 'abc'
    assert merge3('abc', 'def', 'ghj') == 'adgbehcfj'


def test_letter_count():
    assert letter_count('') == {}
    assert letter_count('a') == {'a': 1}
    assert letter_count('aaa') == {'a': 3}
    assert letter_count('abbabab') == {'a': 3, 'b': 4}
    assert letter_count('abracadabra') == {
        'a': 5, 'b': 2, 'r': 2, 'c': 1, 'd': 1}


"""
Too difficult for now - NOT assessed
These last questions are not assessed. I have left them in this script only so that you have continuity 
with the previous version. If you attempt them I will mark your work, 
but you suffer no penalty for not doing them.
"""


def test_mergen_short():
    """Also perhaps ('', '', 'a') and ('', 'b', 'ac')"""
    assert mergen_short('', '', '') == ''
    assert mergen_short('abc', 'd', 'ef') == 'ade'
    assert mergen_short('abc', 'de', 'fghi') == 'adfbeg'
    assert mergen_short('abc_', 'defg', 'hjkmn', 'pqr',
                        'stuv') == 'adhpsbejqtcfkru'


def test_mergen_long():
    """same comment as for _short()"""
    assert mergen_long('', '', '') == ''
    assert mergen_long('abc', 'd', 'ef') == 'adebfc'
    assert mergen_long('abc_', 'defg', 'hjkmn', 'pqr',
                       'stuv') == 'adhpsbejqtcfkru_gmvn'


def test_runup():
    result = runup('')  # ''
    assert result == (0, -1)
    result = runup('z')  # 'z'
    assert result == (0, 1)
    result = runup('ababcb')  # 'abc'
    assert result == (2, 3)

