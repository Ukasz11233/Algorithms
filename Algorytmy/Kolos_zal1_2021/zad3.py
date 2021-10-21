# Łukasz Chmielewski
# algorytm zachlanny: szukam stacji o jak najwiekszej pojemnosci w naszym zasiegu (ktory poczatkowy wynosi W(0), z ograniczeniem na ilosc paliwa w baku i tankuje w niej zwiekszajac zasieg
# , z tym ze jesli mamy dwie o tak samo lub bardziej pojemne od naszego baku stacje, to wybieramy te ktora jest dalej punktu startowego
# zlozonosc to O(n*q)



from queue import PriorityQueue

from zad3testy import runtests


def SearchStations(T, V, Q, actual_fuel, actual_pos, q):
    n = len(T)

    for i in range(n):
        if T[i] <= actual_fuel:
            Q.put((-V[i], i))



def iamlate(T, V, q, l):
    n = len(T)
    Q = PriorityQueue()

    for i in range(n):
        if T[i] <= V[0]:
            Q.put((-V[i], i))


    result = [0]
    actual_fuel = V[0]
    actual_pos = 0

    while not Q.empty():
        if actual_fuel >= l:
            return result
        el = Q.get()

        actual_pos = el[1]
        result.append(el[1])
        if actual_fuel + T[actual_pos] < q:
            actual_fuel += T[actual_pos]
        else:
            actual_fuel = q

        SearchStations(T, V, Q, actual_fuel, actual_pos, q)

    return result


#runtests( iamlate )