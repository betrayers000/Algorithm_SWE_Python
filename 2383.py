import sys

sys.stdin = open('input.txt', 'r')

def get_dis(h, s):
    hx, hy = h
    sx, sy = s
    return abs(hx-sx) + abs(hy-sy) + 1

def f(n, k, m, z, s, r):
    if n == m:
        moving(list(s), list(r))
        return
    else:
        for i in range(z, k):
            if used[i] == 0:
                used[i] = 1
                f(n+1, k, m, i, s | {i}, r -{i})
                used[i] = 0

def find(temp, k):
    temp.sort()
    sx, sy = stair[k]
    d = board[sx][sy]
    s = []
    if temp == []:
        return 0
    for i in range(len(temp)):
        n = temp[i]
        if i > 2:
            t = s.pop(0)
            if n <= t:
                n = t
            s.append(n + d)
        else:
            n = n + d
            s.append(n)
        # print(temp, s, d)
    # print(temp, s, d)
    return s[-1]

def moving(l, r):
    global maxV
    # print(l, r)
    left = []
    right = []
    for i in range(len(l)):
        left.append(get_dis(human[l[i]], stair[0]))
    for i in range(len(r)):
        right.append(get_dis(human[r[i]], stair[1]))
    # print(left, right)
    res = max(find(left, 0), find(right, 1))
    # print(f"res{res}")
    if maxV > res:
        maxV = res

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]
    human = []
    stair = []
    for i in range(N):
        for j in range(N):
            if board[i][j] == 1:
                human.append((i, j))
            elif 1 < board[i][j] < 11:
                stair.append((i, j))
    used = [0] * len(human)
    ori = set(range(len(human)))
    maxV = 99999999
    for i in range(len(human)+1):
        f(0, len(human), i, 0, set(), ori)
    print(f"#{tc} {maxV}")