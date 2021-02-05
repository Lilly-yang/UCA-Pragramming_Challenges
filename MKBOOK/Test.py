import sys

# Input List of String
entree_str = ['10 15',
              '15 10',
              '912 912',
              '900 999',
              '0 0',
              '0 1',
              '1 0',
              '0']

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

# Print Results
for n in entree_int:
    # print(entree_int.keys(n), entree_int.values(n))
    print(n)
