A = [1, 0, 0, 1, 1, 2, 1, 2]

def longest_incomplete(A, k):  # rozwiazanie  k nalezacych od [0, k-1]. Dla dowolnych k potrzebny bylby slownik
    if len(A) == 1:
        return 1
    counter = [0 for _ in range(k)]
    result_mem = float("inf"), 0
    mem = 0, 0
    n = len(A)
    i = j = il = 0
    while i <= j and j < n:
        if il < k:
            print(i, j)
            counter[A[j]] += 1
            if counter[A[j]] == 1:
                il += 1
            j += 1
        else:
            counter[A[i]] -=1
            if counter[A[i]] == 0:
                il -= 1
                mem = (i, j-1)
            if result_mem[1] - result_mem[0] < mem[1] - mem[0]:
                result_mem = mem
            i += 1

    mem = (i, j-1)
    if result_mem[1] - result_mem[0] < mem[1] - mem[0]:
        result_mem = mem

    return result_mem

print(longest_incomplete(A, 3))




A = [1,100, 5, 100, 1, 5, 1, 5]


def longest_incomplete(A ,k):     # dziala dla dowolnego k i ma ok zlozonosc bo k << n
    n = len(A)
    F = [[float("inf")] for _ in range(k+1)]
    idx = 0
    for i in range(n):
        flag = False
        for j in range(k):
            if A[i] == F[j][0]:
                flag = True
        if flag == False:
            F[idx][0] = A[i]
            F[idx].append(0)
            idx += 1
    F[k] = 0

    result = 0
    l, r = 0, 0
    while l < n and r < n:
        tmp_result = 0
        el = A[r]
        for i in range(k):
            if F[i][0] == el:
                if F[i][1] == 0:
                    F[k] += 1
                F[i][1] += 1

        if F[k] == k:
            while l < r or F[k] == k:
                tmp = A[l]
                for i in range(k):
                    if F[i][0] == tmp:
                        F[i][1] -= 1
                        if F[i][1] == 0:
                            F[k] -=1
                l += 1

        for i in range(k):
            tmp_result += F[i][1]

        if result < tmp_result:
            result = tmp_result

        r += 1

    return F, result
print(longest_incomplete(A, 3))