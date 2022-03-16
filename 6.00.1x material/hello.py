# -*- coding: utf-8 -*-
"""
Created on Fri Mar 11 17:47:00 2022

@author: Othman Faiz
"""

def recursion(a, b):
    if b == 1:
        return a
    else:
        return a + recursion(a, b-1)

print(recursion(5,5))