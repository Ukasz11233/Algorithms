A = [4, 3, 2, 6, 3, 6, 2, 1, 0 ,4]

def CountNumInCompartment(A, a, b):
    counting = [0]*(max(A)+1)
    for i in range(len(A)):
      counting[A[i]] += 1
    print(counting)
    for i in range(1, (max(A) + 1)):
        counting[i] += counting[i-1]
    return counting[b] - counting[a-1]

print(CountNumInCompartment(A, 1, 6))