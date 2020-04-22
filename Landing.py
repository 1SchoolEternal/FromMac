
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






# row_num = 4
# c = "xx..xx.T...C"
# digit_num = 12
# # duh_list = [[i, row] for i in range(digit_num) if c[i] == '.']

# duh_list = [[i, row] for i in range(digit_num) if c[i] == '.'] for row in range(row_num)]

# print(duh_list)

# last_price = 0
# high_price = 0
# price_drop = 0
# n = int(input())
# for i in input().split():
#     v = int(i)
#     if v >= last_price:
#         if v > high_price:
#             high_price = v
#     else:
#         price_drop = (v - high_price) if ((v - high_price)
#                                           < price_drop) else price_drop
#     last_price = v

# x = math.ceil(2, 15)
# print(x)
# [[300, 30], [1500, 20], [3000, 10]]
# [[1000, 15], [3000, 10], [4000, 30], [5000, 30], [6000, 5], [7000, 10]]

# [1234, 5],  [2468, 5],  [3702, 5],  [6170, 5],  [8638, 5],
# [13574, 5], [16042, 5], [20978, 5], [23446, 5], [28382, 5],
# [35786, 5], [38254, 5], [45658, 5], [50594, 5], [53062, 5],
# [57998, 5]
# speed = int(input())
# light_count = int(input())
# speed = 90
# light_count = 3
# speed = 89
# light_count = 16

# dd = [[int(j) for j in input().split()] for i in range(light_count)]
# cntr = 0
# r = float(speed/3.6)
# # print(dd)
# while cntr < light_count:
#     dd_count = dd[cntr]
#     distance = dd_count[0]
#     duration = dd_count[1]
#     t = distance/r
#     if t % duration == 0:
#         lcs = 0 if t/duration < 1 else t/duration
#     else:
#         lcs = math.floor(t/duration)
#     # lcs = math.ceil(t/duration)
#     # if lcs % 2 != 0:
#     if lcs % 2 == 0:
#         cntr += 1
#     else:
#         r = distance / ((lcs + 1) * duration)
#         cntr = 0
#         speed_now = r * 3.6
# speed = int(r * 3.6)
# print(speed)

# you have distance and duration
# you still have the same speed
# you need to look at the distance
# minus the previous distance
# to determine NEVER MIND


# x = '3'
# y = '5'

# x = int(x) * 1.25

# print(x)


# I don't use either of the above

# t = [2, -8, 7, -6, 5, -4, 3, 9]
# running = True
#     for e, temp in enumerate(t):
#         temp = t[e] for temp

# list = ['R', 'U']
# if 'R' in list:
#     print(True)
# x = int(4)
# y = int(2)
# z = 5/2
# print(int(1/2))

# x = [2, -8, 7, -6, 5, -4, 3, 9]
# for s in range(8):
#     T = [int(s) for s in input().split()]
#     print(T)
#     print(T and sorted(sorted(T, reverse=True), key=abs)[0] or 0)

# FIRST GAME CODE
# h = [2, 8, 7, 6, 5, 4, 3, 9]
# for x in range(8):
#     # z = [(h[x], x) for x in range(8)]
#     # z = max([(h[x], x) for x in range(8)])
#     # z = max([(h[x], x) for x in range(8)])[1]
#     print(max([(h[x], x) for x in range(8)])[1])
#     h[h.index(max(h))] = 0
# pattern = re.(r"\d*")
# li = []
# for i in range(2):
# n1, n2 = [int(j) for j in input().split()]
# link = [[n1, n2] for i in range(2)]
# print(link)
# li.append([int(j) for j in input().split()])
# link = [[int(j) for j in input().split()] for i in range(2)]
# print(link)

# light_count = 2
# dd = [[int(j) for j in input().split()] for i in range(light_count)]
# #     yy = [[n1, n2] for [int(j) for j in input().split()]]
# print(dd)
# print(n1)
# print(n2)

# dict = {'car': {'Volvo', 'kia'}, 'horse':{'paint', 'stalion'}}
# # dict = {'car': 'Volvo', 'horse':'paint'}
# # x = dict.items()
# y = dict[0] & 'kia'
# print(x)
# print(y)


# n, l, e = [int(i) for i in input().split()]

# an adjacency list that, for each node, has a list of neighbors
# represented as a dictionary of sets
# this syntax is called "list comprehension"
# n = 3
# l = 2
# e = 1

# adjList = {x: set() for x in range(n)}

# for i in range(l):
#     n1, n2 = [int(j) for j in input().split()]
#     adjList[n1].add(n2)
#     # both nieghbors must know each other :)
#     adjList[n2].add(n1)

# # a list of gateway nodes
# # respresented as a set, a list could also be used but we don't need to store any order
# gateList = set()
# for i in range(e):
#     ei = int(input())
#     gateList.add(ei)
# print("adjList:", adjList, file=sys.stderr)     # debug

# r = 4
# x = 1
# sampl = [1, 2, 3, 4, 5, 6, 7, 8]

# for i in range(r):
#     x += 1
#     if x == 3:
#         i -= 1
#     print(x)
#     print(i)


# game loop
# while True:
#     si = int(input())                        # skynet si position
#     # si's neighbor nodes that are also gateways

#     exits = adjList[si] & gateList
#     if (exits):                                 # if there are such nodes:
#         # unlink one of them, no testcase will include 2
#         print(si, list(exits)[0])
#     else:                                       # else:
#         print(si, list(adjList[si])[0])   # unlink any node next to the si

