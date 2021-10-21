A = "ABC"
B = "ABB"


def PrintSolution(A, B, F, i, j):
    if i == 0 or j == 0:
        return

    if A[i-1] == B[j-1]:
        PrintSolution(A, B, F, i-1, j-1)
        print(A[i-1], end=" ")
    else:
        if F[i-1][j] < F[i][j-1]:
            PrintSolution(A, B, F, i-1, j)
            print(B[j-1], end=" ")
        else:
            PrintSolution(A, B, F, i, j-1)
            print(A[i-1], end=" ")

def SCS(A, B):
    n = len(A)
    m = len(B)

    F = [[0]*(m+1) for _ in range(n+1)]

    for i in range(n+1):
        F[i][0] = i
    for i in range(m+1):
        F[0][i] = i

    for i in range(1, n+1):
        for j in range(1, m+1):
            if A[i-1] == B[i-1]:
                F[i][j] = F[i-1][j-1] + 1
            else:
                F[i][j] = min(F[i-1][j], F[i][j-1]) + 1


    PrintSolution(A, B, F, i, j)
    print("")
    return F[-1][-1]


print(SCS(A, B))