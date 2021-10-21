# uzuasadnienie poprawnosci: uzywamy bucket sorta, poniewaz mamy przslanke, ze x znajduje sie na przedziale [0,1]
# rozlozonym w sposob jednostajny. Jako indeksy bucketow odwolujemy sie do x-ów pomnozonych
# przez ilosc ilementow w tablicy wejscowej.
# Dostajemy sie do nich poprzez zlogarytmizowanie kluczy w tablicy poprzez wartosc a.
# zlozonosc czasowa to: O(n)


import math

A = [pow(4, 1/2), pow(4, 1/300), pow(4, 1/60), pow(4, 1/3), pow(4, 1/8), pow(4, 1)]


def InsertionSort(A): # stabilny
    for i in range(1, len(A)):
        key = A[i]
        j = i-1
        while j >= 0 and int(A[j]) > int(key):
            A[j+1] = A[j]
            j -= 1
        A[j+1] = key
    return A


def fast_sort(tab, a):
    n = len(tab)
    buckets = [[] for _ in range(n+1)]
    for i in range(n):
        idx_b = int(math.log(A[i], a)*n)
        buckets[idx_b].append(A[i])
    for i in range(n):
        buckets[i] = InsertionSort(buckets[i])
    k = 0
    for i in range(n):
        for j in range(len(buckets[i])):
            tab[k] = buckets[i][j]
            k+=1

    return tab

print(fast_sort(A, 4))
