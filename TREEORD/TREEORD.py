import fileinput

def checktree(preorder, inorder, postorder, length):
    # if the array lengths are 0, then all of them are obviously equal
    if length == 0:
        return 1

    # if array lengths are 1, then check if all of them are equal
    if length == 1:
        return (preorder[0] == inorder[0] == postorder[0])

    # search for first element of preorder in inorder array
    idx = -1

    for i in range(length):
        if inorder[i] == preorder[0]:
            idx = i
            break

    if idx == -1:
        return 0

    # check for the left subtree
    ret1 = checktree(preorder[1:], inorder, postorder, idx)

    # check for the right subtree
    ret2 = checktree(preorder[idx + 1:], inorder[idx + 1:], postorder[idx:], length-idx-1)

    # return 1 only if both of them are correct else 0
    return (ret1 and ret2)

# test data
test_data_1 = ['6',
               '1 2 4 5 3 6',
               '4 5 2 6 3 1',
               '4 2 5 1 3 6']

test_data_2 = ['5',
               '4 2 5 1 3',
               '1 2 4 5 3',
               '4 5 2 3 1']

# if __name__ == "__main__":
    # para = 'stan'
    #
    # if 'stan' in para:
    #     if 'test' in para:
    #         entree_str = test_data_2
    #     else:
    #         # Standard input()
    #         entree_str = [line.strip() for line in fileinput.input()]
    #
    #     len_node = int(entree_str[0].split(' ')[0])
    #     preorder = [int(i) for i in entree_str[1].split(' ')]
    #     postorder = [int(i) for i in entree_str[2].split(' ')]
    #     inorder = [int(i) for i in entree_str[3].split(' ')]
    #     # print(inorder, preorder, postorder)
    #     len1 = len(inorder)
    #     len2 = len(preorder)
    #     len3 = len(postorder)
    #
    # # For test
    # if para == 'test':
    #     len_node = 5
    #     inorder = [4,2,5,1,3]
    #     preorder = [1,2,4,5,3]
    #     postorder = [4,5,2,3,1]
    #     len1 = len(inorder)
    #     len2 = len(preorder)
    #     len3 = len(postorder)

entree_str = [line.strip() for line in fileinput.input()]

len_node = int(entree_str[0].split(' ')[0])
preorder = [int(i) for i in entree_str[1].split(' ')]
postorder = [int(i) for i in entree_str[2].split(' ')]
inorder = [int(i) for i in entree_str[3].split(' ')]
# print(inorder, preorder, postorder)
len1 = len(inorder)
len2 = len(preorder)
len3 = len(postorder)


# print(preorder, inorder, postorder, len_node)
# check if all the array lengths are equal
if len_node == len1 and len1 == len2 and len2 == len3:
    correct = checktree(preorder, inorder, postorder, len_node)
    if correct:
        print('yes')
    else:
        print('no')
else:
    print('no')
