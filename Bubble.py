# -*- coding: utf-8 -*-
"""
Created on Tue Sep  7 12:28:10 2021

@author: Harold
"""


def Bubblesort(number):
    """
    Parameters
    ----------
    number : list or array of numbers to be sorted

    Returns 
    -------
    sorted list or array of number
    """
    
    n = len(number)
    
    # Need to keep track of if algorithm is finished
    # i.e) more iteration required or no
    done = False
    
    while done == False:
        
        # First change 'done' to allow for already sorted 'number' being passed
        done = True
        for i in range(n - 1):
            if number[i] > number[i + 1]:
                hold = number[i]
                number[i] = number[i+1]
                number[i+1] = hold
                
                # 'number' may require more than 1 iteration to sort
                done = False
    
    # After while loop, number should be correctly sorted            
    return number
