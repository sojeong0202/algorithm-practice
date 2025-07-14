import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
  H, W, N = map(int, input().split())
  result = ""
  a = ''
  di = N // H
  rest = N % H
  if rest == 0:
    rest += H
    di -= 1
  if di < 9:
    a = '0'
  a = a + str(di + 1)
  result = str(rest) + a
  print(result)