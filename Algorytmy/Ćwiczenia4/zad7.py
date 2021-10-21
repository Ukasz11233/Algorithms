A = [0, 1, 3, 1, 0, 0, 2, 1, 3, 1, 0, 2]

def FindAllColours(A, k):
    n = len(A)
    il = i = j = 0
    min_length = 0, float("inf")
    colours = [0 for _ in range(k)]
    while j < n:
        if il < k:
            colours[A[j]] += 1
            if colours[A[j]] == 1:
                il += 1
            j+=1
        else:
            colours[A[i]] -= 1
            if colours[A[i]] == 0:
                il -= 1
                mem = i, j-1
                print(mem)
                if min_length[1] - min_length[0] > mem[1] - mem[0]:
                    min_length = mem
            i+=1
    return min_length

print(FindAllColours(A, 4))