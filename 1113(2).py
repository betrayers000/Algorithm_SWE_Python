import sys

sys.stdin = open('input.txt', 'r')

def get_exp(K):
    # n = K*2-1
    # div = n//2
    # si, sj = i-div, j-div
    # price = 0
    # for i in range(n):
    #     if i <= div:
    #         for j in range(div-i, div+i+1):
    #             ni, nj = si + i, sj +j
    #             price += 1
    #     else:
    #         for j in range(i-div, div+n-i):
    #             ni, nj = si + i, sj +j
    #             price += 1
    # print(price)
    return K * K + (K - 1) * (K - 1)

maxK = 11

def get_dis(a, b):
    sx, sy = a
    ex, ey = b
    return abs(sx-ex) + abs(sy - ey)

def f(h):
    global M, maxV
    for i in range(get_dis(h, (N-1, N-1))+1):
        temp = 0
        exp = get_exp(i + 1)
        for j in range(len(home)):
            dis = get_dis(h, home[j])
            if dis <= i:
                temp += 1
        res = temp * M - exp
        # if h == (3, 3):
        #     print(exp, temp * M, i)
        if res >= 0:
            if maxV < temp:
                maxV = temp


T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0] * N for _ in range(N)]
    home = []
    maxV = 0
    for i in range(N):
        for j in range(N):
            if board[i][j] == 1:
                home.append((i, j))
    for i in range(N):
        for j in range(N):
            f((i, j))
    print(f"#{t} {maxV}")

