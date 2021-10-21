A = [[0, 6], [8, 16], [1, 9], [2, 5], [6, 11], [12, 15], [0, 4], [5, 10], [11, 14], [8, 13]]

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

def FindBiggest(A):
    Mergesort(A) # sortowanie przedziałów względem początku O(nlgn)
    print(A)
    count = maxcount = 0
    currA = A[0][0]
    currB = A[0][1]

    for el in A:  #liniowo przechode po elementach i zliczam te ktore zawieraja sie w przedziale
        if currA < el[0] and currB > el[1]:
            count += 1
        elif currB < el[1]:
            currA = el[0]
            currB = el[1]
            count = 0
        if maxcount < count:
            maxcount = count
            maxA = currA
            maxB = currB
    return maxA, maxB

print(FindBiggest(A))