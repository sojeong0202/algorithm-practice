import sys

def solution(n):
    if n == 1:
        return 1
    for i in range(1, 100000):
        if (3*i**2 - 3*i + 2) <= n < (3*i**2 + 3*i + 2):
            return i + 1
    return -1

print(solution(int(sys.stdin.readline())))
