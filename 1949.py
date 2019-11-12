import sys

sys.stdin = open('input.txt', 'r')

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def f(i, j, d):
    global N, K, dig, maxV
    for k in range(4):
        ni, nj = i + dx[k], j+dy[k]
        if 0<=ni < N and 0 <= nj < N and visited[ni][nj] == 0:
            if board[i][j] > board[ni][nj]:
                visited[ni][nj] = 1
                f(ni, nj, d+1)
                visited[ni][nj] = 0
            else:
                if dig and board[ni][nj]-K < board[i][j]:
                    ori = board[ni][nj]
                    visited[ni][nj] = 1
                    board[ni][nj] = board[i][j] - 1
                    dig = False
                    f(ni, nj, d+1)
                    dig = True
                    visited[ni][nj] = 0
                    board[ni][nj] = ori
    if maxV < d:
        maxV = d

T = int(input())
for t in range(1, T+1):
    N, K = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0] * N for _ in range(N)]
    start = []
    dig = True
    maxV = 0
    high = 0
    for i in range(N):
        for j in range(N):
            if board[i][j] > high:
                high = board[i][j]
    for i in range(N):
        for j in range(N):
            if board[i][j] == high:
                start.append((i, j))
    for s in start:
        visited[s[0]][s[1]] = 1
        f(s[0], s[1], 1)
        visited[s[0]][s[1]] = 0
    print(f"#{t} {maxV}")