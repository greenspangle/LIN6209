# To LIN6209 students
# ===================
# This is the test script I use to test which of your assignment 2 functions work corrrectly
# Although you will not be able to execute this Python script on your PC without installing
# the 'pytest' library it should be reasonably straightforward to read and see exactly what is being tested.
# For instance the statement
#       assert magic7() == 7
# means: execute the function magic7() and test that the value returned is 7

# TEST SCRIPT STARTS HERE
# import the student assignment script and all the code within it
from w2_functions.w2_assignment.w2assgnt_answers import *
# import 'types' from Python standard library (used for testing type of values)
import types


def test_magic7():
    assert isinstance(magic7, types.FunctionType)
    assert isinstance(magic7(), int)
    assert magic7() == 7
    assert magic7() == 7


def test_times2():
    assert isinstance(times2, types.FunctionType)
    # int
    assert isinstance(times2(0), int)
    assert times2(0) == 0
    assert times2(2) == 4
    assert times2(1234567890) == (1234567890 * 2)
    assert times2(-0) == 0
    assert times2(-2) == -4
    assert times2(-1234567890) == -(1234567890 * 2)
    # float
    assert isinstance(times2(0.0), float)
    assert times2(0.0) == 0
    assert times2(2.1) == 4.2
    assert times2(12345.67890) == (12345.67890 * 2)
    assert times2(-0.0) == 0
    assert times2(-2.0) == -4.0
    assert times2(-1234567890) == -(1234567890 * 2)
    # strings
    assert isinstance(times2(''), str)
    assert times2('') == ''
    assert times2(' ') == '  '
    assert times2('w') == 'ww'
    assert times2('four') == 'fourfour'
    assert times2('abracadabra') == 'abracadabraabracadabra'


def test_all_ops_pt1():
    assert isinstance(all_ops_pt1, types.FunctionType)
    assert all_ops_pt1(4, 2) == (6, 2, 8, 2.0, 2, 0)
    assert isinstance(all_ops_pt1(4, 2)[3], float)
    assert all_ops_pt1(5, 4) == (9, 1, 20, 1.25, 1, 1)
    assert all_ops_pt1(9, 3) == (12, 6, 27, 3.0, 3, 0)


def test_all_ops_pt2():
    assert isinstance(all_ops_pt2, types.FunctionType)
    assert all_ops_pt2(1, 2)[:-1]  == (True, True, False, True, False, False)[:-1]
    assert all_ops_pt2(2, 1)[:-1]  == (False, False, False, True, True, True)[:-1]
    assert all_ops_pt2(0, 0)[:-1]  == (False, True, True, False, True, False)[:-1]
    assert all_ops_pt2(1, 1)[:-1]  == (False, True, True, False, True, False)[:-1]


def test_magic_number():
    assert isinstance(magic7, types.FunctionType)
    assert magic_number(7)
    assert magic_number(11171171)
    assert magic_number(-7)
    assert magic_number(0.123456789)
    assert not magic_number(0)
    assert not magic_number(0123.456)


def test_hms_to_s():
    assert isinstance(hms_to_s, types.FunctionType)
    assert hms_to_s(0, 0, 0) == 0
    assert hms_to_s(0, 0, 1) == 1
    assert hms_to_s(0, 1, 0) == 60
    assert hms_to_s(1, 0, 0) == 3600
    assert hms_to_s(1, 1, 1) == 3661
    assert hms_to_s(1, 2, 3) == 3723
    assert hms_to_s(100, 100, 100) == 366100


def test_s_to_hms():
    assert isinstance(s_to_hms, types.FunctionType)
    assert s_to_hms(0) == (0, 0, 0)
    assert s_to_hms(1) == (0, 0, 1)
    assert s_to_hms(60) == (0, 1, 0)
    assert s_to_hms(3600) == (1, 0, 0)
    assert s_to_hms(10921) == (3, 2, 1)
    assert s_to_hms(366100) == (101, 41, 40)


def test_add_hms():
    assert isinstance(add_hms, types.FunctionType)
    assert add_hms(0, 0, 0, 0, 0, 0) == (0, 0, 0)
    assert add_hms(1, 1, 1, 0, 0, 0) == (1, 1, 1)
    assert add_hms(0, 0, 0, 1, 1, 1) == (1, 1, 1)
    assert add_hms(1, 1, 1, 1, 1, 1) == (2, 2, 2)
    assert add_hms(0, 0, 50, 0, 0, 40) == (0, 1, 30)
    assert add_hms(25, 50, 50, 145, 40, 20) == (171, 31, 10)


def test_add_old_uk():
    assert isinstance(add_old_uk, types.FunctionType)
    assert add_old_uk(0, 0, 0, 0, 0, 0) == (0, 0, 0)
    assert add_old_uk(0, 0, 1, 0, 0, 0) == (0, 0, 1)
    assert add_old_uk(0, 1, 0, 0, 0, 0) == (0, 1, 0)
    assert add_old_uk(1, 0, 0, 0, 0, 0) == (1, 0, 0)
    assert add_old_uk(100, 0, 0, 200, 0, 0) == (300, 0, 0)
    assert add_old_uk(0, 100, 0, 0, 200, 0) == (15, 0, 0)
    assert add_old_uk(0, 0, 100, 0, 0, 200) == (1, 5, 0)
    assert add_old_uk(0, 0, 11, 0, 0, 7) == (0, 1, 6)
    assert add_old_uk(0, 19, 11, 1, 10, 6) == (2, 10, 5)


def test_lucky_fun():
    assert isinstance(lucky_fun, types.FunctionType)
    a = lucky_fun(7)
    assert isinstance(a, types.FunctionType)
    assert isinstance(a(11711), bool)
    assert a(11711)
    assert not a(11511)
    assert not a(0)
    b = lucky_fun(11)
    assert isinstance(b, types.FunctionType)
    assert isinstance(a(11711), bool)
    assert b(11711)
    assert not b(15151)
    assert b(1.102)
    assert not b(1010)
    assert b(11711)
    assert b(11711)


def test_rearranged():
    assert isinstance(rearranged, types.FunctionType)
    assert isinstance(rearranged('Debit card', 'Bad credit'), bool)
    assert rearranged('Debit card', 'Bad credit')
    assert rearranged('Sugared ambulances', 'Cumberland Sausage')
    assert rearranged('A legal title', 'Tagliatelle')
    assert not rearranged('this phrase', 'that phrase')
    assert rearranged('', '')
    assert rearranged('A', 'a')
    assert rearranged('2', str(2))
    assert rearranged('-', '-')
    assert not rearranged('a', 'b')


def test_is_back_to_front():
    assert isinstance(is_back_to_front('Kayak'), bool)
    assert is_back_to_front('Kayak')
    assert is_back_to_front('Akasaka')
    assert is_back_to_front('never odd or even')
    assert is_back_to_front('NeVER OdD or EveN')
    assert not is_back_to_front('backwards')
