import sys

sys.stdin = open('input.txt', 'r')


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    M = int(input())
    table = [[600] * (N+1) for _ in range(N+1)]
    for _ in range(M):
        s, e = map(int, input().split())
        table[s][e] = 1
    for i in range(1, N+1):
        for j in range(1, N + 1):
            if j != i:
                for k in range(1, N + 1):
                    if k != j:
                        table[i][j] = min(table[i][j] , table[i][k] + table[k][j])
    result = 0
    for i in range(N+1):
        temp = 0
        for j in range(N+1):
            if table[i][j] != 600:
                temp += 1
            if table[j][i] != 600:
                temp += 1
        if temp == N-1:
            result += 1

    # ans = f()
    # print(ans)
    print(f"#{tc} {result}")