def LSS(M, L, r, c, maxsize):
    if r == 0 or c == 0:
        if maxsize != 0:
            return M[r][c], max(maxsize, M[r][c])
        for i in range(r + 1):
            if M[i][c] == 1:
                return 1, 1
        for i in range(c + 1):
            if M[r][i] == 1:
                return 1, 1
        return 0, 0
    if L[r][c] > 0:
        return L[r][c], L[r][c]
    left, maxsize = LSS(M, L, r, c-1, maxsize)
    top, maxsize = LSS(M, L, r-1, c, maxsize)
    diagonal, maxsize = LSS(M, L, r-1, c-1, maxsize)


    size = 1 + min(min(top, left), diagonal) if M[r][c] != 0 else 0
    L[r][c] = max(maxsize, size)
    return size, L[r][c]

if __name__ == "__main__":
    M = [
        [0, 0, 1, 0, 1, 1],
        [0, 1, 1, 1, 0, 0],
        [0, 0, 1, 1, 1, 1],
        [1, 1, 0, 1, 1, 1],
        [1, 1, 1, 1, 1, 1],
        [1, 1, 0, 1, 1, 1],
        [1, 0, 1, 1, 1, 1],
        [1, 1, 1, 0, 1, 1]
    ]
    L = [[0 for _ in range(len(M[0]))] for _ in range(len(M))]

    print(LSS(M, L, len(M)-1, len(M[0])-1, 0))