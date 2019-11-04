def f(n, m, k, z):
    if n == m:
        print(res)
        return
    else :
        for i in range(z, k):
            if used[i] == 0:
                used[i] = 1
                res[n] = num[i]
                f(n+1, m, k, i)
                used[i] = 0


num = [1, 2, 3, 4]
used = [0] * 4 # [0, 0, 0, 0]
res = [0] * 3