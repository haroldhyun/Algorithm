# -*- coding: utf-8 -*-
"""
Created on Wed Sep  8 17:45:52 2021

@author: Harold
"""
import numpy as np

def km_assignment_step(data, Mu):
    """ Compute K-Means assignment step
    
    Args:
        data: a NxD matrix for the data points
        Mu: a DxK matrix for the cluster means locations
    
    Returns:
        R_new: a NxK matrix of responsibilities
    """
    
    N, D = data.shape # Number of datapoints and dimension of datapoint
    K = Mu.shape[1] # number of clusters
    r = np.zeros((N, K))
    
    for k in range(K):
        # r[:, k] = ...
        r[:, k] = np.linalg.norm(data - np.array([Mu[:, k], ] * N), axis=1)**2
        
    # arg_min = ... # argmax/argmin along dimension 1
    # axis = 1 -> by rows
    arg_min = np.argmin(r, axis = 1)
    
    
    # R_new = ... # Set to zeros/ones with shape (N, K)
    # R_new[..., ...] = 1 # Assign to 1
    
    R_new = np.zeros((N,K))
    R_new[np.array(range(N)), arg_min] = 1
    
    return R_new



def km_refitting_step(data, R, Mu):
    """ Compute K-Means refitting step.
    
    Args:
        data: a NxD matrix for the data points
        R: a NxK matrix of responsibilities
        Mu: a DxK matrix for the cluster means locations
    
    Returns:
        Mu_new: a DxK matrix for the new cluster means locations
    """
    N, D = data.shape # Number of datapoints and dimension of datapoint
    K = Mu.shape[1]  # number of clusters
    
    # axis = 0 will fix the column
    Mu_new = np.dot(data.T, R)/np.sum(R, axis = 0)
    return Mu_new