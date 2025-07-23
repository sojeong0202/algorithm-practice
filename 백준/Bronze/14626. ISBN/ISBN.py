import sys

def solution(x):
    m = int(x[12])

    sum_num = 0
    star_pos = -1

    for i in range(12):
        if x[i] == '*':
            star_pos = i
        else:
            if i % 2 == 0:
                sum_num += int(x[i])
            else:
                sum_num += 3 * int(x[i])

    # (sum_num + 손상_숫자) % 10 = 10 - m
    # 손상_숫자 = 10 - m - (sum_num % 10)
    target = (10 - m - (sum_num % 10)) % 10
    if star_pos % 2 == 0:
        return target
    else:
        for j in range(10):
            if (j * 3) % 10 == target:
                return j
        return None


print(solution(sys.stdin.readline().strip()))