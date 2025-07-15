import sys
import math
input = sys.stdin.readline

T = int(input())
nList = map(int, input().split())
result = 0

def is_prime_number(x):
    if x == 1:
        return False
    
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True

for j in nList:
    if is_prime_number(j):
        result += 1

print(result)