import sys

sys.stdin = open('input.txt', 'r')

pipe = [
    [],
    [(0, 1), (0, -1), (1, 0), (-1, 0)],
    [0, 0, (1, 0), (-1, 0)],
    [(0, 1), (0, -1), 0, 0],
    [(0, 1), 0, 0, (-1, 0)],
    [(0, 1), 0, (1, 0), 0],
    [0, (0, -1), (1, 0), 0],
    [0, (0, -1), 0, (-1, 0)],
]
connect = [[1, 3, 6, 7], [1, 3, 4, 5], [1, 2, 4, 7], [1, 2, 5, 6]]


def bfs(i, j):
    global N, M, L
    q = []
    q.append((i, j))
    visited[i][j] = 1
    res = 0
    while q:
        x, y = q.pop(0)
        if visited[x][y] > L:
            return res
        res += 1
        # print(board[x][y], pipe[board[x][y]], visited[x][y])
        temp = pipe[board[x][y]]
        for k in range(4):
            if temp[k] != 0:
                a, b = temp[k]
                nx, ny = x + a, y + b
                if 0 <= nx < N and 0 <= ny < M and board[nx][ny] != 0:
                    if visited[nx][ny] == 0 and board[nx][ny] in connect[k]:
                        visited[nx][ny] = visited[x][y] + 1
                        q.append((nx, ny))
    return res


T = int(input())
for t in range(1, T+1):
    N, M, R, C, L = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0] * M for _ in range(N)]
    print(f"#{t} {bfs(R, C)}")
    # for i in range(N):
    #     print(visited[i])
