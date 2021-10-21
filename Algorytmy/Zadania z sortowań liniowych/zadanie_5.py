A = [1, 14, 3, 10, 11, 5, 12, 4, 5, 2, 15, 1, 14, 17, 18, 11, 13, 1, 2, 4]

# 5, 4, 3, 4

def InsertionSort(A):
    for i in range(1, len(A)):
        key = A[i]
        j = i - 1
        while j >= 0 and A[j] > key:
            A[j+1] = A[j]
            j -= 1
        A[j+1] = key
    return A


def CountingSort(A, k):
    counting = [0]*(k+1)
    output = [0]*(len(A)-10)
    rest = []
    for i in range(len(A)):
        if A[i] <=k and A[i] > 0:
            counting[A[i]] += 1
        else:
            rest.append(A[i])

    for i in range(1, len(counting)):
        counting[i] += counting[i-1]
    rest = InsertionSort(rest)

    for i in range(len(A)):
        if A[i] <= k and A[i] > 0:
            output[counting[A[i]]-1] = A[i]
            counting[A[i]] -= 1

    for i in range(len(A)-10):
        A[i] = output[i]

    k = 0
    for i in range(len(A)-10, len(A)):
        A[i] = rest[k]
        k+=1

    return A

print(CountingSort(A, 5))