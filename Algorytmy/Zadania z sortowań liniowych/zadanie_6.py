A = [5, 3, 2, 2, 2, 3, 2, 2, 2, 2, 2, 2, 2]

def countingsort(A, k):
    n = len(A)
    output = [0 for _ in range(n)]
    counting = [0 for _ in range(k+1)]
    for i in range(n):
        counting[A[i][0]] += 1
    for i in range(1, k+1):
        counting[i] += counting[i-1]
    for i in range(n):
        counting[A[i][0]] -= 1
        output[counting[A[i][0]]] = A[i]
    for i in range(n):
        A[i] = output[i]



def BinarySearch(A, x, l, r):
    while l <= r:
        mid = (l+r)//2
        if A[mid][0] > x:
            r = mid - 1
        elif A[mid][0] < x:
            l = mid + 1
        else:
            A[mid][1] += 1
            return True
    return False

def SortingUniqueValuse(A):
    B = []
    for i in range(len(A)):
        result = BinarySearch(B, A[i], 0, len(B)-1)
        if result is False:
            B.append([A[i], 1])
            if len(B) > 1:
                countingsort(B, max(B)[0])

    k = 0
    for i in range(len(B)):
        while B[i][1] > 0:
            A[k] = B[i][0]
            k+=1
            B[i][1] -=1
    return A


print(SortingUniqueValuse(A))
