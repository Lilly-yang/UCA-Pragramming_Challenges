#!/usr/bin/python3
# -*- coding: utf8 -*-
import fileinput
import sys

# Lecture des données depuis l'entrée standard
# Documentation pour fileinput.input() :
# This iterates over the lines of all files listed in sys.argv[1:],
# defaulting to sys.stdin if the list is empty.

# On récupère les lignes de l'entrée en supprimant les caractères blancs :
entree_str = [line.strip() for line in fileinput.input()]
# On supprime les lignes vides :
# entree_str = filter(lambda s : len(s) > 0, entree_str)

# Conversion de l'entrée en entiers :
# entree_int = [int(s) for s in entree_str]

# Traitement sur l'entree, ici aucun :
entree_int = []
# for-loop the cases
for i in range(int(entree_str[0])):
    # print('---Counting Case %d/%d---'%(i+1,int(entree_str[0])))
    # num_list = [int(num) for num in entree_str[(i+1)*2].split(' ')]
    # num_str = ''.join(num_list)
    sum_num = 0
    # print(int(entree_ststr[(i+1)*2][-1]))
    # new_entree_str = entree_str.replace(' ','')
    # for-loop each stairs
    # print('Stairs No.%d --- '%(int(entree_str[i*2+1])), entree_str[(i+1)*2])
    for k in range(1, int(entree_str[i*2+1])):
        # for-loop each number that < stairs number
        for j in range(int(entree_str[(i+1)*2].replace(' ', '')[k])):
            # print('Sum numbers <%d and =%d in '%(int(entree_str[(i+1)*2].replace(' ', '')[k]), j), entree_str[(i+1)*2][:k])
            sum_num += j*entree_str[(i+1)*2].replace(' ', '')[:k].count(str(j))
        # print('Sum is: ', sum_num)
    # entree_int.append(sum([int(num) for num in entree_str[(i+1)*2].split(' ')][:-1]))
    # print('Sum is: %d'%sum_num)
    entree_int.append(sum_num)

# Affichage :
# Attention, "print" ajoute par défaut un caractère '\n'
# Pour l'éviter : print(var_ou_str, end='')
for n in entree_int :
    print(n,file=sys.stdout)
