import sys

T = int(sys.stdin.readline())

for _ in range(T):
  a, b = input().split()
  a = int(a)

  result = ""
  for char in b:
    result += char * a
  print(result)