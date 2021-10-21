A = [24, 17, 36, 79, 41, 92, 53 ,99]
B = [54, 39, 12, 66, 99]

def FindBiggestDiffrence(A):
    k = max(A)
    n = len(A)
    buckets = [[] for i in range(n+1)]
    for i in range(n):
        idx_b = A[i]//(k//n)
        buckets[idx_b].append(A[i])
    print(buckets)
    result = diff = 0
    i ,j = 0, 1  # wskaznikami bede porownywac najwiekszy element z jednego kubelka i najmniejszym z nastepnego niepustego kubelka
    while i < j and j <= n:
        if len(buckets[i]) > 0 and len(buckets[j]) > 0:
            diff = min(buckets[j]) - max(buckets[i])
            print(i, j)
            i+=1
            j+=1

        elif len(buckets[j]) == 0:
            j+=1
        elif len(buckets[i]) == 0 and len(buckets[j]) > 0 and j-i > 1:
            i+=1
        else:
            i+=1
            j+=1

        if diff > result:
            result = diff
    return result

print(FindBiggestDiffrence(B))