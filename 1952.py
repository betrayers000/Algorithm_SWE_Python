import sys

sys.stdin = open('input.txt', 'r')


T = int(input())
for tc in range(1, T+1):
    d, m, tm, y = map(int, input().split())
    plan = list(map(int, input().split()))
    dp = [0] * 12
    for i in range(12):
        dp[i] = min(min(plan[i] * d, m) + dp[i-1], dp[i-3] + tm)
    print("#{} {}".format(tc, min(dp[-1], y)))