"""Convert marks to grades according to this table

Mark   Grade
>=80    Merit
>=60    Good
>=40    Pass
<40     Fail
"""

def grader_v1(mark):  # faulty logic
    grade = 'not decided'
    if mark >= 80:
        grade = 'Merit'
    if mark >= 60:
        grade = 'Good'
    if mark >= 40:
        grade = 'Pass'
    if mark < 40:
        grade = 'Fail'
    return grade


def grader_v2(mark):
    """ now works but what if there were 10 grades? or 20? or 30??"""
    grade = 'not decided'
    if mark >= 80:
        grade = 'Merit'
    else:
        if mark >= 60:
            grade = 'Good'
        else:
            if mark >= 40:
                grade = 'Pass'
            else:
                if mark < 40:
                    grade = 'Fail'
    return grade


def grader_v3(mark):  # simpler to write & read
    if mark >= 80:
        grade = 'Merit'
    elif mark >= 60:
        grade = 'Good'
    elif mark >= 40:
        grade = 'Pass'
    elif mark < 40:
        grade = 'Fail'
    else:
        grade = 'not decided'  # catch all other conditions
    return grade

