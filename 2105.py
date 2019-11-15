import sys

sys.stdin = open('input.txt', 'r')

dx = [1, 1, -1, -1]
dy = [-1, 1, 1, -1]
di = [[0, 1], [1, 2], [2, 3], [3, 0]]


def dfs(x, y, d, s, t):
    global N, startI, startJ, maxV
    # print(x, y, startI, startJ, s, board[x][y], t)
    if t < 0:
        return
    if x == startI and y == startJ:
        nx, ny = x + 1, y-1
        if y - 1 >= 0 and x + 1 < N and used[board[nx][ny]] == 0:
            used[board[nx][ny]] = 1
            visited[nx][ny] = 1
            dfs(nx, ny, 0, s + 1, t)
            used[board[nx][ny]] = 0
            visited[nx][ny] = 0
    else:
        for k in range(len(di[d])):
            z = di[d][k]
            if t == 0 and z != d:
                continue
            nx, ny = x + dx[z], y + dy[z]
            if 0 <= nx < N and 0 <= ny < N:
                if nx == startI and ny == startJ:
                    # print(f"#{s}")
                    if maxV < s:
                        maxV = s
                    return
                if used[board[nx][ny]] == 0 and visited[nx][ny] == 0:
                    used[board[nx][ny]] = 1
                    visited[nx][ny] = 1
                    if d != z:
                        dfs(nx, ny, z, s + 1, t-1)
                    else:
                        dfs(nx, ny, z, s + 1, t)
                    used[board[nx][ny]] = 0
                    visited[nx][ny] = 0



T = int(input())
for t in range(1, T+1):
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]
    maxV = -1
    for i in range(N - 1):
        for j in range(N - 1):
            visited = [[0] * N for _ in range(N)]
            used = [0] * 101
            visited[i][j] = 1
            used[board[i][j]] = 1
            startI = i
            startJ = j
            dfs(i, j, 0, 1, 3)
    print(f"#{t} {maxV}")
