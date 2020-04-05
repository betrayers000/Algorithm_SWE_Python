arr = [1, 3, 1, 2]


def solution(A):
    cnt = 0
    temp = -1
    w = False
    remove = []
    for i in range(1, len(A)-1):
        if w:
            w = False
            continue
        if cnt == 2:
            return -1
        if (A[i] == A[i-1]) or (A[i] == A[i+1]):
            if (A[i] < A[i - 1] and A[i] < A[i + 2]) or (A[i] > A[i - 1] and A[i] > A[i + 2]):
                w = True
                cnt += 1
                temp = -2
            else:
                return -1
        elif (A[i] < A[i-1] and A[i] < A[i+1]) or (A[i] > A[i-1] and A[i] > A[i+1]):
            pass
        else:
            temp = i
            cnt += 1
            for k in range(i-2, i+3):
                if k < 0 or k >= len(A):
                    continue
                else:
                    remove.append(A[k])
    if cnt >= 2:
        return -1
    if temp == -1:
        return 0
    elif temp == -2:
        return 2

    idx = (4 - len(remove)) * -1
    ans = 0
    for _ in range(3):
        remove_temp = remove.copy()
        del remove_temp[idx]
        idx += 1
        for i in range(1, len(remove_temp)-1):
            if (remove_temp[i] < remove_temp[i - 1] and remove_temp[i] < remove_temp[i + 1]) or (remove_temp[i] > remove_temp[i - 1] and remove_temp[i] > remove_temp[i + 1]):
                pass
            else:
                break
            ans += 1
    return ans



print(solution(arr))