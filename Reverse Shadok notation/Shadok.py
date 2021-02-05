# -*- coding: utf8 -*-
# First-Name: Li, Family-Name: Yang
# E-mail: li.yang-li@etu.univ-cotedazur.fr

import fileinput
import sys


# replace Shadok notation to number or number to Shadok notation
def str_replace(ent, sha=False):
    # from Shadok to number
    if not sha:
        ent = ent.replace('Ga', '0')
        ent = ent.replace('Bu', '1')
        ent = ent.replace('Zo', '2')
        ent = ent.replace('Meu', '3')
    # from umber to Shadok
    else:
        ent = ent.replace('0', 'Ga-')
        ent = ent.replace('1', 'Bu-')
        ent = ent.replace('2', 'Zo-')
        ent = ent.replace('3', 'Meu-')

    return ent


# caculate single Shadok notation
def shadok(ent):
    # replace Shadok to bumber
    ent = str_replace(ent)

    # get number list one-by-one to calculate
    split_shadok = [int(s) for s in ent.split('-')]

    #
    sum = 0
    for i in range(len(split_shadok)):
        # print(4^(len(split_shadok)-i-1))
        sum += split_shadok[i] * (4 ** (len(split_shadok) - i - 1))

    return str(sum)


# caculate single line
def re_reverse(list):
    for i, ele in enumerate(list):
        if ele == '+':
            new_ele = int(list[i - 2]) + int(list[i - 1])
            break
        elif ele == '-':
            new_ele = int(list[i - 2]) - int(list[i - 1])
            break
        elif ele == '*':
            new_ele = int(list[i - 2]) * int(list[i - 1])
            break
        elif ele == '/':
            new_ele = int(list[i - 2]) / int(list[i - 1])
            break

    new_list = list[:i - 2] + [new_ele] + list[i + 1:]

    return new_list, list


# Hexadecimal conversion
def sijinzhi(x):
    list = []
    while x > 3:
        list.append(str(x % 4))
        x = x // 4
    if x:
        list.append(str(x))
    x = ''.join(reversed(list))

    return x


# transform int number to standard Shadok notation
def be_shadok(x):
    shax = str_replace(str(x), sha=True)
    if shax[-1] == '-':
        shax = shax[:-1]

    return shax


# Main function
def reverse_shadok_notation(entree_str):
    for i, element in enumerate(entree_str):
        if len(element) == 1:
            continue
        else:
            entree_str[i] = shadok(entree_str[i])

    new = entree_str
    while len(new) > 1:
        new, entree_str = re_reverse(new)

    shadok_int = sijinzhi(int(new[0]))

    shadok_speaker = be_shadok(shadok_int)

    return shadok_speaker


# Test case
entree_str = ['3',
              '5 2 * 3 4 + - .',
              'Bu-Bu Zo * Meu Bu-Ga + - .',
              'Bu-Bu-Ga 5 Meu 1 * - * .']


if __name__ == '__main__':
    # On récupère les lignes de l'entrée en supprimant les caractères blancs :
    entree_str = [line.strip() for line in fileinput.input()]

    # On supprime les lignes vides :
    entree_str = filter(lambda s: len(s) > 0, entree_str)

    # Store input as a list
    entree_str = [s.split() for s in entree_str]

    # calculate line-by-line
    case = int(entree_str[0][0])
    all_results = []
    for i in range(case):
        result = reverse_shadok_notation(entree_str[i + 1][:-1])
        all_results.append(result)

    # Affichage :
    # Attention, "print" ajoute par défaut un caractère '\n'
    # Pour l'éviter : print(var_ou_str, end='')
    for n in all_results:
        print(n, file=sys.stdout)
