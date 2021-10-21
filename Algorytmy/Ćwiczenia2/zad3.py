A = [1, 2, 2, 4, 5, 2, 2, 2]

def FindLeader(A):
    count = 0
    for i in range(len(A)):
        if count == 0:
            leader = i
        if A[leader] == A[i]:
            count += 1
        else:
            count -= 1
    counter = 0
    for el in A:
        if el == A[leader]:
            counter += 1
    if counter > len(A)//2:
        return A[leader]
    return None
print(FindLeader(A))