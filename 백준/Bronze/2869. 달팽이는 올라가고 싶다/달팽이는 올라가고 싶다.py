import math
import sys

def solution(A, B, V):
    ability = A - B
    exception_last = V - A
    day = 1
    if exception_last <= 0:
        return day
    day += math.ceil(exception_last / ability)
    return day


a, b, v = map(int, sys.stdin.readline().split())
print(solution(a, b, v))