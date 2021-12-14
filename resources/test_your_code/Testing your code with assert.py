#!/usr/bin/env python
# coding: utf-8

# # Testing your code with 'assert' statements
# 
# 
# 

# In[ ]:


test = True


# ## Example 1 - Testing the score_2(dice_1, dice_2) function

# In[ ]:


def score_2(dice_1, dice_2):
    if dice_1 + dice_2==7:
        sum = 14
        return sum
    if dice_1 == dice_2 != 6:
        sum = dice_1*3
        return sum
    if dice_1==6==dice_2:
        sum = (dice_1 == dice_2)*2  # can you spot the problem?
        return sum
    else:
        sum = dice_1 + dice_2
        return sum


# Testing with `assert`
# 
# If all tests pass, nothing happens!
# Which means it's easy to test lots of cases without having to wade through lots of output for no reason.

# In[ ]:


if test:
    assert score_2(1, 5) == 6
    assert score_2(5, 1) == 6
    assert score_2(3, 4) == 14
    assert score_2(5, 2) == 14
    assert score_2(2, 2) == 6
    assert score_2(6, 6) == 24


# If a test does fail, `assert` raises an exception and identifies **exactly** which test failed.
# 

# ## Example 2 - score_4(red_1, red_2, blue_1, blue_2)

# In[ ]:


def score_4(red1, red2, blue1, blue2):
    s =  (red1, red2, blue1, blue2)
    a = sorted (s)
    if red1 + blue2 ==7 and red2+ blue1 !=7:
        return 7
    if red1 + blue1 == 7 and red2 + blue2 != 7:
        return 7
    if red1 + blue1 != 7 and red2+blue2==7:
        return 7
    if red1+blue2!=7 and red2+blue1==7:
        return 7
    while red1+blue1 ==7 and red2 +blue1 ==7:
        if s.count (3) ==2 and s.count(4)==2:
            return 21
        else:
            return 14
    while red1+blue2 ==7 and red2+blue1 ==7:
        if s.count(3) ==2 and s.count (4)==2:
            return 21
        else:
            return 14
    else:
        return a [0]


# In[ ]:


if test:
    assert score_4(1, 5, 6, 6) == 7
    assert score_4(3, 2, 3, 3) == 2
    assert score_4(2, 6, 1, 5) == 14
    assert score_4(1, 1, 2, 6) == 7
    assert score_4(1, 2, 3, 4) == 1
    assert score_4(3, 3, 3, 4) == 7
    assert score_4(3, 3, 4, 4) == 21
    assert score_4(4, 3, 3, 4) == 21


# And problem identified, precisely!
