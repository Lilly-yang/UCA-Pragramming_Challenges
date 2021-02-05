# -*- coding: utf8 -*-
# First-Name: Li, Family-Name: Yang
# E-mail: li.yang-li@etu.univ-cotedazur.fr


import fileinput
import sys
import numpy as np


# Main function
def fishnet(para, school):
    # transform Shadok notation to number in a line
    para = [int(s) for s in para.split()]
    school = [int(s) for s in school.split()]

    size = para[1] * 2 + 1

    # Set the number less than the maximum capture weight to 0
    school = np.array(school, np.int)
    school[school < para[2]] = 0

    # End of array plus zero value for radius length
    new_school = np.zeros(len(school) + 2 * para[1], np.int)
    new_school[para[1]:para[1] + len(school)] = school

    # get the position of the maximum sub-array
    maxSub = [np.sum(new_school[i:i + size]) for i in range(0, len(new_school) - size + 1)]
    posation = maxSub.index(max(maxSub)) + 1

    return posation


# Test case
entree_str = ['4',
              '7 1 5',
              '7 2 5 8 1 1 9',
              '1 1 1',
              '1',
              '4 2 2',
              '5 4 3 1',
              '7 3 2',
              '7 6 5 4 3 2 1',
              '']


if __name__ == '__main__':
    ### On récupère les lignes de l'entrée en supprimant les caractères blancs:
    entree_str = [line.strip() for line in fileinput.input()]
    entree_str = filter(lambda s: len(s) > 0, entree_str)
    entree_str = [s for s in entree_str]

    # calculate each case
    # case = int(entree_str[0])
    # all_results = []
    # for i in range(case):
    #     result = fishnet(entree_str[i * 2 + 1], entree_str[i * 2 + 2])
    #     all_results.append(result)


    # Affichage:
    for n in [fishnet(entree_str[i * 2 + 1], entree_str[i * 2 + 2]) for i in range(int(entree_str[0]))]:
    # for n in all_results:
        print(n, file=sys.stdout)
