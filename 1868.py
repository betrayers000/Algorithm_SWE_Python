import sys

sys.stdin = open('input.txt', 'r')

dx = [0, 0, 1, -1, -1, -1, 1, 1]
dy = [1, -1, 0, 0, -1, 1, -1, 1]

def f(i, j):
    global N
    for k in range(8):
        ni, nj = i + dx[k], j +dy[k]
        if 0 <= ni < N and 0 <= nj < N and board[ni][nj] == ".":
            # counter[i][j] += 1
            counter[ni][nj] += 1

def bfs(i, j):
    global N, cnt
    # q = [0] * (N*N)
    # front, rear = -1, -1
    # rear += 1
    # q[rear] = (i, j)
    q = []
    q.append((i, j))
    # front = -1
    while q:
        # front += 1
        # x, y = q[front]
        x, y = q.pop(0)
        for k in range(8):
            nx, ny = x + dx[k], y + dy[k]
            if 0<= nx < N and 0<= ny < N and counter[nx][ny] != -1:
                cnt += 1
                if counter[nx][ny] == 0:
                    # rear += 1
                    # q[rear] = (nx, ny)
                    q.append((nx, ny))
                counter[nx][ny] = -1

T = int(input())
for t in range(1, T+1):
    N = int(input())
    board = [list(input()) for _ in range(N)]

    # 바닥 표시 숫자를 구한다
    counter = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if board[i][j] == "*":
                counter[i][j] = -1
                f(i, j)
            # else:
            #     counter[i][j] = -1
    total = 0
    cnt = 0
    for i in range(N):
        for j in range(N):
            if counter[i][j] != -1:
                total += 1
    # print(counter)
    for i in range(N):
        for j in range(N):
            if counter[i][j] == 0:
                counter[i][j] = -1
                bfs(i, j)
    # print(total, cnt)
    print(f"#{t} {total - cnt}")