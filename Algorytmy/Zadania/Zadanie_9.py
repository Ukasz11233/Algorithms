A = [4, 9, 1, 13, 10, 2, 8]


def SumInversions(A, inv):
    size = len(A)
    if size > 1:
        mid = size//2

        inv, left_array = SumInversions(A[:mid], inv)
        inv, right_array = SumInversions(A[mid:], inv)

        result = []
        p, q, counter = 0, 0, 0

        while p < len(left_array) and q < len(right_array):
            if left_array[p] < right_array[q]:
                result.append(left_array[p])
                p += 1
            else:
                counter += len(left_array) - p
                result.append(right_array[q])
                q += 1

        while p < len(left_array):
            result.append(left_array[p])
            p += 1
        while q < len(right_array):
            result.append(right_array[q])
            q += 1
        return inv + counter, result

    return inv, A

print(SumInversions(A, 0))