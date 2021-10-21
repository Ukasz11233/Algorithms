
A = [12, 5, 3, 1, 2, 6]



def Mergesort(A):
    size = len(A)
    if size > 1:
        mid = int(size/2)

        result = []

        left_array = Mergesort(A[:mid])
        right_array = Mergesort(A[mid:])
        p, q = 0, 0

        while p < len(left_array) and q < len(right_array):
            if left_array[p] < right_array[q]:
                result.append(left_array[p])
                p+=1
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

print(Mergesort(A))

