A = [1, 2, 3, 4, 5, 6]


def BinarySearch(A, x, l, r):
    while l <= r:
        mid = (l + r)//2
        if x == A[mid]:
            return mid
        elif x > A[mid]:
            l = mid + 1
        else:
            r = mid -1
    return None

print(BinarySearch(A, 7, 0, len(A)-1))
