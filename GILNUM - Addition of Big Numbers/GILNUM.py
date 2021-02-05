#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 18 10:06:05 2019

@author: liyang
"""

import fileinput
import sys

# Lecture des données depuis l'entrée standard
# Documentation pour fileinput.input() :
# This iterates over the lines of all files listed in sys.argv[1:],
# defaulting to sys.stdin if the list is empty.

#for n in fileinput.input():
#    print(n, file=sys.stdout)

# On récupère les lignes de l'entrée en supprimant les caractères blancs :
# 通过删除空白字符来恢复输入行
entree_str = [line.strip() for line in fileinput.input()]
# On supprime les lignes vides :
# 删除空行
# entree_str = filter(lambda s : len(s) > 0, entree_str)
entree_str = [int(s) if str.isdigit(s) else None for s in entree_str]
#print('Length of str is: ', len(entree_str))
# Conversion de l'entrée en entiers :
# 将输入转换为整数
#entree_int = [int(s) for s in entree_str if str.isdigit(s)]
#entree_sum = [sum([entree_str[2*i], entree_str[2*i+1]]) if sum([entree_str[2*i], entree_str[2*i+1]]) else '?' for i in range(int(len(entree_str)/2))]
entree_sum = []
for i in range(int(len(entree_str)/2)):
#    print(i)
#    print(2*i, 2*i+1)
    try:
#        sum([entree_str[2*i], entree_str[2*i+1]])
#        sum_str = sum([entree_str[2*i], entree_str[2*i+1]])
#        print(sum_str)
        entree_sum.append(sum([entree_str[2*i], entree_str[2*i+1]]))
    except:
#        print('?')
        entree_sum.append('?')

# Traitement sur l'entree, ici aucun :
# 输入处理（为空）：

# Affichage :
# Attention, "print" ajoute par défaut un caractère '\n'
# Pour l'éviter : print(var_ou_str, end='')

for n in entree_sum :
    print(n,file=sys.stdout)
