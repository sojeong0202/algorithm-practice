import sys
input = sys.stdin.readline

num, k = map(int, input().split())
a = list(map(int, input().split()))
m, n = 0, 0
count = 0

for i in range(len(a)-1, 0, -1):
    max_index = i
    for j in range(i-1, -1, -1):
        if a[max_index] < a[j]:
            max_index = j
    if a[max_index] != a[i]:
        a[max_index], a[i] = a[i], a[max_index]
        m, n = a[max_index], a[i]
        count += 1
    if count == k:
        print(m, n)
        break
if count < k:
    print(-1)
