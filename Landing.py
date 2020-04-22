
import sys
import math
# THE FOLLOWING IS MY LABARYTH CODE

bfs = 0


def up_down(character_set, kr, kc):
    dv = 'U' if r/2 >= kr else 'D'
    if dv == 'U':
        node_row = character_set[0]
        if '?' in node_row[kc]:
            node_row = character_set[kr - 1]
            if node_row[kc] == '.':
                print('U')
            else:
                find_question()
    elif dv == 'D':
        node_row = character_set[r]
        if '?' in node_row[kc]:
            node_row = character_set[kr + 1]
            if node_row[kc] == '.':
                print('D')
            else:
                find_question()


def find_question(character_set):
    for x in characer_set:
        if '?' in x:


# game loop
while True:
    # kr: row where Kirk is located.
    # kc: column where Kirk is located.
    kr, kc = [int(i) for i in input().split()]
    # for i in range(r):
        # row = input()  # C of the characters in '#.TC?' (i.e. one line of the ASCII maze).

    # make a list of characters, x, and y locations
    character_list = [[row[i], i, x] for i in range(c)] for x in range(r)]

    # check for C
    for y in character_list:
        row_list = character_list[y]
        for z in row_list:
            if 'C' in z:
                bfs = 1

    # if C has not been found continue to change ? to visible characters
    # which side of the grid is closer left or right
    dh = 'L' if c/2 >= Kc else 'R'
    node_row = character_list[kr]
    if dh == 'L':
        if '?' in node_row[0]:  # do you need to see characters on the short side
            if node_row[kc - 1] == '.':  # can you move in that direction
                print('L')
            else:
                # MOVE UP OR DOWN dv = 'U' if c/2 >= kr else 'D'
                up_down(character_set, kr, kc)
    elif dh == 'R'
        if '?' in node_row[c]:
            if node_row[kc + 1] == '.':
                print('R')
            else:
                up_down(character_set, kr, kc)
