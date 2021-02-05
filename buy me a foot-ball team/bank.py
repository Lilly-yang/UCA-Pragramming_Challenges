# -*- coding: utf8 -*-
import fileinput, sys
import numpy as np


def reduce_bank_own(entree_str, bank_num):
    own_matrix = np.zeros((bank_num, bank_num))
    for i, line in enumerate(entree_str[1:]):
        split_line = line.split()
        for j in range(bank_num):
            own_matrix[i, j] = int(split_line[j])

    # Traitement sur l'entree, ici aucun :
    bank_sum = np.sum(own_matrix)

    IO = np.zeros((bank_num, 3))
    for i in range(2):
        IO[:, i] = np.sum(own_matrix, axis=i)

    IO[:, 2] = IO[:, 0] - IO[:, 1]

    result = np.sum(IO[:, 2][IO[:, 2] > 0])

    return int(bank_sum), int(result)


entree_str = ['4',
              '0  50 100   0',
              '150   0  20   0',
              '0   0   0  30',
              '30   0   0   0',
              '3',
              '0  10  20',
              '10   0   0',
              '0  20   0',
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
        bank_sum, result = reduce_bank_own(tep_case, bank_num)
        all_results.append([str(count) + '.', bank_sum, result])
        case += bank_num + 1

    # Affichage :
    # Attention, "print" ajoute par défaut un caractère '\n'
    # Pour l'éviter : print(var_ou_str, end='')
    for n in all_results:
        print(' '.join(str(s) for s in n), file=sys.stdout)
