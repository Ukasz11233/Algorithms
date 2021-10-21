E = [[1, 4], [0, 4, 2, 5], [1, 3, 4, 5], [2, 5], [0, 1, 2, 5], [4, 1, 2, 3]]
M = [[0, 1, 0, 0, 1, 0], [1, 0, 1, 0, 1, 1], [0, 1, 0, 1, 1, 1], [0, 0, 1, 0, 0, 1], [1, 1, 1, 0, 0, 1], [0, 1, 1, 1, 1, 0]]

NoEuler = [[0, 1, 1, 1], [1, 0, 1, 0], [1, 1, 0, 1], [1, 0, 1, 0]]

G = [[0,1,1,0,0,0],
[1,0,1,1,0,1],
[1,1,0,0,1,1],
[0,1,0,0,0,1],
[0,0,1,0,0,1],
[0,1,1,1,1,0]]


def euler(G):
    n = len(G)
    C = []  # sciezka cyklu eulera
    M = [[0] * (n + 1) for _ in range(n)]  # skopiowanie macierzy G, z dodatkowa kolumna,
                        # w ktorej bedzie przetrzymywana ilosc krawedzi wychodzacych z danego wierzcholka
    for i in range(n):
        counter = 0
        for j in range(n):
            if G[i][j] == 1:
                counter += 1
            M[i][j] = G[i][j]
        M[i][n] = counter  # stopien wierzcholka

    def DFSVisit(M, u):
        if M[u][n] > 0:  # jesli pozostaly krawedzi wychodzace z wierzcholka, to wtedy je sprawdzamy
            print(u, M[u])
            for i in range(n):
                if M[u][i] == 1:
                    M[u][i] = 0  # usuwamy krawedz (u, i)
                    M[i][u] = 0
                    M[i][n] -= 1  # zmniejszam ilosc krawedzi wychodzacych z wierzcholkow u oraz i
                    M[u][n] -= 1
                    DFSVisit(M, i)  # wywoluje rekurenyjnie DFSVisit dla kolejnego wierzholka
                    C.append(i)  # po przetworzeniu wierzholka, czyli gdy nie zostalo mu wiecej krawedzi, dodaje go do sciezki eulera
        return M

    for i in range(n):
        M = DFSVisit(M, i)

    return C if C[0] == 0 else None  # w mojej funkcji sciezka eulera zawsze zaczyna sie od wierzcholka "0", wiec musi tez sie na nim konczyc


print(euler(G))