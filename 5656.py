import sys

sys.stdin = open('input.txt', 'r')

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def copy_board():
    global H, W
    temp = []
    for i in range(H):
        temp.append(board[i].copy())
    return temp

def get_count(temp):
    global H, W
    ans = 0
    for i in range(H):
        for j in range(W):
            if temp[i][j] != 0:
                ans += 1
    return ans


def f(n, k, m, z, s):
    global minV
    if n == m:
        temp = copy_board()
        for i in range(m):
            crash(s[i], temp)
            drop_table(temp)
        # print(s)
        # for i in range(H):
        #     print(temp[i])
        # print()
        res = get_count(temp)
        if res < minV:
            minV = res
        if res == 0:
            return 1
        return
    else:
        for i in range(k):
            if f(n + 1, k, m, i, s + [i]) == 1:
                return 1

def crash(y, temp_board):
    global H
    for i in range(H):
        if temp_board[i][y] > 1:
            # print(temp_board[i][y])
            n = temp_board[i][y]
            for k in range(3):
                # print(k)
                delete(i, y, k,n, temp_board)
            return
        elif temp_board[i][y] == 1:
            temp_board[i][y] = 0
            return

def delete(x, y, d, n, temp_board):
    global H, W
    temp_board[x][y] = 0
    if n == 1:
        return
    nx, ny = x + dx[d], y + dy[d]
    if 0 <= nx < H and 0 <= ny < W:
        if temp_board[nx][ny] > 1:
            a = temp_board[nx][ny]
            for k in range(4):
                if k != d:
                    delete(nx, ny, k, a, temp_board)
                else:
                    if a >= n:
                        delete(nx, ny, k, a, temp_board)
                    else:
                        delete(nx, ny, d, n - 1, temp_board)
        else:
            delete(nx, ny, d, n-1, temp_board)

def drop_table(temp):
    global H, W
    for i in range(H-1, -1, -1):
        for j in range(W):
            if temp[i][j] == 0:
                p = i
                while p > 0:
                    p -=1
                    if temp[p][j] != 0:
                        temp[i][j] = temp[p][j]
                        temp[p][j] = 0
                        break
    return temp

T = int(input())
for t in range(1, T+1):
    N, W, H = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(H)]
    used = [0] * W
    minV = 999999999
    f(0, W, N, 0, [])
    print(minV)