def parent(i):
    return (i-1)//2

def left(i):
    return 2*i + 1

def right(i):
    return 2*i + 2

def max_heapify(A, i, n):
    l = left(i)
    r = right(i)
    if l < n and A[l] > A[i]:
        largest = l
    else:
        largest = i

    if r < n and A[r] > A[i]:
        largest = r

    if largest != i:
        A[i], A[largest] = A[largest], A[i]
        max_heapify(A, largest, n)

def min_heapify(A, i, n):
    l = left(i)
    r = right(i)
    if l < n and A[l] < A[i]:
        smallest = l
    else: smallest = i

    if r < n and A[r] < A[smallest]:
        smallest = r

    if smallest != i:
        A[i], A[smallest] = A[smallest], A[i]
        min_heapify(A, smallest, n)

def build_max_heap(A):
    for i in range(len(A)//2, -1, -1):
        max_heapify(A, i, len(A))
    return A

def build_min_heap(A):
    for i in range(len(A)//2, -1, -1):
        min_heapify(A, i, len(A))
    return A

def remove_min(A):
    n = len(A)
    A[0], A[n-1] = A[n-1], A[0]
    result = A.pop()
    min_heapify(A, 0, len(A))
    return result

def remove_max(A):
    n = len(A)
    A[0], A[n-1] = A[n-1], A[0]
    result = A.pop()
    max_heapify(A, 0, n-1)
    return result

def heap_sort(A):
    A = build_min_heap(A)
    n = len(A)
    for i in range(len(A)-1, 0, -1):
        A[0], A[i] = A[i], A[0]
        min_heapify(A, 0, i)
    for i in range(len(A)//2):
        A[i], A[n-i-1] = A[n-i-1], A[i]
    return A


def build_median_heap(A): #O(nlgn)
    A = heap_sort(A)
    min_heap = build_min_heap(A[len(A)//2:])
    max_heap = build_max_heap(A[:len(A)//2])
    return min_heap, max_heap

def remove_median(A):
    min_heap, max_heap = build_median_heap(A)
    if len(min_heap) == len(max_heap):
        x1 = remove_min(min_heap)
        x2 = remove_max(max_heap)
        print("opcja 1", x1, x2)
        return (x1 + x2)/2
    else:
        print("opcja 2")
        return remove_min(min_heap)

def insert_to_median_heap(min_heap, max_heap, key):
    if key < max_heap[0]:
        max_heap.append(key)
        i = len(max_heap) - 1
        while i > 0 and max_heap[i] > max_heap[parent(i)]:
            max_heap[parent(i)], max_heap[i] = max_heap[i], max_heap[parent(i)]
            i = parent(i)
    else:
        min_heap.append(key)
        i = len(min_heap) - 1
        while i > 0 and min_heap[i] < min_heap[parent(i)]:
            min_heap[parent(i)], min_heap[i] = min_heap[i], min_heap[parent(i)]
            i = parent(i)

if __name__ == "__main__":
    A = [6, 5, 3, 2, 7, 8]
    min_heap, max_heap = build_median_heap(A)
    print(min_heap, max_heap)
    insert_to_median_heap(min_heap, max_heap, 5)
    print(min_heap)