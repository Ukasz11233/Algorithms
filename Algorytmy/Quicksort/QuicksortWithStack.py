A = [3, 6, 5, 4, 7, 5]

class Stack():
    def __init__(self):
        self.stack = []

    def is_empty(self):
        return 1 if len(self.stack) == 0 else 0

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
    def push(self, x):
        self.stack.append(x)


def Partition(A, low, high):
    i = (low-1)
    pivot = A[high]

    for j in range(low, high):
        if A[j] <= pivot:
            i += 1
            A[i], A[j] = A[j], A[i]
    A[i+1], A[high] = A[high], A[i+1]
    return (i+1)


def Quicksort(A, low, high):
    S = Stack()
    S.push((low, high))
    while not S.is_empty():
        sub = S.pop()
        p = Partition(A, sub[0], sub[1])
        if sub[0] < p-1:
            S.push((sub[0], p-1))
        if sub[1] > p+1:
            S.push((p+1, sub[1]))
    return A

print(Quicksort(A, 0, 5))