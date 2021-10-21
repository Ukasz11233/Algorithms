A = [0, 10, 13, 12, 7]


def Change_array_base(A):
    n = len(A)
    for i in range(n):
        A[i] = change_to(A[i], n)
    return A

def change_to(x, k):
    result = 0
    while x >= k:
        x -= k
        result += 1
    result *= 10
    result += (x % k)
    return result


def RadixSort(A):
    n = len(A)
    A = Change_array_base(A)
    x = max(A)
    exp = 1
    while x // exp :
        A = CountingSort(A, exp)
        exp *= 10

    return A


def CountingSort(A, exp):
    n = len(A)
    C = [0]*10
    B = [0]*n

    for i in range(n):
        idx = A[i]/exp
        C[int(idx % 10)] += 1

    for i in range(1, n):
        C[i] += C[i-1]

    for i in range(n-1, -1, -1):
        idx = int((A[i]/exp) % 10)
        C[idx] -= 1
        B[C[idx]] = A[i]

    return B



print(RadixSort(A))