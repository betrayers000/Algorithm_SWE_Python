import sys

sys.stdin = open('input.txt', 'r')


def f(x, y):
    temp = [(x, y)]
    for dx,dy in [(1, 0), (1, 1), (0, 1)]:
        nx, ny = x + dx, y + dy
        if 0<= nx < M and 0 <= ny < N:
            if board[nx][ny] == 1:
                temp.append((nx, ny))
            else:
                return
    for point in temp:
        i, j = point
        visit[i][j] = 1

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]
    # print(board)
    visit = [[0] * M for _ in range(N)]
    for i in range(N):
        for j in range(M):
            if board[i][j] == 1:
                f(i, j)
    check = 0
    # print(visit, board)
    for i in range(N):
        if board[i] != visit[i]:
            print("NO")
            check = 1
            break
    if not check:
        print("YES")