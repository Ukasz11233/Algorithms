A = ["aaa", "aab", "bab", "b", "ac", "ab"]



def CountingSort(A, exp): #exp = 1
    output = [0]*len(A)
    counting = [0]*(26)
    for i in range(len(A)):
        idx = len(A[i])-exp
        counting[int(idx % 26)] += 1
    for i in range(1, 26):
        counting[i] += counting[i-1]
    for i in range(len(A)-1, -1, -1):
        idx = len(A[i]) - exp
        output[counting[int(idx % 26)] - 1]   = A[i]
        counting[int(idx % 26)] -= 1
    for i in range(0, len(A)):
        A[i] = output[i]

def RadixSort(A):
    maxi = max(A)
    exp = 0

    while maxi[:len(maxi)-exp]:
        CountingSort(A, exp)
        exp +=1
    return A



def SortingArray(A, n):
    B = []
    for i in range(n):
        B.append([])
    for i in range(len(A)):
        tmp = A[i]
        idx_b = 0
        while tmp:
            tmp = tmp[:len(tmp)-1]
            idx_b +=1
        B[idx_b].append(A[i])
    print(B)
    for i in range(len(B)):
        if len(B[i]) > 0:
            B[i] = RadixSort(B[i])

    k = 0
    for i in range(len(B)):
        for j in range(len(B[i])):
            A[k] = B[i][j]
            k += 1
    return A

print(SortingArray(A, 16))