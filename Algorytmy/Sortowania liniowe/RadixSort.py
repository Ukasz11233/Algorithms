A = [123, 536, 235, 622, 267, 234, 1244, 6324, 123, 6435]


def CountingSort(A, exp):    #exp = 1
    output = [0]*len(A)
    counting = [0]*10
    for i in range(len(A)):
        idx = (A[i] / exp)
        counting[int(idx % 10)] += 1
    for i in range(1, 10):
        counting[i] += counting[i-1]
    for i in range(len(A)-1, -1, -1):
        idx = (A[i] / exp)
        output[counting[int(idx % 10)] - 1] = A[i]
        counting[int(idx % 10)] -= 1
    for i in range(0, len(A)):
        A[i] = output[i]

def RadixSort(A):
    maxi = max(A)
    exp = 1

    while maxi / exp > 0:
        CountingSort(A, exp)
        exp *= 10
    return A

