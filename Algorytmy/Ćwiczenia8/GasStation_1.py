S = [1, 4, 8, 9, 11, 12, 15, 17]

def GasStation(S, L):
    n = len(S)
    stops = 0
    actual_position = 0

    for i in range(1, n):
        if S[i] - S[i-1] > L:
            return False

    for i in range(n):
        if S[i] > actual_position + L and i > 0:
            actual_position = S[i-1]
            stops += 1
            print(actual_position, end=" ")
        if S[i] > actual_position + L and i == 0:
            return None

    return stops


print(GasStation(S, 4))