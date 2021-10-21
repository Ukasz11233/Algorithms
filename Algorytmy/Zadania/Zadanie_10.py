A = [-1, -1, 0, 0, 1, 1, 1]

def FindDistinct(A, n):
    number_of_distinct, l, r = n, 0, n-1
    while l < r:
        while l < r and A[l] == A[l+1]:
            number_of_distinct -= 1
            l += 1

        while r > l and A[r] == A[r-1]:
            number_of_distinct -= 1
            r -= 1
        sum = A[l] + A[r]
        if l == r:
            break

        if sum == 0:
            number_of_distinct -= 1
            r -= 1
            l += 1
        elif sum > 0:
            r -= 1
        else:
            l +=1
    return number_of_distinct

print(FindDistinct(A, len(A)))
