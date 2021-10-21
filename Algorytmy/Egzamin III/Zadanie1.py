from collections import deque

L = [ [ 2 ],
[ 2 ],
[ 0, 1, 3],
[ 2, 4 ],
[ 3, 5, 6 ],
[ 4 ],
[ 4 ] ]


def BFS(G, i):
    n = len(G)
    visited = [False]*n
    distance = [0]*n
    Q = deque()
    Q.append(i)
    while len(Q):
        u = Q.pop()
        visited[u] = True

        for el in G[u]:
            if visited[el] == False:
                Q.append(el)
                distance[el] = distance[u] + 1

    result = -float("inf")
    idx = 0
    for i in range(n):
        if distance[i] > result:
            result = distance[i]
            idx = i


    return result

def best_root(L):
    n = len(L)

    result = float("inf")
    idx = None
    for i in range(n):
        tmp = BFS(L, i)
        if tmp < result:
            result = tmp
            idx = i

    return idx

print(best_root(L))