P = [[1, 1], [2, 5], [3, 8], [4, 9], [5, 10], [6, 17], [7, 17], [8, 20], [9, 24], [10, 30]]

def Bottom_up(P, n, c):
    R = [0]*(n+1)

    for j in range(1, n+1):
        q = -float("inf")
        for i in range(1, j+1):
            q = max(q, P[i-1][1] + R[j - i] - c)
        R[j] = q
    return R[n]

print(Bottom_up(P, 4, 1))