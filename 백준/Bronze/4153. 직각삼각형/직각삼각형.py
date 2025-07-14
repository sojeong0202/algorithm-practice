import sys
input = sys.stdin.readline

while True:
  A, B, C = map(int, input().split())

  if A == 0 and B == 0 and C == 0:
    break
  if max(A, B, C)**2 == A**2 + B**2 + C**2 - max(A, B, C)**2:
    print("right")
  else:
    print("wrong")