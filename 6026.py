import sys

sys.stdin = open('input.txt', 'r')

T = int(input())
for t in range(1, T + 1):
    M, N = map(int, input().split())




#
# def ncr(n, r):
#     global factorial
#     up = factorial[n]
#     down = factorial[r]
#     down2 = factorial[n - r]
#     num = (up * math_pow(down, prime - 2)) % prime * math_pow(down2, prime - 2) % prime
#     return num % prime
#
# def math_pow(front, back):
#     global prime
#     res = 1
#     front = front % prime
#     while back > 0:
#         if back % 2 == 1:
#             res = (res * front) % prime
#         back = back >> 1
#         front = (front * front) % prime
#     return res%prime
#
# def Factorial():
#     factorial[0] = 1
#     for i in range(1, 101):
#         factorial[i] = factorial[i - 1] * i % prime
#
#
# prime = 1000000007
# factorial = [0] * (101)
# T = int(input())
# for t in range(1, T + 1):
#     M, N = map(int, input().split())
#     Factorial()
#     count = 0
#     number = 0
#     under = M
#     for i in range(M):
#         if count % 2 == 0:
#             number += (math_pow(under, N) * ncr(M, count)) % prime
#         else:
#             number -= (math_pow(under, N) * ncr(M, count)) % prime
#         under -= 1
#         count += 1
#     result = number % prime
#     if result < 0:
#         result += prime
#     print(result)