A =[(10,10),(15,25),(20,20),(30,40)]


def cost(A, B):
    return int(((A[0] - B[0])**2 + (A[1] - B[1])**2)**(1/2))


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
        if u < 0 and v < 0:
            continue
        if Find(A[u]) != Find(A[v]):
            Union(A[u], A[v])
            result.append(el)

    return result


def highway(A):
    n = len(A)
    E = []
    for i in range(n):
        for j in range(i, n):
            if i != j:
                E.append((i, j, cost(A[i], A[j])))

    min_days = float("inf")
    min_highways = None
    for i in range(len(E)):
        tmp = E[i]
        E[i] = (-1, -1, float("inf"))
        A = Kruskal(E)
        max_ = max(A, key=lambda item:item[2])[2]
        min_ = min(A, key=lambda item:item[2])[2]
        if min_days > max_ - min_:
            min_days = max_ - min_
            min_highways = A
        E[i] = tmp


    return min_days, min_highways


print(highway(A))
