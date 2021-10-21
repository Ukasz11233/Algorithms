A = [6, 0, 2, 0, 1, 3, 4, 6, 1, 3, 2]  # len(A) = 11


def CountingSort(A):
    output = [0]*len(A)
    counting = [0]*(max(A)+1)
    for i in range(len(A)):
        counting[A[i]] += 1
    for i in range(1, max(A)+1):
        counting[i] = counting[i] + counting[i-1]
    print(counting)
    for j in range(len(A)-1, -1, -1):
        print(output)
        output[counting[A[j]]-1] = A[j]
        counting[A[j]] -= 1
    return output

print(CountingSort(A))