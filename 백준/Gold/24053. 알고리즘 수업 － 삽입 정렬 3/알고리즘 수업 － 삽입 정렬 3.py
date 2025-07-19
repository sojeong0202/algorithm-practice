import sys
input = sys.stdin.readline

num = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
flag = 0

for i in range(1, len(a)):
    index = i-1
    new_item = a[i]
    while 0 <= index and new_item < a[index]:
        a[index+1] = a[index]
        if a == b:
            flag = 1
        index -= 1
    if index+1 != i:
        a[index+1] = new_item
        if a == b:
            flag = 1

print(flag)