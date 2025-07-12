import sys
input = sys.stdin.readline

numList = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
a = int(input())
b = int(input())
c = int(input())
mul = a * b * c

for char in str(mul):
    numList[int(char)] += 1

print(*numList, sep='\n')