from queue import PriorityQueue

import soupsieve.css_parser


class Node:
    def __init__(self, s = " "):
        self.vertex = s
        self.children = 0
        self.child = []
        self.l1 = 0
        self.l2 = 0
        self.parent = None
        self.path = []



A = Node("A")
B = Node("B")
C = Node("C")
D = Node("D")
E = Node("E")
F = Node("F")
G = Node("G")
H = Node("H")
I = Node("I")

A.children = 3
A.child = [ (B,5), (I, 100), (C,-1)]
B.children = 2
B.child = [ (D, 3), (E, 2)]
C.children = 2
C.child = [(F, 4), (G, 2)]
F.children = 1
F.child = [(H, -10)]


def DFS(V):

    if V.children > 0:
        for i in range(V.children-1, -1, -1):
            V.child[i][0].parent = V
            DFS(V.child[i][0])

    if V.parent != None:
        U = V.parent
        l = V.l1 + U.child[U.children-1][1]
        tmp = U.l1
        U.l1 = max(U.l1, U.l2, l)
        if U.l1 == l:
            U.l2 = max(U.l2, tmp)
        else:
            U.l2 = max(U.l2, l)
        U.children -= 1


def find_heaviest(T, max_path):
    if T.l1 + T.l2 > max_path:
        max_path = T.l1 + T.l2
    for el in T.child:
        find_heaviest(el[0], max_path)

    return max_path

def heav_path(T):
    DFS(T)
    max_path = -float("inf")
    return find_heaviest(T, max_path)

print(heav_path(A))