# IT SEEMS THAT THE LINK THAT IS CUT FIRST
# DOES NOT CONNECT WITH A GATEWAY
# ACTUALLY THAT IS WHAT IT SAYS IN THE COMMENTS
# WHEN I WROTE THE PROGRAM I ONLY GOT RID OF
# LINKS TO GATEWAYS AND TRACKED WHICH ONES HAD
# BEEN CUT - THIS PROGRAM IS SIMPLER THAN MINE
# I WOULD ARGUE ALSO LESS EFFECTIVE
# I AM NOT FAMILIAR WITH LINE 79
# adjList[si] & gateList
# I guess it returns the key for a key value pair, or nothing
# I DON'T WANT TO LOOK AT THIS SHIT ANY MORE TODAY


# gateway = [int(input()) for i in range(2)]
# print(gateway)

# x = 4
# y = 3
# lll = [x, y]
# zzz = []
# zzz.append(lll)
# x = 5
# y = 8
# lll = [x, y]
# zzz.append(lll)
# print(zzz)

# n = 2
# link = [[1, 2], [1, 4], [2, 4], [5, 2], [2, 5], [3, 8]]
# gateway = [2, 6]
# si = 3
# cut = False
# for i in range(n):
#     if not cut:
#         if [gateway[i], si] in link:
#             edge = link.pop([gateway[i], si])
#             print(str(edge[0]), str(edge[1]))
#             cut = True
#         elif [si, gateway[i]] in link:
#             edge = link.pop(link.index([si, gateway[i]]))
#             print(str(edge[0]), str(edge[1]))
#             cut = True
# if not cut:
#     while not cut:
#         for e, y in enumerate(link):
#             if not cut:
#                 if si in y:
#                     edge = link.pop(e)
#                     print(str(edge[0]), str(edge[1]))
#                     cut = True
# cut = False

# zz = link.index([gateway[0], si])
# cut = link.pop(zz)
# print(str(cut[0]), str(cut[1]))
# print(link)
# elif link.index([si, gateway[0]]):
#     zz = link.index([si, gateway[0]])
#     cut = link.pop(zz)
#     print(str(cut[0]), str(cut[1]))
#     print(link)
# else:
#     print("negative")


# light_x, light_y, initial_tx, initial_ty = [int(i) for i in input().split()]

# light_x = 5
# initial_tx = 0
# light_y = 10
# initial_ty = 7

# while running:

#     EastWest = "" if light_y == initial_ty else max(
#         [[light_y, 'E'], [initial_ty, 'W']])[1]
#     NorthSouth = '' if light_x == initial_tx else max(
#         [[light_x, 'S'], [initial_tx, 'N']])[1]
#     move = NorthSouth + EastWest
#     print(move)
#     if move == 'N':
#         initial_ty -= 1
#     elif move == 'S':
#         initial_ty += 1
#     elif move == 'E':
#         initial_tx += 1
#     elif move == 'W':
#         initial_tx -= 1
#     elif move == 'NE':
#         initial_ty -= 1
#         initial_tx += 1
#     elif move == 'NW':
#         initial_ty -= 1
#         initial_tx -= 1
#     elif move == 'SE':
#         initial_ty += 1
#         initial_tx += 1
#     elif move == 'SW':
#         initial_ty += 1
#         initial_tx -= 1
#     else:
#         print("error")

#     # OLD SOLUTION
#     difx = initial_tx - light_x
#     dify = initial_ty - light_y
#     count_difx = abs(difx)
#     count_dify = abs(dify)
#     if count_difx >= count_dify:
#         i = 0
#         while i < count_difx:
#             if difx < 0:
#                 x = "E"
#             elif difx > 0:
#                 x = "W"
#             if dify > 0:
#                 y = "N"
#                 dify -= 1
#             elif dify < 0:
#                 y = "S"
#                 dify += 1
#             else:
#                 y = ""
#             move = y+x
#             print(move)
#             if move == 'N':
#                 initial_ty -= 1
#             elif move == 'S':
#                 initial_ty += 1
#             elif move == 'E':
#                 initial_tx += 1
#             elif move == 'W':
#                 initial_tx -= 1
#             elif move == 'NE':
#                 initial_ty -= 1
#                 initial_tx += 1
#             elif move == 'NW':
#                 initial_ty -= 1
#                 initial_tx -= 1
#             elif move == 'SE':
#                 initial_ty += 1
#                 initial_tx += 1
#             elif move == 'SW':
#                 initial_ty += 1
#                 initial_tx -= 1
#             else:
#                 print("error")
#             i += 1

#     elif count_dify > count_difx:
#         i = 0
#         while i < count_dify:
#             if dify < 0:
#                 y = "S"
#             elif dify > 0:
#                 y = "N"
#             if difx > 0:
#                 x = "E"
#                 dify -= 1
#             elif difx < 0:
#                 x = "W"
#                 difx += 1
#             else:
#                 x = ""
#             move = y+x
#             print(move)
#             if move == 'N':
#                 initial_ty -= 1
#             elif move == 'S':
#                 initial_ty += 1
#             elif move == 'E':
#                 initial_tx += 1
#             elif move == 'W':
#                 initial_tx -= 1
#             elif move == 'NE':
#                 initial_ty -= 1
#                 initial_tx += 1
#             elif move == 'NW':
#                 initial_ty -= 1
#                 initial_tx -= 1
#             elif move == 'SE':
#                 initial_ty += 1
#                 initial_tx += 1
#             elif move == 'SW':
#                 initial_ty += 1
#                 initial_tx -= 1
#             else:
#                 print("error")
#             i += 1
# # END OLD SOLUTION

# running = False if light_x == initial_tx and light_y == initial_ty else True
