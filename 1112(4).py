import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    table = []
    inp = list(map(int, input().split()))
    N = inp[0]
    temp = []
    for i in range(1, len(inp)):
        n = inp[i]
        if n == 0:
            n = 1001
        temp.append(n)
        if i % N == 0:
            table.append(temp)
            temp = []
    minV = 1001*N
    for i in range(N):
        for j in range(N):
            if i != j:
                for k in range(N):
                    if j != k:
                        table[i][j] = min(table[i][j], table[i][k] + table[k][j])
        temp = sum(table[i]) -1001
        if minV > temp:
            minV = temp
    print(f"#{tc} {minV}")
