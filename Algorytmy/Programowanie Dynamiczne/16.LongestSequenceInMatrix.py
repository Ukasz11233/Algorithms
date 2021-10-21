def isValid(M, i, j):
    return 0 <= i < len(M) and 0 <= j < len(M[0])

def LSIM(M, i, j):
    if not isValid(M, i, j):
        return None

    path = None

    if i > 0 and M[i-1][j] == M[i][j] + 1:
        path = LSIM(M, i-1, j)
    if j > 0 and M[i][j-1] == M[i][j] + 1:
        path = LSIM(M, i, j-1)
    if i + 1 < len(M) and M[i+1][j] == M[i][j] + 1:
        path = LSIM(M, i+1, j)
    if j + 1 < len(M[0]) and M[i][j+1] == M[i][j] + 1:
        path = LSIM(M, i, j+1)
    return f"{M[i][j]} - {path}" if path  else f"{M[i][j]}"

if __name__ == "__main__":
    M = [
            [10, 13, 14, 21, 23],
            [11, 9, 22, 2, 3],
            [12, 8, 1, 5, 4],
            [15, 24, 7, 6, 20],
            [16, 17, 18, 19, 25]
        ]
    res_size = -float("inf")
    for i in range(len(M)):
        for j in range(len(M[0])):
            str = LSIM(M, i, j)
            size = str.count('-')
            if size > res_size:
                result = str
                res_size = size
    print(result)

#mysle ze nie pojawi sie taki problem na zajeciach