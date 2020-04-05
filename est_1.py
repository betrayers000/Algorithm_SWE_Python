
def solution(A):
    temp = [0] * 100000
    dic = {}
    for val in A:
        if temp[val] != -1:
            temp[val] += 1
        if temp[val] > val:
            temp[val] = -1
            del dic[val]
        if temp[val] == val:
            dic[val] = 1
    if dic == {}:
        return 0
    return max(dic.keys())


arr = [3, 8, 2, 3, 3, 2]

print(solution(arr))