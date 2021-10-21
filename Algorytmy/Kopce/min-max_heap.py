from max_heap_implementation import Left, Right, Parent

A = [27, 17, 3, 16, 13, 10, 1, 5, 7, 12, 4, 8, 9, 0]


def level(i):
    return (i+1).bit_length() - 1

def Floyd_Build_Heap(A):
    for i in range(len(A)//2, -1, -1):
        Push_Down(A, i)
    return A


def Push_Down(A, i):
    if level(i) % 2 == 0:   #min level
        Push_Down_Min(A, i)
    else:  #max level
        Push_Down_Max(A, i)


def Push_Down_Min(A, i):
    if i*2+1 < len(A):   #i has children
        m = i*2 + 1
        if i*2 + 2 < len(A) and A[i*2 + 2] < A[m]:
            m = i*2 + 2
        child = True
        for j in range(i*4 + 3, min(i*4 + 7, len(A))):
            if A[j] < A[m]:
                m = j
                child = False
        if child:
            if A[m] < A[i]:
                A[m], A[i] = A[i], A[m]
        else:
            if A[m] < A[i]:
                A[m], A[i] = A[i], A[m]
            if A[m] > A[(m-1) // 2]:
                A[m], A[(m-1) // 2] = A[(m-1) // 2], A[m]
                Push_Down_Min(A, m)


def Push_Down_Max(A, i):
    if i*2+1 < len(A):   #i has children
        m = i*2 + 1
        if i*2 + 2 < len(A) and A[i*2 + 2] > A[m]:
            m = i*2 + 2
        child = True
        for j in range(i*4 + 3, min(i*4 + 7, len(A))):
            if A[j] > A[m]:
                m = j
                child = False
        if child:
            if A[m] > A[i]:
                A[m], A[i] = A[i], A[m]
        else:
            if A[m] > A[i]:
                A[m], A[i] = A[i], A[m]
            if A[m] < A[(m-1) // 2]:
                A[m], A[(m-1) // 2] = A[(m-1) // 2], A[m]
                Push_Down_Max(A, m)

def Push_Up(A, i):
    if level(i) % 2 == 0:  #min level
        if i > 0 and A[i] > A[(i-1) // 2]:
            A[i], A[(i-1) // 2] = A[(i-1) // 2], A[i]
            Push_Up_Max(A, i)
        else:
            Push_Up_Min(A, i)
    else:
        if i > 0 and A[i] < A[(i - 1) // 2]:
            A[i], A[(i - 1) // 2] = A[(i - 1) // 2], A[i]
            Push_Up_Min(A, i)
        else:
            Push_Up_Max(A, i)

def Push_Up_Min(A, i):
    while i > 2:
        if A[i] < A[(i-3) // 4]:
            A[i], A[(i-3) // 4] = A[(i-3) // 4], A[i]
            i = (i-3) // 4
        else:
            return


def Push_Up_Max(A, i):
    while i > 2:
        if A[i] > A[(i-3) // 4]:
            A[i], A[(i-3) // 4] = A[(i-3) // 4], A[i]
            i = (i-3) // 4
        else:
            return

def Insert(A, k):
    A.append(k)
    Push_Up(A, len(A)-1)

print(len(A))
print(Floyd_Build_Heap(A))
Insert(A, 2)
print(A)

def GetMedian(A):
    if A[1] > A[2]:
        return (A[0] + A[1]) // 2
    else:
        return (A[0] + A[2])  // 2

def GetMax(A):
    return maxs(A[1], A[2])


def GetMin(A):
    return A[0]

print(GetMedian(A), GetMax(A), GetMin(A))