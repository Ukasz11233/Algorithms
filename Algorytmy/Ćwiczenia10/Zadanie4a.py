from collections import deque

A = [(0, 4), (11, 14), (6, 7), (4, 8), (7, 11), (9, 13), (8, 11), (8, 9), (0, 6), (7, 11)]

def MakeGraph(A):
    n = len(A)
    G = [[] for _ in range(n)]
    A.sort(key=lambda x:x[0])

    for i in range(n):
        v = i
        while v < n and A[v][0] <= A[i][1]:
            if A[v][0] < A[i][1]:
                v +=1
            else:
                G[i].append(v)
                v += 1
    return G

def CheckInterval(A, a, b):    #zakladam ze przedzial (a, b) jest w tablicy A
    E = MakeGraph(A)
    n = len(A)
    visited = [False]*n
    Q = deque()
    print(A, E)

    possible = 0
    for i in range(n):
        if A[i][0] == a:
            Q.append(i)
            visited[i] = True
        if A[i][1] == b:
            possible = True

    if len(Q) == 0 or possible == False:
        return False


    while len(Q):
        v = Q.pop()
        if A[v][1] == b:
            return True
        for el in E[v]:
            if visited[el] == False:
                visited[el] = True
                Q.append(el)

    return False

print(CheckInterval(A, 2, 9))

