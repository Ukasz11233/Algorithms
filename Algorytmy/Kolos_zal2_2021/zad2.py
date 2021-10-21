from zad2testy import runtests


# Łukasz Chmielewski
# Moim pomysłem jest aby użyc bucket sorta. Wrzucamy nasze liczby do  10^K kubełkow i nastepnie przechodząc miedzy kubelkami staramy sie dojsc do ostatniego elemntu
# jesli jest to nie mozliwe zwracamy None
# Zlozonosc to O(N + M)


A = [100133, 101109, 101139, 102105, 102130, 102134, 103110, 103120, 104120, 105105, 105107, 105109, 105118,
                 105135, 106103, 106140,
                 107110, 107119, 107123, 107138, 107140, 108130, 109107, 109128, 109132, 109139, 110101, 110103, 110104,
                 110128, 112122, 113102,
                 113107, 113119, 113135, 116113, 116133, 117118, 117124, 118105, 118117, 118123, 119102, 119110, 119125,
                 119137, 120113, 120119,
                 120130, 120132, 121120, 121133, 122122, 122133, 122136, 123105, 123127, 123137, 124108, 124138, 125140,
                 127131, 127139, 128117,
                 128129, 129120, 129127, 129133, 130106, 130107, 130119, 131123, 132118, 132124, 133109, 133113, 133135,
                 133137, 133138, 134106,
                 135102, 135107, 135116, 135200, 136105, 137121, 137129, 137135, 138101, 138121, 138139, 139110, 139113,
                 139116, 139129, 140109,
                 140112, 140122, 200000]

C  = [100133, 133138, 138101, 101139, 139129, 129127, 127139, 139113, 113119, 119137, 137129, 129120, 120113,
                 113107, 107110, 110104, 104120,
                 120130, 130119, 119125, 125140, 140109, 109139, 139110, 110101, 101109, 109107, 107119, 119102, 102105,
                 105107, 107140, 140112, 112122,
                 122122, 122133, 133135, 135107, 107123, 123127, 127131, 131123, 123105, 105135, 135102, 102130, 130107,
                 107138, 138121, 121120, 120119,
                 119110, 110103, 103110, 110128, 128129, 129133, 133109, 109132, 132124, 124108, 108130, 130106, 106103,
                 103120, 120132, 132118, 118123,
                 123137, 137121, 121133, 133137, 137135, 135116, 116113, 113102, 102134, 134106, 106140, 140122, 122136,
                 136105, 105109, 109128, 128117,
                 117118, 118105, 105105, 105118, 118117, 117124, 124138, 138139, 139116, 116133, 133113, 113135, 135200,
                 200000]


D = [1213, 1324, 1325, 2465, 2465, 6599, 6524, 9900]

def order(L, K):
    B = []
    n = len(L)
    s = min(L)              # liczba z ktorej startujemy
    t = max(L)              # liczba na ktorej musimy skonczyc

    for i in range(10 ** K):        # tworzymy 10^K kubelkow
        B.append([])
    B[(s // 10 ** K)].append(s)  # na poczatek dodajemy eleemnt z ktorego bedziemy startowac
    B[(t // 10 ** K)].append(t)  # na koniec dodajemy najwieksza liczbe
    for i in range(n):              # uzupelniamy kubelki
        if L[i] == s or L[i] == t:
            continue
        idx_b = (L[i] // 10 ** K)
        B[idx_b].append(L[i])
    #B[(t // 10 ** K)].append(t)  # na koniec dodajemy najwieksza liczbe

    for i in range(10**K):
        if len(B[i]):
            B[i] = sorted(B[i])

    result = [s]
    B[s // 10 ** K][0] = -1         # zmieniam wartosc najmniejszej liczby w kubelku na -1, zeby nie odwiedzic jej dwa razy
    idx = s % 10 ** K               # indeks nastepnego kubleka w ktym bede szukal liczby na ktora moge przejsc

    for i in range(n):             # kolejno n razy przechodzimy miedzy kublekami i uzupelniamy nasza liste pythonowa w takiej kolejnosci
        for j in range(len(B[idx])):
            if B[idx][j] >= 0:          # warunek sprawdzajacy czy element zostal juz odwiedzony

                result.append(B[idx][j])
                tmp = idx
                idx = B[idx][j] % (10**K)   # aktualizuje indeks nastepnego kubelka
                B[tmp][j] = -1              # jesli element zostal juz odwiedzony zmieniamy go na wartosc -1
                break

    return result if result[len(result) - 1] == t else None

print(order(A, 3))
print(C)
#runtests(order)


