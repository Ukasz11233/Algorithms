from queue import PriorityQueue

class Node:
    def __init__(self, val):
        self.val = val
        self.parent = self
        self.rank = 0


def Find(x):
    if x != x.parent:
        x.parent = Find(x.parent)
    return x.parent


def Union(x, y):
    x = Find(x)
    y = Find(y)
    if x == y:
        return

    if x.rank > y.rank:
        y.parent = x

    else:
        x.parent = y
        if x.rank == y.rank:
            y.rank += 1



E = [[(1, 1), (2, 7)], [(0, 1), (2, 8), (4, 4), (5, 12)], [(0, 7), (1, 8), (3, 2), (5, 3)], [(2, 2), (4, 5)], [(1, 4), (3, 5), (5, 6)], [(1, 12), (2, 3), (4, 6)]]

E2 = [(0, 2, 7), (0, 1, 1), (1, 2, 8), (2, 3, 2), (3, 4, 5), (1, 4, 4), (2, 5, 3), (1, 5, 12), (5, 4, 6)]

E3 = [(0,2,2), (1,2,1), (1,4,3), (1,3,2), (2,4,5), (3,4,1), (3,5,3) ]


def Kruskal(E):
    n = len(E)
    E = sorted(E, key=lambda x: x[2])

    A = []
    for i in range(n):
        A.append(Node(i))

    result = [E[0]]
    Union(A[E[0][0]], A[E[0][1]])

    for el in E:
        u = el[0]
        v = el[1]
        if Find(A[u]) != Find(A[v]):
            Union(A[u], A[v])
            result.append(el)

    return result

print(Kruskal(E3))

G = [[-1, 2,-1,-1, 1],
    [ 2,-1, 3, 1,-1],
    [-1, 3,-1, 5,-1],
    [-1, 1, 5,-1, 4],
    [ 1,-1,-1, 4,-1]]

def Kruskal_on_matrix(E):
    Q = PriorityQueue()
    n = len(E)
    result = []
    for i in range(n):
        for j in range(n):
            if E[i][j] >= 1:
                Q.put((E[i][j], (i, j)))
                E[i][j] = -1
                E[j][i] = -1

    A =[]
    for i in range(n):
        A.append(Node(i))

    start = Q.get()[1]
    Union(A[start[0]], A[start[1]])
    result.append(start)

    while not Q.empty():
        el = Q.get()[1]

        if Find(A[el[0]]) != Find(A[el[1]]):
            Union(A[el[0]], A[el[1]])
            result.append(el)


    return result


print(Kruskal_on_matrix(G))