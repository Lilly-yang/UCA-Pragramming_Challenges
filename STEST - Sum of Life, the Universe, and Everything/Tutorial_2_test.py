#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 17 11:20:59 2019

@author: liyang
"""

entree_int = [1,2,3]

Ind_42 = len(entree_int)
if len(entree_int) > 2:
    for i in range(len(entree_int)-2):
        # print(i)
        if sum(entree_int[i:i+3]) == 42:
            #print(entree_int[i:i+3])
            Ind_42 = i
            break
    
entree_int = entree_int[:Ind_42]

print(entree_int)
