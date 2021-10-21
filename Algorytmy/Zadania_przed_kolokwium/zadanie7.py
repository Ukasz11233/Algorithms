A = [4, 11, 12 ,19, 23, 52, 99]

def BucketSort(A):
    k = max(A)
    n = len(A)
    buckets = [[] for _ in range(n+1)]

    for i in range(n):
        idx_b = (A[i]//(k//n))
        buckets[idx_b].append(A[i])
    i = 0
    j = 1
    diff = result = 0
    print(buckets)
    while i < j and j <= n:
        if len(buckets[i]) > 0 and len(buckets[j]) > 0:
            diff = min(buckets[j]) - max(buckets[i])
            i +=1
            j +=1
        elif len(buckets[i]) > 0 and len(buckets[j]) ==0:
            j+=1
        else:
            i+=1
            j+=1
        if diff > result:
            result = diff
    return result

print(BucketSort(A))