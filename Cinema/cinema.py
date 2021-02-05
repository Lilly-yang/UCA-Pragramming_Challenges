# -*- coding: utf8 -*-
import fileinput, sys
import numpy as np


def count_row_colum(cinema, row = True, colum = True):
    if row:
        cin_sum = np.sum(cinema[:-1, :-1], axis=0)
        cinema[-1, :-1] = cin_sum

    if colum:
        mov_len = np.sum(cinema[:-1, :-1], axis=1)
        cinema[:-1, -1] = mov_len

    # print(cin_sum, '/', mov_len)
    # print(cinema.shape, '/', cinema)

    return cinema


# On récupère les lignes de l'entrée en supprimant les caractères blancs :
entree_str = [line.strip() for line in fileinput.input()]
# On supprime les lignes vides :
entree_str = filter(lambda s : len(s) > 0, entree_str)

# Conversion de l'entrée en entiers :
entree_str = [s.split(' ') for s in entree_str]
# print(entree_str)
mov_num = int(entree_str[0][0])
entree_int = [[int(s[0]), int(s[1])] for s in entree_str[1:]]
# print(entree_int)
# entree_long = [s[1]-s[0] for s in entree_int]
# print(entree_long)

# mov_num = 6
# entree_int = [[0, 2], [1, 7], [4, 11], [5, 6], [8, 10], [9, 13]]

# Traitement sur l'entree, ici aucun :
mov_end = [s[1] for s in entree_int]
cinema = np.zeros((mov_num+1, max(mov_end)+1))
for ind, movie in enumerate(entree_int):
    cinema[ind, movie[0]:movie[1]] = 1
# print(cinema)

count_row_colum(cinema)

while np.max(cinema[-1]) > 1:
    max_ind = np.argmax(cinema[-1])
    # print(max_ind)
    # print(cinema[:, int(max_ind)])
    cin_inx = np.where(cinema[:, int(max_ind)] == 1)
    # print(cin_inx)
    cin_len = [cinema[:,-1][s] for s in cin_inx]
    short_mov_ind = np.argmin(cin_len[0])
    short_mov = cin_inx[0][np.argmin(cin_len[0])]
    for ind in cin_inx[0]:
        if ind != short_mov:
            cinema[ind, :] = 0
            # print(cinema[ind, :])

    count_row_colum(cinema, colum = False)

    # print(cinema)

num_max = np.count_nonzero(cinema[:,-1])
print(num_max, file=sys.stdout)

