A = [17, 19, 24, 20, 35, 27, 29, 45, 22]

def parent(i):
    return (i-1)//2

def left(i):
    return 2*i + 1

def right(i):
    return 2*i + 2


def HeapBFS(A, n, x, k, i):
    visited = [0 for _ in range(n)]

    while i >= 0 and i < n:

        if k == 0 and A[i] >= x:
            return True
        print(visited)
        if left(i) < n:
            if A[left(i)] < x and visited[left(i)] == 0:
                k-=1
                i = left(i)
        if right(i) < n:
            if A[right(i)] <= x and visited[right(i)] == 0:
                k-=1
                i = right(i)
        else:
            visited[i] = 1
            i = parent(i)
huj w dupe temu gownie


def HeapFind(A, x, k):
    n = len(A)
    i = 0
    if A[i] > x:
        return False
    return HeapBFS(A, n, x, k-1, i)

print(HeapFind(A, 19, 1))