import sys
input = sys.stdin.readline

T = int(input())

for i in range(0, T):
    stack = []
    PS = input()
    for char in PS:
        if char == "(":
            stack.append("(")
        elif len(stack) != 0 and char == ")":
            stack.pop()
        elif len(stack) == 0 and char == ")":
            stack.append("IPS")
            break
    if len(stack) == 0:
        print("YES")
    else:
        print("NO")
