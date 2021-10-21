A = [(0,4),(1,10),(6,7), (2,8)]

def kintersect(A, k):
    n = len(A)
    B = sorted(A)
    max_inter = -1
    final_result = []

    for i in range(n-1, -1, -1):
        result = [B[i]]
        counter = 1
        inter = 0
        for j in range(i-1, -1, -1):
            if counter >= k:
                break
            if B[i][0] >= B[j][0]:
                if B[j][1] >= B[i][1]:
                    inter = B[i][1] - B[i][0]
                    result.append(B[j])
                else:
                    if B[j][1] >= B[i][0]:
                        inter = B[j][1] - B[i][0]
                        result.append(B[j])
                    else:
                        continue
                counter += 1

        if counter >= k:
            if max_inter < inter:
                final_result = result
                max_inter = inter

    result = []
    print(max_inter, final_result)
    for el in final_result:
        for i in range(n):
            if A[i] == el:
                result.append(i)
                break

    return result
from zad3testy import runtests
runtests(kintersect)

C = [(10, 11), (9, 12), (8, 13), (7, 14), (6, 15)]

#print(kintersect(C, 3))
#[2, 3, 4], 5, k = 3