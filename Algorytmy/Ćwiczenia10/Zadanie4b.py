A = [(0, 4), (11, 14), (6, 7), (4, 8), (7, 11), (9, 13), (8, 11), (8, 9), (0, 6), (7, 11)]

def MakeGraph(A, k):
    n = len(A)
    G = [[] for _ in range(n)]
    A.sort(key=lambda x:x[0])

    for i in range(n):
        v = i
        while v < n and A[v][0] <= A[i][1]:
            print(v, i)
            if A[v][0] < A[i][1]:
                v +=1
            else:
                if len(G[i]) >= k:
                    break
                G[i].append(v)
                v += 1
    return G

def LongestInterval(A, k):    #zakladam ze przedzial (a, b) jest w tablicy A
    E = MakeGraph(A, k)
    n = len(A)
    G = [[(1, 6), (2, 7)],
     [(2, 8), (4, -4), (3, 5)],
     [(4, 9), (3, -3)],
     [(1, -2)],
     [(3, 7), (0, 2)]]

    visited = [False]*n
    max_dist = 0

    def DFSVisit(E, u, start, max_dist):
        if A[u][1] - A[start][0] > max_dist:
            max_dist = A[u][1] - A[start][0]

        for el in E[u]:
            if visited[el] == False:
                visited[el] = True
                max_dist = DFSVisit(E, el, start, max_dist)

        return max_dist

    for i in range(n):
        start = A[i][0]
        if visited[i] == False:
            dist = DFSVisit(E, i, start, max_dist)
            if dist > max_dist:
                max_dist = dist

    return max_dist

print(LongestInterval(A, 2))

