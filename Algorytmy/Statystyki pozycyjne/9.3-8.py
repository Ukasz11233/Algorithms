A = [2, 5, 7, 12, 19, 24]
B = [4, 5, 13, 21, 23, 30]

def MedianOfTwoArrays(A, B, n):
    if n == 0:
        return -1
    elif n == 1:
        return (A[0] + B[1])/2
    elif n == 2:
        return (max(A[0], B[0]) + min(A[1], B[1])) / 2
    else:
        m1 = Median(A, n)
        m2 = Median(B, n)
    if m1 > m2:
        if n % 2 == 0:
            return MedianOfTwoArrays(A[:int(n / 2) + 1], B[int(n / 2) - 1:], int(n / 2) + 1)
        else:
            return MedianOfTwoArrays(A[:int(n / 2) + 1], B[int(n / 2):], int(n / 2) + 1)
    else:
        if n % 2 == 0:
            return MedianOfTwoArrays(A[int(n / 2) - 1:], B[:int(n / 2) + 1], int(n / 2) + 1)
        else:
            return MedianOfTwoArrays(A[int(n / 2):], B[:int(n / 2) + 1], int(n / 2) + 1)


def Median(A, n):
    if n % 2 == 0:
        return (A[int(n / 2)] + A[int(n / 2) - 1]/2)
    else:
        return (A[int(n / 2)])

