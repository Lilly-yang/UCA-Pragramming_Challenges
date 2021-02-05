import sys
import numpy as np

# entrees = [1, 2, 0, 1]
# entrees = [0, 1, 2, 0, 3, 1, 4, 2, 3, 4, 0]
# entrees = [0, 1, 0, 3, 0, 1, 4, 2, 1, 3, 4, 0]

entree_str = sys.stdin.readline()
entree_str = entree_str.split()
entrees = [int(s) for s in entree_str]

n = max(entrees)
mat = np.zeros((n+1, n+1))

for i in range(0, len(entrees)-1):
    int_sort = entrees[i: i+2]
    int_sort.sort()
    mat[int_sort[0], int_sort[1]] += 1

slices = ((n+1)**2 - n -1)/2
if np.sum(mat == 1) == slices:
    # print('0 0 0')
    result = [0, 0, 0]
else:
    # print('%d %d %d'%(1, np.sum(mat == 0)-slices-n-1, np.sum(mat>1)))
    result = [1, int(np.sum(mat == 0)-slices-n-1), int(np.sum(mat>1))]

print(*result)
