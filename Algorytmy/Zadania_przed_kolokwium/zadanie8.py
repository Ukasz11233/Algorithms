import math

A = [[2, 1], [4, 4], [5, 1], [8, 5], [2, 6], [6, 3], [7, 7]]


def Partition(A, low, high):
    i = (low-1)
    pivot = A[high]

    for j in range(low, high):
        if A[j] <= pivot:
            i += 1
            A[i], A[j] = A[j], A[i]
    A[i+1], A[high] = A[high], A[i+1]
    return (i+1)

def QuickSort(A,low, high):
    if len(A) == 1:
        return A
    if low < high:
        p = Partition(A, low, high)
        QuickSort(A, low, p-1)
        QuickSort(A, p+1, high)
    return A


def FindPlaceToHome(A):
    n = len(A)
    sufix = prefix = 0
    home = None
    A = QuickSort(A, 0, n-1)
    print(A)
    result = float("inf")
    for i in range(n):
        for k in range(i):
            prefix += (math.pow(A[k][0], 2) + math.pow(A[k][1], 2))
            print(prefix)
        prefix = math.sqrt(i*(math.pow(A[i][0], 2) + math.pow(A[i][1], 2)) - prefix)
        for j in range(i+1, n):
            sufix += (math.pow(A[j][0], 2) + math.pow(A[j][1], 2))
        sufix = math.sqrt(sufix - (n-i)*(math.pow(A[i][0], 2) + math.pow(A[i][1], 2)) )

        if result > sufix + prefix:
            home = A[i]
            result = sufix + prefix



# LUB


def Partition(A, low, high, x):
    for i in range(len(A)): #element x w tablicy ustawiam jako pivot, czyli na koncu tablicy
        if A[i] == x:
            A[i], A[high] = A[high], A[i]
            break

    pivot = A[high]
    i = low-1
    for j in range(low, high):
        if A[j] <= pivot:
            i+=1
            A[i], A[j] = A[j], A[i]
    A[i+1], A[high] = A[high], A[i+1]
    return i+1


def InsertionSort(A, start, end):
    for i in range(start, end):
        key = A[i]
        j = i - 1
        while j >= start and A[j] > key:
            A[j + 1] = A[j]
            j -= 1
        A[j + 1] = key
    return A


def FindMedian(A, left, right):
    InsertionSort(A, left, right)
    return A[(left+right)//2]


def Select(A, low, high, k):
   if k >= 0 and k < high - low +1:
        medians = []
        n = high - low
        i = 0
        while i < n//5:         # znajduje mediany kazdej pelnej piatki
            medians.append(FindMedian(A, low + i*5, low + i*5+5))
            i+=1

        if i*5 < n:        # ostatnia "piatka" ktora moze miec mniej niz 5 elementow
            medians.append(FindMedian(A, low + i*5, high))

        if len(medians) == 1:
            medofmed = medians[0]
        else:
            medofmed = Select(medians, 0, i, i//2)   # wybieram mediane median

        q = Partition(A, low, high-1, medofmed)
        if q-low == k:
            return A[q]
        if q-low > k:                        # rekurencyjnie dalej wyszukuje k-tego elementu
            return Select(A, low, q, k)
        else:
            return Select(A, q+1, high, k - (q-low) - 1)


def FindHome(A):
    n = len(A)
    if n % 2 == 0:
        x = Select(A, 0, n, n//2)
    else:
        x1 = Select(A, 0, n, math.floor(n//2))
        x = Select(A, 0, n, math.ceil(n//2))

    return x   # trzeba jeszcze obliczyc odleglosci i je dodac

print(FindHome(A))