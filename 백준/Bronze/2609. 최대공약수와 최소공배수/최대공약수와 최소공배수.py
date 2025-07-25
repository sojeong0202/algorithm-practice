import sys
input = sys.stdin.readline

import math
a, b = map(int, input().split())

print(math.gcd(a, b))
print(math.lcm(a, b))