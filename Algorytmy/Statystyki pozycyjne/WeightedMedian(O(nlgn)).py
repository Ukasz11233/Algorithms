A = [3, 5, 2, 4, 6, 1, 7]
W = [0.1, 0.05, 0.1, 0.05, 0.2, 0.15, 0.35]

# O(nlgn) bo Mergesort

def Mergesort(A):
    size = len(A)
    if size > 1:
        mid = size // 2
        left_arr = A[:mid]
        right_arr = A[mid:]

        Mergesort(left_arr)
        Mergesort(right_arr)

        p, q, r = 0, 0, 0

        left_size = len(left_arr)
        right_size = len(right_arr)
        while p < left_size and q < right_size:
            if left_arr[p][1] < right_arr[q][1]:
                A[r] = left_arr[p]
                p+=1
            else:
                A[r] = right_arr[q]
                q+=1
            r+=1

        while p < left_size:
            A[r] = left_arr[p]
            p+=1
            r+=1

        while q < right_size:
            A[r] = right_arr[q]
            q+=1
            r+=1


def Weighted_Median(A, W):
    pairs = []
    for i in range(len(A)):
        pairs.append((A[i], W[i]))
    Mergesort(pairs)

    if len(pairs) % 2 != 0:
        sum = 0
        for key, weight in pairs:
            sum += weight
            if sum >= 0.5:
                return key
    else:
        sum = 0
        for key, weight in pairs:
            sum += weight
            if sum >= 0.5:
                return key
        sum = 0
        for i in range(len(A)-1, -1, -1):
            key = pairs[i][0]
            weight = pairs[i][1]
            sum += weight
            if sum >= 0.5:
                return key

print(Weighted_Median(A, W))