A = [2, 4, 6, 7, 8, 9]

def binary_search(A, l, r, x):
    if r >= l:
        mid = (l+r) // 2
        if A[mid] == x:
            return mid
        elif A[mid] > x:
           return binary_search(A, l, mid-1, x)
        else:
           return binary_search(A, mid+1, r, x)
    else:
        return -1
print(binary_search(A, 0, len(A)-1, 4))