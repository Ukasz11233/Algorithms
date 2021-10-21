A = [0, 1, 2, 3, 4, 4, 3, 5, 1, 9, 4]

def BiggestGCD(A, n):
    buckets = [[] for _ in range(n)]
    for i in range(n):
        tmp = A[i]
        norm = 2
        while norm <= tmp:
            if tmp % norm == 0:
                buckets[norm].append(tmp)
            norm += 1
    max_length = 0
    for i in range(n):
        length = len(buckets[i])
        if length > max_length:
            max_length = length
    return max_length

print(BiggestGCD(A, 10))