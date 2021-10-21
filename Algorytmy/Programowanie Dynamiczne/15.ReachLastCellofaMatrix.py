def RLCM2(A, i, j, L):
    if i == len(A) or j == len(A[0]):
        return float("inf")
    if i == len(A)-1 and j == len(A[0])-1:
        return A[len(A)-1][len(A[0])-1]
    if L[i][j] > 0:
        return L[i][j]
    else:
        q1 = float("inf")
        q2 = min(RLCM2(A, i+1, j, L), RLCM2(A, i, j+1, L)) + A[i][j]
        L[i][j] = min(q1, q2)
    return L[i][j]

def Write(L):
    for i in range(len(L)):
        for j in range(len(L[0])):
            print(L[i][j], end=" ")
        print()


if  __name__ == "__main__":
    A = [[4, 7, 6, 8, 4],
         [6, 7, 3, 9, 2],
         [3, 8, 1, 2, 4],
         [7, 1, 7, 3, 7],
         [2, 9, 8, 9, 3]]
    L = [[ 0 for i in range(len(A[0]))] for i in range(len(A))]

    print(RLCM2(A, 0, 0, L))
    Write(L)