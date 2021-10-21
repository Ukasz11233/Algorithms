A = [174, 178, 179, 185, 169, 170, 182]

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



def linearselect(A, k):       # najmniejszy element to 0, najwiekszy to len(A)-1
    return Select(A, 0, len(A), k)


def CountingSort(A):
    output = [0] * len(A)
    counting = [0] * (max(A) + 1)
    for i in range(len(A)):
        counting[A[i]] += 1
    for i in range(1, max(A) + 1):
        counting[i] = counting[i] + counting[i - 1]
    for j in range(len(A) - 1, -1, -1):
        counting[A[j]] -= 1
        output[counting[A[j]]] = A[j]
    return output

def section(T, p, q):
    p_height = linearselect(T, p)
    q_height = linearselect(T, q)
    result = [p_height, q_height]
    for el in T:
        if el > q_height and el < p_height:
            result.append(el)
    return CountingSort(result)

print(section(A, 4, 1))