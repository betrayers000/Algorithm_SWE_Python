import sys

sys.stdin = open('input.txt', 'r')


# + - * /

def f(n, k, s):
    global minV, maxV
    if n == k:
        if s > maxV:
            maxV = s
        if s < minV:
            minV = s
        return
    if opr[0] > 0:
        opr[0] -= 1
        f(n+1, k, s+nums[n+1])
        opr[0] += 1
    if opr[1] > 0:
        opr[1] -= 1
        f(n+1, k, s-nums[n+1])
        opr[1] += 1
    if opr[2] > 0:
        opr[2] -= 1
        f(n+1, k, s*nums[n+1])
        opr[2] += 1
    if opr[3] > 0:
        opr[3] -= 1
        f(n+1, k, int(s/nums[n+1]))
        opr[3] += 1

T = int(input())
for t in range(1, T+1):
    N = int(input())
    opr = list(map(int, input().split()))
    nums = list(map(int, input().split()))
    minV = 100000001
    maxV = -100000001
    f(0, sum(opr), nums[0])
    print(f"#{t} {maxV - minV}")
