import sys

sys.stdin = open('input.txt', 'r')

for tc in range(1, 2):
    N = int(input())
    origin = list(input().split())
    order_cnt = int(input())
    orders = list(input().split())
    order_num = []
    re_orders = []
    i = 0
    while i < len(orders):
        j = i
        if orders[i] == 'I':
            spot = int(orders[j + 1])
            cnt = int(orders[j + 2])
            k = 0
            j = j + 3
            while k < cnt:
                origin.insert(spot + k, orders[j])
                k += 1
                j += 1
            i = j
        elif orders[i] == 'D':
            spot2 = int(orders[j + 1])
            cnt2 = int(orders[j + 2])
            j = j + 3
            k = 0
            while k < cnt2:
                origin.pop(spot2)
                k += 1
            i = j
        elif orders[i] == 'A':
            cnt3 = int(orders[j + 1])
            k = 0
            j = j + 2
            while k < cnt3:
                origin.append(orders[j])
                k += 1
                j += 1
            i = j
    print('#{} {}'.format(tc, ' '.join(origin[:10])))
