A = [1, 1, 1]
B = [1, 1, 1]
C = [0, 0, 0, 0]

def binary_sum(A, B):
    j=0
    for i in range(0, len(A)):
        if(A[i]+B[i]) == 2:
            C[j] = 1
            C[j+1] = 0
            j+=1
        elif(A[i]+B[i]) == 1:
            C[j+1] = 1
            j+=1
        else:
            j+=1
    return C
print(binary_sum(A, B))

