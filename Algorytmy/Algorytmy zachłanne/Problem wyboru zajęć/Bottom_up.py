S = [[1, 4], [3, 5], [0, 6], [5, 7], [3, 9], [5, 9], [6, 10], [8, 11], [8, 12], [2, 14], [12, 16]]


def Activity_selector(S, n):
    M = [0]*n
    for i in range(n):
        for j in range(i):
            if S[i][0] > S[j][1] and M[i] < M[j]:
                M[i] = M[j]
        M[i] += 1
    return max(M)

print(Activity_selector(S, 11))