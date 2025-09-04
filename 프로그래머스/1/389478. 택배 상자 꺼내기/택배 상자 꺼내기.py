def solution(n, w, num):
    answer = 0
    sum_stack = list()
    k = n // w
    if w == 1:
        return n - num + 1
    for i in range(k, 0, -1):
        sum = i*w + i*w + 1
        sum_stack.append(sum)
        if (i-1)*w +1 <= num and num <= i*w:
            break
    # print(sum_stack)
    sub_num = num
    for j in reversed(sum_stack):
        remain = j - sub_num
        if remain > num and remain <= n:
            answer += 1
            sub_num = remain
    answer += 1
    return answer