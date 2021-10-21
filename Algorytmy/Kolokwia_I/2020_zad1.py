A = [123, 6733, 455, 2344]

def CountingSort(A, exp, B): #exp = 1
    output = [0]*len(A)
    counting = [0]*(10)
    for i in range(len(A)):
        if A[i] / exp > 1:
            idx = (A[i] / exp)
            counting[int(idx % 10)] += 1
            B[i][int(idx % 10)] += 1
    for i in range(1, 10):
        counting[i] += counting[i-1]
    for i in range(len(A)-1, -1, -1):
        idx = (A[i] / exp)
        output[counting[int(idx % 10)] - 1] = A[i]
        counting[int(idx % 10)] -= 1

def CountingSortArray(A, k, B): #exp = 1
    counting = [0]*(10)
    for i in range(len(A)):
        idx = (A[i][k])
        counting[int(idx % 10)] += 1
    for i in range(1, 10):
        counting[i] += counting[i-1]
    for i in range(len(A)-1, -1, -1):
        idx = (A[i][k])
        B[counting[int(idx % 10)] - 1] = A[i]
        counting[int(idx % 10)] -= 1
    for i in range(0, len(A)):
        A[i] = B[i]



def PrettySortArray(A, B):
    for i in range(9, -1, -1):
        CountingSortArray(A, i, B)

    output = [0]*len(A)
    i = 0
    for j in range(len(A)-1, -1, -1):
        output[i] = A[j][10]
        i += 1
    return output


def RadixSort(A):
    maxi = max(A)
    exp = 1
    B = [[0 for i in range(10)] for i in range(len(A))]
    C = [[0 for i in range(10)] for i in range(len(A))]
    while maxi / exp > 1:
        CountingSort(A, exp, B)
        exp *= 10
    for i in range(len(A)):         #cumulative sum tablicy B
        for j in range(10):
            if B[i][j] > 0:
                C[i][B[i][j]] += 1
        C[i].append(A[i])
    return C

def PrettySort(A):
    C = RadixSort(A)
    B = [[0 for i in range(10)] for i in range(len(A))]
    return PrettySortArray(C, B)

print(PrettySort(A))

#zlozonosc: O(n + n) = O(n) ; najpierw radix sort z counting sortem, pozniej znowu przerobiony
# radix sort z counting sortem.
