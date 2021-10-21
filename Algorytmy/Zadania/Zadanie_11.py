A = [-1, -1, -1, 0, 0, 1, 1, 1]

def findDistinct(A, n):
    max_size = 1
    result = 0
    for el in A:
        if el < 0:
            tmp = el*(-1)
        else:
            tmp = el
        if tmp > max_size:
            max_size = tmp

    Distinct = [0 for _ in range(max_size+1)]

    for el in A:
        if el < 0:
            idx = el*(-1)
        else:
            idx = el
        Distinct[idx] += 1
    for x in Distinct:
        if x > 0:
            result +=1
    return result

print(findDistinct(A, len(A)))  # czas dzialania funkcji to O(n)
