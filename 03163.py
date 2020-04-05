import sys

sys.stdin = open('input.txt', 'r')

def f(n, k, z, s, r):
    global minV, N
    if r > minV:
        return
    if n == k:
        # print(s, r)
        r += max(array[s[n-1]:]) - min(array[s[n-1]:])
        if minV > r:
            minV = r
        return
    for i in range(z, N):
        if used[i] == 0:
            used[i] = 1
            f(n+1, k, i, s + [i], r + (max(array[s[n-1]:i]) - min(array[s[n-1]:i+1])))
            used[i] = 0

N, K = map(int, input().split())
# N 원소수
# K 부분 배열 수
minV = 99999999999
array = list(map(int, input().split()))
used = [0] * N
# print(array)
f(1, K, 1, [0], 0)
print(minV)