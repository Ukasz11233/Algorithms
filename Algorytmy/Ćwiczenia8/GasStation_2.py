S = [0, 1, 5, 7, 11, 15, 20]
P = [4, 2, 5, 7, 3, 1, 9]

S1 = [0, 1, 5, 7, 11]
P1 = [3, 2, 4, 3, 9]

S2 = [0, 1, 9, 15, 16, 17, 27, 30]
P2= [3, 1, 10, 10, 5, 1, 39, 4]


def FindCheapest_withoutCurrent(S, P, actual_postion, d):
    n = len(P)
    min_price = float("inf")
    cheapest_postion = None
    for i in range(actual_postion+1, n):
        if S[i] - S[actual_postion] <= d:
            if P[i] < min_price or i == n-1:
                min_price = P[i]
                cheapest_postion = i

    return cheapest_postion


def FindCheapest(S, P, acutal_position, d):
    n = len(S)
    min_price = P[acutal_position]
    cheapest_position = acutal_position

    for i in range(acutal_position, n):
        if S[i] - S[acutal_position] <= d:
            if P[i] < min_price or i == n-1:
                min_price = P[i]
                cheapest_position = i
        else:
            break
    return cheapest_position


def GasStation(S, P, d):
    n = len(P)
    actual_position = 0
    actual_fuel = d
    cost = 0
    while actual_position < n-1:
        cheapest_station = FindCheapest(S, P, actual_position, d)
        print(actual_fuel, actual_position, cost)
        if cheapest_station == actual_position:
            cost += (d - actual_fuel)*P[actual_position]
            actual_fuel = d
            tmp = actual_position
            actual_position = FindCheapest_withoutCurrent(S, P, actual_position, d)
            actual_fuel -= (S[actual_position] - S[tmp])
        else:
            if actual_fuel < S[cheapest_station] - S[actual_position]:
                cost += ((S[cheapest_station] - S[actual_position]) - actual_fuel)*P[actual_position]
                actual_fuel = 0
            else:
                actual_fuel -= S[cheapest_station] - S[actual_position]
            actual_position = cheapest_station
    return cost

print(GasStation(S2, P2, 10))