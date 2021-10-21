A = [4, 6, 5, 3, 1, 2, 8, 7, 9, 10 ,11, 12]

def Mergesort(A, low, high):
    size = high - low + 1
    if size > 1:
        mid = (high-low+1)//2
        print(mid)
        Mergesort(A, low, mid)
        Mergesort(A, mid+1, high)

        output = [0]*len(A)
        p, q, r = low, low, low

        left_size = len(left_arr)
        right_size = len(right_arr)
        while p < left_size and q < right_size:
            if left_arr[p] < right_arr[q]:
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
        return A

def MergeSorted(A, low, high, n, m):
    if high - low +1 == m:
        Mergesort(A, low, high)
        print(A)
    if high - low +1 > 3:
        mid = (high - low+1)//2
        MergeSorted(A, low, mid, n, m)
        MergeSorted(A, mid, high, n, m)

    return A

print(Mergesort(A, 3, 6))
