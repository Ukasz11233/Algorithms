B = [[(5, 3), (7, 0)], [(1, 3), (3, 0)], [(0, 6), (3, 4)], [(4, 8), (5, 5)], [(2, 9), (3, 7)], [(0, 13), (3, 10)], [(5, 17), (6, 14)], [(0, 18), (2, 15)]]
A = [[0 for _ in range(3)] for i in range(16)]
j = 0
for i in range(0, len(A), 2):
    A[i][0] = B[j][0][1]
    A[i][1] = B[j][1][0] - B[j][0][0]
    A[i+1][0] = B[j][1][1]
    A[i][2] = True
    A[i+1][2] = False
    j+=1

print(A)

def Mergesort(A):
    size = len(A)
    if size > 1:
        mid = size//2
        left_arr = A[:mid]
        right_arr = A[mid:]

        Mergesort(left_arr)
        Mergesort(right_arr)

        p, q, r = 0, 0, 0

        left_size = len(left_arr)
        right_size = len(right_arr)
        while p < left_size and q < right_size:
            if left_arr[p][0] < right_arr[q][0]:
                A[r] = left_arr[p]
                p+=1
            else:
                A[r] = right_arr[q]
                q+=1
            r+=1

        while p < left_size:
            A[r] = left_arr[p]
            p+=1
            r+=1

        while q < right_size:
            A[r] = right_arr[q]
            q+=1
            r+=1

def FulfillBuckets(A, l):
    Mergesort(A)
    print(A)
    fulfilled = 0
            return fulfilled

    return len(A)

print(FulfillBuckets(A, 7))

#jebać, nie czaje tresci i algorytmu