"""
Created on Wed Sep 04 , 2019

@author: Abhirup Banerjee
contact : abhirup.banerjee@pik-potsdam.de
"""
import numpy as np

def moving_average(x, w):
    return np.convolve(x, np.ones(w), 'valid') / w

x = np.array([5,3,8,10,2,1,5,1,0,2])


