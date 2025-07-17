import sys
input = sys.stdin.readline

num, k = map(int, input().split())
a = list(map(int, input().split()))
count = 0

for i in range(1, len(a)):
    index = i-1
    new_Item = a[i]

    while 0 <= index and new_Item < a[index]:
        a[index+1] = a[index]
        count += 1
        index -= 1
        if count == k:
            print(a[index+1])
            break
    if index+1 != i:
        a[index+1] = new_Item
        count += 1
    if count == k:
        print(a[index+1])
        break
if count < k:
    print(-1)