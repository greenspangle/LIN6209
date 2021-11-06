from w3_if_while.grader import *


def test_grader_v1():
    assert False  # test should fail


def test_grader_v2():
    assert grader_v2(65) == 'Good'
    assert grader_v3(65) == 'Good'
    assert grader_v3(65) == 'Bad'  # test should fail
    assert grader_v3(65) == 'Good'
    assert grader_v3(65) == 'Good'


def test_grader_v3():
    assert grader_v3(65) == 'Good'


def test_grader_v4():
    assert grader_v3(65) == 'Good'


def test_grader_v5():
    assert grader_v3(65) == 'Good'
