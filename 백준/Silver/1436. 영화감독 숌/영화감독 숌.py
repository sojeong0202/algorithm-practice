import sys

def solution(target_num):
    count_num = 1
    result_num = 666
    while count_num != target_num:
        result_num += 1
        if "666" in str(result_num):
            count_num += 1
    return result_num

print(solution(int(sys.stdin.readline())))

