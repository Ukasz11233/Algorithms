#Łukasz Chmielewski
#pomysl polega na zmodyfikowaniu mergesorta tak, aby lewa czesc tablicy do pewnego elementu byla malejaca, a reszta tablicy rosnaca lub aby cala tablica byla rosnaca lub malejaca
#zlozonosc to O(nlogn)

A = [10, 5, 1, 0, 5, 5, 6, 8, 9, 2, 3, 4]
B = [1, 10, 5]

from zad1testy import runtests

def Merge(A, ascending):
    size = len(A)
    if size > 1:
        mid = int(size/2)
        result = []

        left_array_ascending = Merge(A[:mid], True)
        left_array_descending = Merge(A[:mid], False)
        if len(left_array_ascending) > len(left_array_descending):
            left_array = left_array_ascending
            left = True
        else:
            left_array = left_array_descending
            left = False
        right_array_ascending = Merge(A[mid:], True)
        right_array_descending = Merge(A[mid:], False)
        if len(right_array_ascending) > len(right_array_descending):
            right_array = right_array_ascending
            right = True
        else:
            right_array = right_array_descending
            right = False

        if ascending == False:
            ascending_array = Merge(A[mid:], True)
            if len(ascending_array) > len(right_array):
                right_array = ascending_array
                right = True

        p, q = 0, 0

        while p < len(left_array) and q < len(right_array):
            if left == right:        # jesli jestesmy w lewej czesci tablicy
                if left == False:
                    if left_array[p] <= right_array[q]:
                        result.append(right_array[q])
                        left_array = left_array[:p]
                        q += 1
                    else:
                        result.append(left_array[p])
                        p += 1

                else:                                   # jesli jestesmy w prawej czesci tablicy
                    if left_array[p] >= right_array[q]:
                        result.append(right_array[q])
                        left_array = left_array[:p]
                        q += 1
                    else:
                        result.append(left_array[p])
                        p += 1
            else:
                if left == False and right == True:
                    if left_array[p] > right_array[q]:
                        result.append(left_array[p])
                        p += 1
                    else:
                        q = float("inf")


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

    left_array = Merge(X[:mid], False)   # lewa polowa ma byc malajaca do pewnego miejsca
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
