def solution(t, p):
    answer = 0
    p_len = len(p)
    p_num = int(p)
    
    for i in range(len(t) - p_len + 1):
        substring = t[i: i+p_len]
        substring_num = int(substring)
        if p_num >= substring_num:
            answer += 1
    return answer