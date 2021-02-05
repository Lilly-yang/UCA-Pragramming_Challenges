# Team members:
# Yidan Cai, yidan.cai@etu.univ-cotedazur.fr
# Li Yang, li.yang-li@etu.univ-cotedazur.fr

# Use bubble sort to sort the end time and get a list of corresponding start times
import fileinput, sys


def bubble_sort(s, f):
    for i in range(len(f)):
        for j in range(0, len(f) - i - 1):
            if f[j] > f[j + 1]:
                f[j], f[j + 1] = f[j + 1], f[j]
                s[j], s[j + 1] = s[j + 1], s[j]
    return s, f


def greedy(s, f, n):
    a = [True for x in range(n)]
    # Initial selection of the first activity
    j = 0
    for i in range(1, n):
        # If the start time of the next event is greater than or equal to the end time of the previous event
        if s[i] >= f[j]:
            a[i] = True
            j = i
        else:
            a[i] = False
    return a


# On récupère les lignes de l'entrée en supprimant les caractères blancs :
entree_str = [line.strip() for line in fileinput.input()]
# On supprime les lignes vides :
entree_str = filter(lambda s : len(s) > 0, entree_str)
# Conversion de l'entrée en entiers :
entree_str = [s.split(' ') for s in entree_str]

n = int(entree_str[0][0])
arr = [[int(s[0]), int(s[1])] for s in entree_str[1:]]

# n = 6
# arr = [[0, 2], [1, 7], [4, 11], [5, 6], [8, 10], [9, 13]]

s = []
f = []
for ar in arr:
    s.append(ar[0])
    f.append(ar[1])

s, f = bubble_sort(s, f)
A = greedy(s, f, n)

res = []
for k in range(len(A)):
    if A[k]:
        res.append('({},{})'.format(s[k], f[k]))
# print(' '.join(res))
print(len(res), file=sys.stdout)