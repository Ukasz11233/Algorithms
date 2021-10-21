S = [[1, 4], [3, 5], [0, 6], [5, 7], [3, 9], [5, 9], [6, 10], [8, 11], [8, 12], [2, 14], [12, 16]]
F = [[1, 4], [2, 5], [4, 5], [5, 6]]


def Top_down_activity_selector(S):
    L = [[-float("inf") for i in range(6)]for i in range(6)]
    return Top_down(S, L, 0, 0)

def Aux_top_down_activity_selector(S, L, idx, finish):
    if idx == len(S):
        return 0, L
    if L[idx][finish] > -1:
        return L[idx][finish], L
    v1, v2 = 0, 0

    v1 = Aux_top_down_activity_selector(S, L, idx+1, finish)[0] #nie wybieram danej aktywnosci
    if S[idx][0] >= finish:
        v2 = Aux_top_down_activity_selector(S, L, idx+1, S[idx][1])[0] + 1 #wybieram aktywnosc
    L[idx][finish] = max(v1, v2)
    return L[idx][finish], L

print(Top_down_activity_selector(F))