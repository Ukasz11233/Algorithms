# Łukasz Chmielewski
from zad1testy import runtests

def Partition(arr, l, r, x):
    for i in range(l, r):
        if arr[i] == x:
            arr[r], arr[i] = arr[i], arr[r]
            break

    x = arr[r]
    i = l
    for j in range(l, r):
        if (arr[j] <= x):
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
    arr[i], arr[r] = arr[r], arr[i]
    return i


def insertionSort(A):
    for i in range(1, len(A)):
        up = A[i]
        j = i - 1
        while j >= 0 and A[j] > up:
            A[j + 1] = A[j]
            j -= 1
        A[j + 1] = up
    return A


def FindMedian(A, l, n):
    arr = []
    for i in range(l, l+n):
        arr.append(A[i])
    arr = insertionSort(arr)
    return arr[n//2]


def Select(A, l, r, k):
    if k > 0 and k <= r - l + 1:
        n = r - l + 1
        median = []
        i = 0

        while i < n // 5:
            median.append(FindMedian(A, l+i*5, 5))
            i += 1

        if i*5 < n:
            median.append(FindMedian(A, l+i*5, n % 5))
            i += 1

        if i == 1:
            med_of_med = median[i-1]
        else:
            med_of_med = Select(median, 0, i-1, i//2)

        q = Partition(A, l, r, med_of_med)

        if q - l == k - 1:
            return A[q]
        if q - l > k - 1:
            return Select(A, l, q-1, k)

        return Select(A, q+1, r, k-q+l-1)



T = [[2, 3, 5],
     [7, 11, 13],
     [17, 19, 23]]


def Median(T):
    n = len(T)
    A = []
    for i in range(n):
        for j in range(n):
            A.append(T[i][j])

    p1 = Select(A, 0, n*n-1, (n*n - n)//2 + 1)
    p2 = Select(A, 0, n*n-1, (n*n + n)//2 )

    i = -1
    k = (n*n -n)//2
    l = (n*n + n)//2

    for j in range(n):
        if A[j] < p1:
            i += 1
            A[i], A[j] = A[j], A[i]
        elif A[j] > p1 and A[j] < p2:
            k += 1
            A[k], A[j] = A[j], A[k]
        elif A[j] > p2:
            l += 1
            A[l], A[j] = A[j], A[l]

    down, mid, up = 0, (n*n -n)//2 , (n*n + n)//2
    print(down, mid, up)
    for i in range(len(T)):
        for j in range(len(T)):
            if i == j:
                T[i][j] = A[mid]
                mid += 1
            elif i < j:
                T[i][j] = A[up]
                up += 1
            elif i > j:
                T[i][j] = A[down]
                down += 1


    for i in range(len(T)):
        for j in range(len(T)):
            print(T[i][j], end=" ")
        print()

    return T



runtests( Median )
