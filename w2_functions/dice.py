"""Simulate a many-sided dice"""

import random  # from the standard library

def dice(sides=6):
    # return a random integer from 1 to sides (default 6) inclusive
    return random.randint(1,sides)
