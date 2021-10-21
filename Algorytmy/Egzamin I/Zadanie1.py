from queue import PriorityQueue

G1 = [ [0,5,1,8,0,0,0 ],
[5,0,0,1,0,8,0 ],
[1,0,0,8,0,0,8 ],
[8,1,8,0,5,0,1 ],
[0,0,0,5,0,1,0 ],
[0,8,0,0,1,0,5 ],
[0,0,8,1,0,5,0 ] ]


G2 = [[0, 1, 5, 0],
      [1, 0, 1, 1],
      [5, 1, 0, 1],
      [0, 1, 1, 0]]

def Relax(dist, color, u, v, w):
    if dist[v] >= dist[u] + w:
        dist[v] = dist[u] + w
        color[v] = w


def islands(G, A, B):
    n = len(G)
    dist = [float("inf")]*n
    visited = [False]*n
    color = [None]*n
    dist[A] = 0
    Q = PriorityQueue()
    Q.put((0, A))

    while not Q.empty():
        u = Q.get()[1]
        visited[u] = True

        for i in range(n):
            if G[u][i] > 0:
                if visited[i] == False and color[u] != G[u][i]:
                    Relax(dist, color, u, i, G[u][i])
                    Q.put((dist[i], i))

    return dist[B] if dist[B] > 0 else None

print(islands(G1, 5, 2))