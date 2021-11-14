# Week 4 Assignment
import w6_assignment_solution as tutor
from w6_assignment_solution import *
from w6_tests_helper_functions import datafile


def test_thermostat():
    # given examples
    assert thermostat(21) == 'stat'
    assert thermostat(16) == 'on'
    assert thermostat(34) == 'off'
    assert thermostat(19) == 'stat'
    assert thermostat(24) == 'stat'
    # a few extremes
    assert thermostat(-999) == 'on'
    assert thermostat((19 + 24) / 2) == 'stat'
    assert thermostat(+999) == 'off'


def test_score_2():
    assert score_2(1, 5) == 6
    assert score_2(5, 1) == 6
    assert score_2(3, 4) == 14
    assert score_2(5, 2) == 14
    assert score_2(2, 2) == 6
    assert score_2(6, 6) == 24


def test_score_4():
    assert score_4(1, 5, 6, 6) == 7
    assert score_4(3, 2, 3, 3) == 2
    assert score_4(2, 6, 1, 5) == 14
    assert score_4(1, 1, 2, 6) == 7
    assert score_4(1, 2, 3, 4) == 1
    assert score_4(3, 3, 3, 4) == 7
    assert score_4(3, 3, 4, 4) == 21
    assert score_4(4, 3, 3, 4) == 21


def test_fizzbuzz():
    assert fizzbuzz(1) == '1'
    assert fizzbuzz(5) == 'Buzz'
    assert fizzbuzz(33) == 'Fizz'
    assert fizzbuzz(45) == 'FizzBuzz'
    assert fizzbuzz(13) == '13'


def test_num_seq_str():
    assert num_seq_str(1) == '1'
    assert num_seq_str(2) == '1, 2'
    assert num_seq_str(5) == '1, 2, 3, 4, 5'
    # other tests
    assert num_seq_str(11) == '1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11'
    assert num_seq_str(0) == ''
    assert num_seq_str(-9) == ''


def test_num_seq_list():
    assert num_seq_list(1) == [1]
    assert num_seq_list(2) == [1, 2]
    assert num_seq_list(5) == [1, 2, 3, 4, 5]
    assert num_seq_list(11) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
    assert num_seq_list(0) == []
    assert num_seq_list(-9) == []


def test_num_seq_set():
    assert num_seq_set(1) == {1}
    assert num_seq_set(2) == {1, 2}
    assert num_seq_set(5) == {1, 2, 3, 4, 5}
    assert num_seq_set(11) == {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11}
    assert num_seq_set(0) == set()
    assert num_seq_set(-9) == set()


def test_num_seq_dict():
    assert num_seq_dict(1) == {1: '1'}
    assert num_seq_dict(2) == {1: '1', 2: '2'}
    assert num_seq_dict(3) == {1: '1', 2: '2', 3: 'Fizz'}
    assert num_seq_dict(5) == {1: '1', 2: '2', 3: 'Fizz', 4: '4', 5: 'Buzz'}
    assert num_seq_dict(15) == {1: '1', 2: '2', 3: 'Fizz', 4: '4', 5: 'Buzz',
                                6: 'Fizz', 7: '7', 8: '8', 9: 'Fizz', 10: 'Buzz',
                                11: '11', 12: 'Fizz', 13: '13', 14: '14', 15: 'FizzBuzz'}


def test_get_chars_set():
    assert get_chars_set(datafile('')) == set()
    assert get_chars_set(datafile('abc 123')) == set('abc 123')
    assert get_chars_set(datafile('~abc+cab~')) == set('~abc+cab~')
    assert get_chars_set(datafile('\t\n\n')) == set('\t\n\n')


def test_count_chars():
    assert count_chars(datafile('')) == 0
    assert count_chars(datafile('abc 123')) == 7
    assert count_chars(datafile('~abc+cab~')) == 9
    assert count_chars(datafile('\t\n\n')) == 3


def test_count_Q():
    assert count_Q(datafile('')) == 0
    assert count_Q(datafile('?-?')) == 2
    assert count_Q(datafile('?-?-?')) == 3
    assert count_Q(datafile('any???thing')) == 3


def test_count_and():
    assert count_and(datafile('')) == (0, 0, 0)
    assert count_and(datafile('and and and, ')) == (3, 1, 1)
    assert count_and(datafile('Andover and shandy')) == (3, 1, 0)
    assert count_and(datafile('')) == (0, 0, 0)


def test_count_words():
    assert count_words(datafile('')) == 0
    assert count_words(datafile('abc 123')) == 2
    assert count_words(datafile('abc     123    \n\t    xyz')) == 3


def test_char_frequency():
    assert char_frequency(datafile('')) == {}
    assert char_frequency(datafile('abc')) == {'a': 1, 'b': 1, 'c': 1}
    assert char_frequency(datafile('abc ab a d')) == {'a': 3, 'b': 2, 'c': 1, 'd': 1, ' ': 3}
    assert char_frequency(datafile('abc     123    \n\t\n    23b')) == {
        'a': 1, 'b': 2, 'c': 1, ' ': 13, '1': 1, '2': 2, '3': 2, '\n': 2, '\t': 1}


def test_word_frequency():
    assert word_frequency(datafile('')) == {}  # empty dictionary
    assert word_frequency(datafile('abc 123')) == {'abc': 1, '123': 1}
    assert word_frequency(datafile('abc     123    \n\t    xyz')) == {'abc': 1, '123': 1, 'xyz': 1}
    assert word_frequency(datafile('abc     123    \n\t    abc xyz')) == {'abc': 2, '123': 1, 'xyz': 1}


def test_average_word_length():
    assert average_word_length(datafile('')) == 0
    assert average_word_length(datafile('abc def xyz')) == 3
    assert average_word_length(datafile('Andover and shandy')) == (16 / 3)


def test_text_analysis_01():
    assert text_analysis_01(datafile('')) == (0, 0, 0, 0)
    assert text_analysis_01(datafile('abc')) == (1, 1, 3, 0)
    assert text_analysis_01(datafile('\t \t \n')) == (0, 0, 0, 5)
    assert text_analysis_01(datafile('abc def. \tdef?\tghi jk!')) == (3, 5, 17, 5)


def test_write_Q():
    # name and create the two output files, one by student, one by tutor
    s_file = 's_file.txt'
    t_file = 't_file.txt'
    # run the test for integer values 1, 3, and 5
    print()  # this just keeps output looking tidy
    for i in [1, 3, 5]:
        print('Testing for an_int =', i)
        write_Q(i, s_file)
        tutor.write_Q(i, t_file)
        with open(s_file) as sf, open(t_file) as tf:
            # read and compare the successive lines of both files
            for s_line in sf:  # for each line is students file
                t_line = tf.readline()  # read a line of tutors file
                assert s_line == t_line  # and test that they are equal


def test_write_ints():
    # exactly the same structure as before
    # name and create the two output files, one by student, one by tutor
    s_file = 's_file.txt'
    t_file = 't_file.txt'
    # run the test for various integer values
    print()  # this just keeps output looking tidy
    for i in [0, 1, 2, 5]:
        print('Testing for an_int =', i)
        write_ints(i, s_file)
        tutor.write_ints(i, t_file)
        with open(s_file) as sf, open(t_file) as tf:
            # read and compare the successive lines of both files
            for s_line in sf:  # for each line is students file
                t_line = tf.readline()  # read a line of tutors file
                assert s_line == t_line  # and test that they are equal



## end ##