A = [0, 2, 2, 3, 4, 5, 6, 7]

def BinarySearch(A, l, r, x):
    if x > len(A): return False
    while l <= r:
        mid = (l + r)//2
        if x == mid and A[mid] == mid:
            return True
        elif A[mid] > x:
            r = mid - 1
        elif A[mid] < x:
            l = mid + 1
    return False

print(BinarySearch(A, 0, len(A)-1, 15))
