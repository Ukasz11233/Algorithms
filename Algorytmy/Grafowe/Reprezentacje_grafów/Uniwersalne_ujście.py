M = [[0, 1, 1, 0], [0, 0, 1, 1], [0, 0, 0, 0], [0, 0, 1, 0]]

def FindUniwersalOutlet(M):
    i, j = 0, 0
    n = len(M)

    while i < n and j < n:
        if M[i][j] == 0:
            j += 1
        else:
            i += 1

    return (i if j == n and i != n else None )

print(FindUniwersalOutlet(M))