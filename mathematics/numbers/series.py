# mathematics/numbers/series.py

import math  # Import math module for the built-in sum function

def sum(list=None, **kwargs):  # Use 'list' as the parameter name
    if list is not None:
        return math.fsum(list)  # Use math.fsum to calculate the sum
    return 0  # Return 0 if no list is provided

def average(list=None, **kwargs):  # Use 'list' as the parameter name
    if list is not None:
        return math.fsum(list) / len(list)  # Use math.fsum to calculate the sum
    return 0  # Return 0 if no list is provided

