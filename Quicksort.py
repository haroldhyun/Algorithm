# -*- coding: utf-8 -*-
"""
Created on Tue Sep  7 14:20:59 2021

@author: Harold
"""


def Quicksort(number):
    """
    Parameters
    ----------
    number : list or array of numbers to be sorted

    Returns 
    -------
    sorted list or array of number
    """
    
    
    # Create three empty lists to store what's left/right of the pivot
    left = []
    same = []
    right = []
    
    
    # If n = 1 then we just return that number.
    
    if len(number) <= 1:
        return number
    else:
        
        # As per convention, pivot will be the last element
        pivot = number[-1]
        
        for x in number[:-1]:
            # This is pretty self-explanatory. Big goes right, small goes left.
            if x > pivot:
                right.append(x)
            elif x == pivot:
                same.append(x)
            else:
                left.append(x)
    
    # Now we have to do recursive step
    l = Quicksort(left)
    r = Quicksort(right)
    
    # We have to include our pivot back into the list of sorted number.
    sort = l + same + [pivot] + r
    
    # Then we have sorted numbers.
    return sort