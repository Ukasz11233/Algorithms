A = [4, 2, 6, 3, 10, 32, 64, 34, 23, 11, 65, 8]


def Mergesort(A, k):
    size = len(A)
    if size > 1:
        mid = size//2
        left_arr = A[:mid]
        right_arr = A[mid:]

        Mergesort(left_arr, k)
        Mergesort(right_arr, k)

        p, q, r, i = 0, 0, 0, 0

        left_size = len(left_arr)
        right_size = len(right_arr)
        while p < left_size:
            A[r] = left_arr[p]
            r += 1
            p += 1
        while q < right_size:
            A[r] = right_arr[q]
            r += 1
            q += 1
        while i + k < left_size + right_size:
            if A[i] > A[i+k]:
                A[i], A[i+k] = A[i+k], A[i]
            i += 1
Mergesort(A, 2)
print(A)