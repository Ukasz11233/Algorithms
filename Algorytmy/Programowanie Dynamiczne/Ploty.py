A = [1, 2, 8, 4, 3, 7, 1, 9, 2, 1, 3]


def PrintResult(A, x, stop):
    for i in range(x, stop):
        print(A[i], end=" ")


def Fence(A, k):
    n = len(A)

    F = [[-1]*n for _ in range(k+1)]
    output = [[-1]*n for _ in range(k+1)]
    F[1][0] = A[0]
    for i in range(1, n):
        F[1][i] = F[1][i-1] + A[i]
    maxx = 0
    l = 1
    for i in range(2, k+1):
        for j in range(1, n):
            q_max = -1
            for x in range(j):
                q = min(F[i-1][x], F[1][j] - F[1][x])
                if q_max < q:
                    q_max = q
                    idx = x
            output[i][idx] = idx
            F[i][j] = q_max
        l += 1

    print(output)
    print("")
    return F[k][n-1]



def puotki(A,k):
    n = len(A)
    T = [ [-1]*n for i in range(k+1) ]

    def f(i, j, A):
        if T[i][j] >= 0: # TABLICA
            return T[i][j]
        if i == 0:
            T[i][j] = 0 # TABLICA
            return 0
        if i == 1:
            summ = 0
            for s in range(j + 1):
                summ += A[s]
            T[i][j] = summ # TABLICA
            return summ

        max_now = 0
        for p in range(j):
            summ = 0
            for l in range(p, j + 1):
                summ += A[l]
            fval = f(i - 1, p-1, A) # TU BYŁO    fval = f(i - 1, p, A)
            min_local = min(fval, summ)
            max_now = max(max_now, min_local)
        T[i][j] = max_now # TABLICA
        print(T)
        return max_now

    return f(k,n-1,A)

print(puotki(A, 2))
#print(Fence(A, 3))