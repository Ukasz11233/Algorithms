def Fib(n):
    R = [-1]*(n+1)
    R[0], R[1] = 0, 1
    return FibAux(R, n)


def FibAux(R, n):
    if R[n] >= 0:
        return R[n]
    else:
        R[n] = FibAux(R, n - 1) + FibAux(R, n - 2)
    return R[n]

print(Fib(8))