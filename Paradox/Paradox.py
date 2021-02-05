# -*- coding: utf8 -*-
import fileinput, sys
import numpy as np


def reduce_bank_own(entree_str, bank_num):
    relationship = 'NOT PARADOX'
    own_matrix = np.zeros((bank_num, 2))
    own_matrix[0,0] = 1
    for i, line in enumerate(entree_str[1:]):
        line = line.split()
        sum_i = np.sum(own_matrix[i])
        if sum_i == 2:
            relationship = 'PARADOX'
            break

        if sum_i == 0:
            if int(line[0])-1 == i and line[1] == 'false':
                relationship = 'PARADOX'
                break

            own_matrix[i, 0] = 1
            if np.sum(own_matrix[int(line[0])-1]) == 0:
                add_n = 1
            else:
                add_n = -1
            if line[1] == 'true':
                own_matrix[int(line[0])-1, 0] = add_n
            else:
                own_matrix[int(line[0])-1, 1] = add_n
        else:
            if own_matrix[i,1] == 1:
                if line[1] == 'true':
                    own_matrix[int(line[0])-1, 1] = 1
                else:
                    own_matrix[int(line[0])-1, 0] = 1
            else:
                if line[1] == 'true':
                    own_matrix[int(line[0])-1, 0] = 1
                else:
                    own_matrix[int(line[0])-1, 1] = 1

        if abs(np.sum(own_matrix[int(line[0])-1])) == 2:
            relationship = 'PARADOX'
            break

    return relationship


entree_str = ['2',
              '2 false',
              '1 true',
              '2',
              '2 false',
              '1 false',
              '3',
              '2 false',
              '2 true',
              '3 true',
              '3',
              '2 false',
              '2 false',
              '3 true',
              '4',
              '2 false',
              '3 false',
              '1 true',
              '2 true',
              '5',
              '1 true',
              '3 true',
              '4 false',
              '5 true',
              '2 true',
              '3',
              '1 true',
              '2 false',
              '3 true',
              '1',
              '1 true',
              '1',
              '1 false',
              '0']

if __name__ == '__main__':
    # On récupère les lignes de l'entrée en supprimant les caractères blancs :
    entree_str = [line.strip() for line in fileinput.input()]
    # On supprime les lignes vides :
    entree_str = filter(lambda s: len(s) > 0, entree_str)
    entree_str = [s for s in entree_str]

    # print(entree_str)

    case = 0
    count = 0
    all_results = []
    while entree_str[case] != '0':
        count += 1
        bank_num = int(entree_str[case])
        tep_case = entree_str[case:case + bank_num + 1]
        result = reduce_bank_own(tep_case, bank_num)
        all_results.append(result)
        case += bank_num + 1

    # Affichage :
    # Attention, "print" ajoute par défaut un caractère '\n'
    # Pour l'éviter : print(var_ou_str, end='')
    for n in all_results:
        print(n, file=sys.stdout)
