import sys
sys.stdin = open('input.txt')

T = int(input())
for t in range(1, T+1):
    N = int(input())
    nums = list(map(int, input().split()))
    nums.sort()
    left = []
    right = []
    for i in range(N):
        if i % 2:
            left.append(nums[i])
        else:
            right.append(nums[i])
    res = right + list(reversed(left))
    maxV = 0
    # print(left, right)
    # print(res)
    for i in range(-1, N-1):
        ans = abs(res[i+1] - res[i])
        # print(ans)
        if maxV < ans:
            maxV = ans
    print(f"#{t} {maxV}")