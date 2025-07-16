import sys

def solution(x):
    for i in range(max(0, x - 9 * len(str(x))), x+1):
        sum = i
        for j in str(i):
            sum += int(j)
        if sum == x:
            return i
    return 0

print(solution(int(sys.stdin.readline())))
