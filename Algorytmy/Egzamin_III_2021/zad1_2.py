# Łukasz Chmielewski
A = [10, 5, 1, 0, 5, 5, 6, 8, 9, 2, 3, 4]
B = [1, 10, 5]

from zad1testy import runtests

def Merge(A, ascending):
    size = len(A)
    if size > 1 and ascending == False:
        mid = int(size/2)
        result = []

        left_array = Merge(A[:mid], ascending)
        right_array = Merge(A[mid:], ascending)
        right_array_ascending = Merge(A[mid:], True)
        p, q = 0, 0
        if len(right_array > len(right_array_ascending)):
            while p < len(left_array) and q < len(right_array):
                if ascending == False:        # jesli jestesmy w lewej czesci tablicy
                    if left_array[p] <= right_array[q]:
                        result.append(right_array[q])
                        p += 1
                        q += 1
                    else:
                        result.append(left_array[p])
                        p += 1

                else:  # jesli jestesmy w prawej czesci tablicy
                    if left_array[p] >= right_array[q]:
                        result.append(right_array[q])
                        p += 1
                        q += 1
                    else:
                        result.append(left_array[p])
                        p += 1

            while p < len(left_array):
                result.append(left_array[p])
                p += 1

            while q < len(right_array):
                result.append(right_array[q])
                q += 1
        else:
            while p < len(left_array) and q < len(right_array_ascending):
                if ascending == False:  # jesli jestesmy w lewej czesci tablicy
                    if left_array[p] >= right_array_ascending[q]:
                        result.append(right_array_ascending[q])
                        p += 1
                        q += 1
                    else:
                        result.append(left_array[p])
                        p += 1

                else:  # jesli jestesmy w prawej czesci tablicy
                    if left_array[p] <= right_array[q]:
                        result.append(right_array[q])
                        p += 1
                        q += 1
                    else:
                        result.append(left_array[p])
                        p += 1

            while p < len(left_array):
                result.append(left_array[p])
                p += 1

            while q < len(right_array):
                result.append(right_array[q])
                q += 1

        return result
    if size > 1:
        mid = int(size/2)
        result = []

        left_array = Merge(A[:mid], ascending)
        right_array = Merge(A[mid:], ascending)
        p, q = 0, 0

        while p < len(left_array) and q < len(right_array):
            if ascending == False:        # jesli jestesmy w lewej czesci tablicy
                if left_array[p] <= right_array[q]:
                    result.append(right_array[q])
                    p += 1
                    q += 1
                else:
                    result.append(left_array[p])
                    p += 1

            else:  # jesli jestesmy w prawej czesci tablicy
                if left_array[p] >= right_array[q]:
                    result.append(right_array[q])
                    p += 1
                    q += 1
                else:
                    result.append(left_array[p])
                    p += 1

        while p < len(left_array):
            result.append(left_array[p])
            p += 1

        while q < len(right_array):
            result.append(right_array[q])
            q += 1

        return result
    return A


def mr(X):
    size = len(X)
    mid = int(size/2)

    left_array = Merge(X[:mid], False)   # lewa polowa ma byc malajaca
    right_array = Merge(X[mid:], True)    # prawa polowa ma byc rosnaca
    ascending_array = Merge(X, True)
    descending_array = Merge(X, False)

    result = left_array + right_array

    if len(ascending_array) > len(descending_array):
        return ascending_array if len(ascending_array) > len(result) else result
    else:
        return descending_array if len(descending_array) > len(result) else result


print(mr(A))
#runtests(mr)