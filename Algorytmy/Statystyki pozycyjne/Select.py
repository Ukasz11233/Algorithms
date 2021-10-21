A = [4, 5, 7, 12, 54, 23, 7, 54, 85, 32, 13, 63, 23 ,46 ,23 ,32, 11, 75, 32, 20, 10, 1]

# Median of medians
#the worst case and expected is O(n)

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



print(Select(A, 0, len(A)-1, 3))
