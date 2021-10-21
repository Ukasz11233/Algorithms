A = [(6, 10), (6, 10), (5, 11), (4, 10), (3, 5), (2, 6), (1, 3), (1, 2), (0, 5)]

def MaxSubset(A):
    n = len(A)
    A.sort(key= lambda x:x[0])
    print(A)
    result = []
    deleted = [0]*n


    for i in range(n):
        for j in range(i+1, n, 1):
            if deleted[j] == 0:
                if A[i][0] <= A[j][0] and A[i][1] >= A[j][1]:
                    deleted[i] = 1
                    break


    print(deleted)

    for i in range(n):
        if deleted[i] == 0:
            result.append(A[i])
    return result


print(MaxSubset(A))