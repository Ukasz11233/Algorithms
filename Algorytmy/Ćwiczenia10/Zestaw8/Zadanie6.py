from queue import PriorityQueue

E = [[(1, 1), (2, 1)], [(3, 0)], [(3, 1), (1, 1)], [(6, 1), (4, 0)], [(5, 0)], [(6, 1)], []]

E2 = [[(1, 1), (2, 1)], [(3, 0)], [(4, 1)], [(5, 1)], [(6, 1)], [(7, 1)], [(8, 1)], [(9, 1)], [(10, 0)], [(11, 1)], [(12, 0)], [], [(11, 0)]]

def PrintSolution(P, i):
    if P[i] != 0:
        PrintSolution(P, P[i])
        print(P[i], end=" ")
    else:
        print(P[i], end=" ")

def EdgeZeroOne(E, s, t):
    Q = PriorityQueue()
    n = len(E)
    visited = [0]*n
    parent = [0]*n
    Q.put((0, s))
    visited[s] = 1

    while Q.qsize():
        u = Q.get()
        visited[u[1]] = 1
        if u[1] == t:
            PrintSolution(parent, t)
            print(t, end=" ")
            return True
        for el in E[u[1]]:
            if visited[el[0]] == 0:
                if el[1] == 1:
                    Q.put((1, el[0]))
                else:
                    Q.put((0, el[0]))
                parent[el[0]] = u[1]

    return False

print(EdgeZeroOne(E2, 0, 11))