import sys

sys.stdin = open('input.txt', 'r')

def f(n, k, m, z, a, b):
    global N, minV
    if n == m:
        res = abs(cooking(list(a)) - cooking(list(b)))
        if minV > res:
            minV = res
        return
    else:
        for i in range(z, k):
            if used[i] == 0:
                used[i] = 1
                f(n+1, k, m, i, a - {i}, b | {i})
                used[i] = 0

def cooking(temp):
    total = 0
    for i in range(len(temp)):
        for j in range(i+1, len(temp)):
            total += table[temp[i]][temp[j]] + table[temp[j]][temp[i]]
    return total

T = int(input())
for t in range(1, T+1):
    N = int(input())
    table = [list(map(int, input().split())) for _ in range(N)]
    ing = set(range(N))
    used = [0] * N
    cycle = 0
    minV = 999999999
    f(0, N, N//2, 0, ing, set())
    print(f"#{t} {minV}")
