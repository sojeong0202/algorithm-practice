import sys
input = sys.stdin.readline

N = int(input())
TList = map(int, input().split())
T, P = map(int, input().split())

TResult = 0
for i in TList:
    if i % T != 0:
        TResult += 1
    TResult += (i // T)
print(TResult)
print(N // P, N % P)