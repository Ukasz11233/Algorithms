from collections import deque

M = [[1, 1, 1, 1, 1, 1],
     [1, 1, 1, 0, 0, 1],
     [1, 1, 1, 1, 1, 1],
     [0, 1, 1, 1, 0, 1],
     [0, 1, 1, 0, 0, 1]
     ]


M2 = [[1, 1, 1, 0],
      [1, 1, 1, 0],
      [0, 0, 1, 1]
      ]
def BFS(M, n, m):
    visited = [[0]*m for _ in range(n)]
    Q = deque()

    Q.append((0, 0))
    visited[0][0] = 1

    while len(Q):
        v = Q.pop()
        print(v[0], v[1])
        if v[0] == n-1 and v[1] == m-1:
            return True

        if v[0] + 1 < n and visited[v[0]+1][v[1]] == 0 and M[v[0]+1][v[1]] == 1:
            visited[v[0]+1][v[1]] = 1
            Q.append((v[0]+1, v[1]))

        if v[1]+1 < m and visited[v[0]][v[1]+1] == 0 and M[v[0]][v[1]+1] == 1:
            visited[v[0]][v[1]+1] = 1
            Q.append((v[0], v[1]+1))

    return False
print(BFS(M, 5, 6))
