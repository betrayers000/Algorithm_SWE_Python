import sys

sys.stdin = open('input.txt', 'r')


numbers = [6, 2, 5, 5, 4, 5, 6, 3, 7, 6]
N = int(input())
n = 0
if N % 2 == 0:
    print("1" * (N//2))
else:
    s = N-3
    if s > 0:
        print("7" + ("1" * (s // 2)))
    else:
        print("7")