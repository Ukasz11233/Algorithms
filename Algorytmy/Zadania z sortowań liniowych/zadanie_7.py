A = [11, 4, 14, 13, 15]

def CountingSort(A, exp):
    counting = [0]*len(A)
    output = [0]*len(A)
    for i in range(len(A)):
        idx = A[i]//exp
        counting[idx % len(A)] += 1
    for i in range(1, len(counting)):
        counting[i] += counting[i-1]
    for i in range(len(A)-1, -1, -1):
        idx = A[i]//exp
        output[counting[idx % len(A)]-1] = A[i]
        counting[idx % len(A)] -= 1
    print(output)
    for i in range(len(A)):
        A[i] = output[i]


def RadixSort(A):
    maxi = max(A)
    exp = 1
    n = len(A)
    while maxi//exp > 1:
        CountingSort(A, exp)
        exp *= n
    return A


def radixsort(A, k):
    n = len(A)
    output = [0 for i in range(n)]
    counting = [0 for i in range(k+1)]

    for i in range(k):
        counting[A[i]%k] += 1
    for i in range(1, k):
        counting[i] += counting[i-1]
    for i in range(n-1, -1, -1):
        counting[A[i]%k] -= 1
        output[counting[A[i]%k]] = A[i]

    counting = [0 for i in range(k)]

    for i in range(k):
        counting[A[i]//k] += 1
    for i in range(1, k):
        counting[i] += counting[i-1]
    for i in range(n-1, -1, -1):
        counting[output[i]//k] -= 1
        A[counting[output[i]//k]] = output[i]
    return A
print(radixsort(A, 5)