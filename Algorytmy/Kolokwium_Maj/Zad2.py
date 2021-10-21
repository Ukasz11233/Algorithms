#Łukasz Chmielewski
from queue import Queue
from zad2testy import runtests

G1 = [ [1, 2],
       [0, 2],
       [0, 1] ]
s1 = 0
t1 = 2
r1 = (0,2)

G2 = [ [1,4],  # 0
       [0,2],  # 1
       [1,3],  # 2
       [2,5],  # 3
       [0,5],  # 4
       [4,3]]  # 5
s2 = 0
t2 = 3

G4 = [ [1,4,3],  # 0
       [0,2],    # 1
       [1,3],    # 2
       [2,5,0],  # 3
       [0,5],    # 4
       [4,3]]    # 5
s4 = 0
t4 = 2
r4 = None

def BFS(G, deleted, s):
    n = len(G)
    visited = [False]*n
    dist = [0]*n
    Q = Queue()
    Q.put(s)
    visited[s] = True
    distance = 0
    while not Q.empty():
        u = Q.get()
        for i in range(len(G[u])):
            if deleted[u][i] == False and visited[G[u][i]] == False:
                visited[G[u][i]] = True
                Q.put(G[u][i])
                dist[G[u][i]] = dist[u] + 1

    return dist


def enlarge(G, s, t):
    n = len(G)

    deleted = [[] for _ in range(n)]
    for i in range(n):
        for el in G[i]:
            deleted[i].append(False)

    counter = [0]*n

    A = BFS(G, deleted, s)
    B = BFS(G, deleted, t)
    path_length = A[t]

    for i in range(n):
        if A[i] + B[i] == path_length:
            counter[i] += 1

    result = []
    for i in range(n):
        if counter[i] == 1:
            for j in range(len(G[i])):
                if deleted[i][j] == False and counter[G[i][j]] == 1:
                    result.append((i, G[i][j]))
                    tmp = G[i][j]
                    deleted[i][j] = True
                    for k in range(len(G[tmp])):
                        if G[tmp][k] == i:
                            deleted[tmp][k] = True
                            break
                    final_length = BFS(G, deleted, s)

                    if final_length[t] > path_length:
                        return (i, G[i][j])
                    else:
                        deleted[i][j] = False
                        deleted[tmp][k] = False

    return None

#print(enlarge(G4, 0, 2))
runtests(enlarge)