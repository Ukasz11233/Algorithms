A = [3

def CountingSort(A, exp): #exp = 1
    output = [0]*len(A)
    counting = [0]*(10)
    for i in range(len(A)):
        idx = (A[i] / exp)
        counting[int(idx % 10)] += 1
    for i in range(1, 10):
        counting[i] += counting[i-1]
    for i in range(len(A)-1, -1, -1):
        idx = (A[i] / exp)
        output[counting[int(idx % 10)] - 1]   = A[i]
        counting[int(idx % 10)] -= 1
    for i in range(0, len(A)):
        A[i] = output[i]

def RadixSort(A, n):
    exp = 1

    for i in range(3):
        CountingSort(A, exp)
        exp *=n
    return A

print(RadixSort(A, 6))