from queue import PriorityQueue

L = ["XXXXXXXXXX",
     "X X      X",
     "X XXXXXX X",
     "X        X",
     "XXXXXXXXXX",
     ]


def robot(L, A, B):
    y = len(L)
    x = len(L[0])
    visited = [[[False for _ in range(12)]
                for _ in range(y)]
                for _ in range(x)]

    Q = PriorityQueue()
    speed = [60, 40, 30]

    Q.put((0, (A[0], A[1], 0)))


    while not Q.empty():
        result, (x, y, step) = Q.get()
        if visited[x][y][step] == True:
            continue
        else:
            visited[x][y][step] = True

        if L[y][x] == "X":
            continue
        if (x, y) == B:
            return result

        Q.put((result + 45, (x, y, (step + 3) % 4)))   # obrot w lewo
        Q.put((result + 45, (x, y, (step + 1) % 4)))   # obrot w prawo
        if step % 2 == 0:
            if step % 4 == 0:
                if step > 7:
                    Q.put((result + speed[step//4], (x + 1, y, step)))
                else:
                    Q.put((result + speed[step//4], (x + 1, y, (step + 4) % 12)))

            else:
                if step > 7:
                    Q.put((result + speed[step//4], (x - 1, y, step)))
                else:
                    Q.put((result + speed[step // 4], (x - 1, y, (step + 4) % 12)))
        else:
            if (step - 1) % 4 == 0:
                if step > 7:
                    Q.put((result + speed[step//4], (x, y + 1, step)))
                else:
                    Q.put((result + speed[step//4], (x, y + 1, (step + 4) % 12)))
            else:
                if step > 7:
                    Q.put((result + speed[step//4], (x, y - 1, step)))
                else:
                    Q.put((result + speed[step//4], (x, y - 1, (step + 4) % 12)))



    return None
from zad2testy import runtests
#print(robot(L, (1, 1), (8, 3)))
runtests(robot)