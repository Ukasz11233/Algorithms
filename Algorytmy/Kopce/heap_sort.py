A = [27, 17, 3, 16, 13, 10, 1, 5, 7, 12, 4, 8, 9, 0]
from max_heap_implementation import Parent, Right, Left, Max_Heapify, Build_Max_Heap, Heap_Maximum, Heap_Increase_Key, Max_Heap_Insert

def Heapsort(A):
    Build_Max_Heap(A)
    n = len(A)
    for i in range(len(A)-1, 0, -1):
        A[0], A[i] = A[i], A[0]
        n = n - 1
        Max_Heapify(A, 0, n)
    return A

def Heap_Delete(A, i):
    n = len(A)-1
    A[i], A[n] = A[n], A[i]
    A.pop()
    A = Heapsort(A)
    return A
print(Heapsort(A))
print(Heap_Delete(A, 0))
#budowanie kopca to O(n), a wszystkie operacje na kopcach to czas O(lgn)

