entree_str = ['2',
              '5',
              '1 5 3 6 4',
              '8',
              '1 5 3 6 4 8 4 0']

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

# Pour l'éviter : print(var_ou_str, end='')
for n in entree_int:
    print(n)
