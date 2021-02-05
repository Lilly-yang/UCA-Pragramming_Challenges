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
for ind, page_range in enumerate(entree_str):
    if page_range == '0':
        break
    rag = [int(i) for i in page_range.split(' ')]
    all_pages_str = ''.join([str(i) for i in range(min(rag),max(rag)+1)])
    count_list = []
    for j in range(10):
        # append_str = str(j)+':'+str(all_pages_str.count(str(j)))
        count_list.append(str(j)+':'+str(all_pages_str.count(str(j))))
    # print(' '.join(count_list))
    # entree_int['Case '+str(ind+1)] = ' '.join(count_list)
    entree_int.append('Case '+str(ind+1)+': '+' '.join(count_list))

# Affichage :
# Attention, "print" ajoute par défaut un caractère '\n'
# Pour l'éviter : print(var_ou_str, end='')
for n in entree_int:
    print(n, file=sys.stdout)
