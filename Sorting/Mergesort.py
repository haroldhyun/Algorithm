# -*- coding: utf-8 -*-
"""
Created on Tue Sep  7 20:04:26 2021

@author: Harold
"""


def Mergesort(number):
    
    """
    Parameters
    ----------
    number : list or array of numbers to be sorted

    Returns 
    -------
    sorted list or array of number
    """
    
    # First divide the list by two halves
    
    n = len(number)
    
    # If there is only 1 element, we don't need to sort.
    if n == 1:
        return number
    
    # Mergesort is a divide and conquer method. Divide into two halves
    half = n // 2
    
    first = number[:half]
    last = number[half:]
    
    # Now we can recursively sort the two halves
    sort_first = Mergesort(first)
    sort_last = Mergesort(last)
    
    # Then we can merge the two
    sort = merge(sort_first, sort_last)
    
    return sort


def merge(one, two):
    """
    Parameters
    ----------
    one : list or array
        numbers to be sorted
    two : list or array
        numbers to be sorted

    Returns
    -------
    sorting: sorted and merged array of one and two
    """
    
    # First create new empty array.
    sorting = []
    
    # Let's loop and compare until one or two runs out of element
    while len(one) != 0 and len(two) != 0:
        
        if one[0] < two[0]:
            sorting.append(one[0])
            one.pop(0)
        else:
            sorting.append(two[0])
            two.pop(0)
            
    # When the first while loop is complete, either one or two has no more elements
    # Then we just have to add whatever is remaining to sorting
    if len(one) != 0:
        sorting = sorting + one
    
    elif len(two) != 0:
        sorting = sorting + two
    
    # Now we just return our sorted array
    return sorting
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    