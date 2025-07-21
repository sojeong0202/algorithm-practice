import sys
import math
input = sys.stdin.readline

def solution(x):
    x_list = list(str(x))
    stack = []
    [stack.append(i) for i in x_list[0:len(x_list)//2]]
    for j in x_list[math.ceil(len(x_list)/2):]:
        if stack.pop() != j:
            return "no"
    return "yes"

while True:
    n = int(input())

    if n == 0:
        break
    else:
        print(solution(n))