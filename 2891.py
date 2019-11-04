import sys
sys.stdin = open('input.txt', 'r')


def s(i, j):
    check = cell[(i, j)]
    if len(check) == 2:
        if check[0] != 0 and check[1] != 0:
            return
    else:
        if check[0] != 0:
            return
    x, y = i // 2 * 2, j // 3 * 3
    cnt = 0
    nums = {1, 2, 3, 4, 5, 6, 7, 8, 9}
    for r in range(x, x + 2):
        for c in range(y, y + 3):
            for n in cell[(r, c)]:
                if n != 0:
                    cnt += 1
                    nums = nums - {n}
    for c in range(6):
        for n in cell[(i, c)]:
            if n != 0:
                cnt += 1
                nums = nums - {n}
    for r in range(6):
        for n in cell[(r, j)]:
            if n != 0:
                cnt += 1
                nums = nums - {n}
    # if len(cell[(i, j)]) == 2:
    #     l, r = cell[(i, j)]
    #     if l == 0 and r == 0:
    #         pass
    #     elif l != 0:
    #         for n in nums:
    #             if l > n:
    #                 nums = nums - {n}
    #     elif r != 0:
    #         for n in nums:
    #             if r < n:
    #                 nums = nums - {n}
    if nums == set():
        return
    return i, j, nums


def search():
    global q
    q = []
    for i in range(6):
        for j in range(6):
            ans = s(i, j)
            if ans != None:
                q.append(ans)
    q.sort(key=lambda x: len(x[2]))
    return q


def fill(q_list):
    top = 0
    while top < len(q_list):
        x, y, temp = q_list[top]
        temp = list(temp)
        if len(temp) > 2:
            break
        if len(temp) == 2:
            if len(temp) == 2 and len(cell[(x, y)]) == 2 and sum(cell[(x, y)]) == 0:
                cell[(x, y)] = [min(temp[0], temp[1]), max(temp[1], temp[0])]
        else:
            if len(cell[(x, y)]) == 2:
                l, r = cell[(x, y)]
                if l == 0:
                    cell[(x, y)] = [temp[0], r]
                else:
                    cell[(x, y)] = [l, temp[0]]
            else:
                cell[(x, y)] = [temp[0]]
        top += 1


T = int(input())
for t in range(1, T + 1):
    board = [input().split() for _ in range(6)]
    cell = {}
    for i in range(6):
        for j in range(6):
            temp = []
            for w in board[i][j]:
                if w == "-":
                    temp.append(0)
                elif w != "/" and w != "-":
                    temp.append(int(w))
            cell[(i, j)] = temp
    time = 0
    while time < 36:
        q = search()
        if q == []:
            break
        fill(q)
        time += 1
    print(f"#{t}")
    print(q)
    for i in range(6):
        temp = []
        for j in range(6):
            tn = cell[(i, j)]
            if len(tn) == 2:
                temp.append(str(tn[0]) + '/' + str(tn[1]))
            else:
                temp.append(str(tn[0]))
        print(" ".join(temp))
