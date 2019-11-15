import sys

sys.stdin = open('input.txt', 'r')

con = [[0, 2, 0, 0], [6, 0, 2, 0], [0, 6, 0, 2], [0, 0, 6, 0]]


def cycle(n, d):
    temp = []
    base = magnet[n]
    if d == 1:
        temp.append(base[-1])
        for i in range(len(base) - 1):
            temp.append(base[i])
    elif d == -1:
        for i in range(1, len(base)):
            temp.append(base[i])
        temp.append(base[0])
    return temp


def get_r(d):
    if d == -1:
        return 1
    return -1


def check(n, d):
    for i in range(len(con[n])):
        z = con[n][i]
        if z != 0:
            k = con[i][n]
            if magnet[n][z] != magnet[i][k] and move[i] == 0:
                move[i] = 1
                check(i, get_r(d))
    magnet[n] = cycle(n, d)


T = int(input())
for t in range(1, T + 1):
    N = int(input())
    magnet = [list(map(int, input().split())) for _ in range(4)]
    for _ in range(N):
        n, d = map(int, input().split())
        move = [0] * 5
        move[n - 1] = 1
        check(n - 1, d)

    res = (magnet[0][0] * 1) + (magnet[1][0] * 2) + (magnet[2][0] * 4) + (magnet[3][0] * 8)
    print(f"#{t} {res}")
