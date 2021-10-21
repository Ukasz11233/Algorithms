S = [[1, 4, 20], [2, 5, 29], [4, 5, 23], [5, 6, 20]]

def MaxActivitySelect(S):
    L = [[-float("inf") for i in range(6)]for i in range (6)]
    return DPMaxActivitySelect(S, L, 0, 0)


def DPMaxActivitySelect(S, L, k, curr_finish):
    if k == len(S):
        return 0
    if L[k][curr_finish] > -1:
        return L[k][curr_finish]
    v1, v2 = 0, 0
    v1 = DPMaxActivitySelect(S, L, k+1, curr_finish)

    if S[k][0] >= curr_finish:
        v2 = DPMaxActivitySelect(S, L, k+1, S[k][1]) + S[k][2]

    L[k][curr_finish]= max(v1, v2)
    return L[k][curr_finish]

print(MaxActivitySelect(S))
