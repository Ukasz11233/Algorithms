A = [174, 178, 179, 185, 169, 170, 182]

import random

def RandomizedPartition(A, p, r):
    i = random.randint(p, r)
    A[r], A[i] = A[i], A[r]
    return Partition(A, p ,r)

def Partition(A, p, r):
    i = (p - 1)
    pivot = A[r]

    for j in range(p, r):
        if A[j] <= pivot:
            i += 1
            A[i], A[j] = A[j], A[i]
    A[i + 1], A[r] = A[r], A[i + 1]
    return (i + 1)


def RandomizedSelect(A, p, r, i):
    if p == r:
        return A[p]
    q = Partition(A, p, r)
    k = q - p + 1
    if i == k:
        return A[q]
    elif i < k:
        return RandomizedSelect(A, p, q - 1, i)
    else:
        return RandomizedSelect(A, q+1, r, i-k)

def CountingSort(A):
    output = [0]*len(A)
    counting = [0]*(max(A)+1)
    for i in range(len(A)):
        counting[A[i]] += 1
    for i in range(1, max(A)+1):
        counting[i] = counting[i] + counting[i-1]
    for j in range(len(A)-1, -1, -1):
        output[counting[A[j]]-1] = A[j]
        counting[A[j]] -= 1
    return output


def Section(A, p, q):
    height_p = RandomizedSelect(A, 0, len(A) - 1, p)
    height_q = RandomizedSelect(A, 0, len(A) - 1, q)
    output = [height_p, height_q]
    for element in A:
        if element < height_p and element > height_q:
            output.append(element)
    return CountingSort(output)
print(Section(A, 5, 2))

#zlozonosc: O(2*n + n + n) = O(n) ; 2 razy wywolanie RandomizedSelect- zlozonosc O(n), jedna iteracja po tablicy
# - O(n) i posortowanie podtablicy coutnigsortem  < O(n).