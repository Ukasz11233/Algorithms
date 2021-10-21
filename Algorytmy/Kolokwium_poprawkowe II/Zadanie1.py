P = [(2, 2), (1, 1), (2.5, 0.5), (3, 2), (0.5, 3)]


def Mergesort(A):
    size = len(A)
    if size > 1:
        mid = int(size/2)

        result = []

        left_array = Mergesort(A[:mid])
        right_array = Mergesort(A[mid:])
        p, q = 0, 0

        while p < len(left_array) and q < len(right_array):
            if left_array[p][1] < right_array[q][1]:
                result.append(left_array[p])
                p+=1
            elif left_array[p][1] == right_array[q][1]:
                if left_array[p][0] < right_array[q][0]:
                    result.append(left_array[p])
                    p+=1
                else:
                    result.append(right_array[q])
                    q+=1
            else:
                result.append(right_array[q])
                q+=1

        while p < len(left_array):
            result.append(left_array[p])
            p+=1

        while q < len(right_array):
            result.append(right_array[q])
            q+=1

        return result
    return A


def dominance_utility(P):
    size = len(P)
    if size > 1:
        mid = size//2
        left_array = dominance_utility(P[:mid])
        right_array = dominance_utility(P[mid:])
        result = []
        p, q = 0, 0

        while p < len(left_array) and q < len(right_array):
            if left_array[p][0] <= right_array[q][0]:
                result.append(left_array[p])
                right_array = right_array[:q]
                p += 1
            else:
                result.append(right_array[q])
                q += 1
        while p < len(left_array):
            result.append(left_array[p])
            p += 1

        while q < len(right_array):
            result.append(right_array[q])
            q += 1

        return result
    return P

def dominance(P):
    output = [[0 for _ in range(3)] for _ in range(len(P))]
    for i in range(len(P)):
        output[i][0], output[i][1], output[i][2] = P[i][0], P[i][1], i
    output = Mergesort(output)
    output = dominance_utility(output)
    S = [0]*len(output)
    for i in range(len(S)):
        S[i] = output[i][2]
    return S

print(dominance(P))