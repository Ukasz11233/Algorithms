# Łukasz Chmielewski
import math
from math import ceil

from zad3testy import runtests

P = [(1,5, 0.75) , (4,8, 0.25)]
T = [6.1, 1.2, 1.5, 3.5, 4.5, 2.5, 3.9, 7.8]


def BucketSort(B):
    if len(B) == 0:
        return []

    n = len(B)
    Buckets = [[] for _ in range(n+1)]
    result = []
    max_el = max(B)
    min_el = min(B)
    if max_el == min_el:
        for el in B:
            result.append(el)
        return result
    for i in range(n):
        idx_b = math.ceil(((B[i]-min_el)/(max_el - min_el))*n)
        Buckets[idx_b].append(B[i])
    print(Buckets)
    for i in range(n+1):
        for el in Buckets[i]:
            result.append(el)
    return result

def SortTab(T, P):
    n = len(T)
    Buckets = [[] for _ in range(n)]
    result = []

    for i in range(n):
        idx_b = int(T[i])
        Buckets[idx_b].append(T[i])

    for i in range(n):
        Buckets[i] = BucketSort(Buckets[i])

    for i in range(n):
        for el in Buckets[i]:
            result.append(el)

    return result

T2 =  [2.4, 7.9, 7.0, 2.8, 6.7, 3.8, 7.2, 6.8, 2.8, 7.5, 2.2, 6.9, 8.7, 2.8, 2.7, 7.7, 3.8, 3.5, 8.6, 2.5]
P2 = [(2,4, 0.5) , (6,9, 0.5)]

T3 =  [5.2, 2.7, 6.6, 3.9, 1.4, 4.8, 6.3, 7.0, 6.4, 1.1, 7.4, 5.4, 5.1, 4.3, 6.7, 7.2, 5.6, 7.7, 6.9, 1.6, 2.7, 4.1, 4.3, 6.5]
P3 = [(1,4, 0.25) , (4,7, 0.5) , (6,8, 0.25)]

print(SortTab(T2, P2))
runtests( SortTab )
