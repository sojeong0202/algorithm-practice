import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
  a = input()
  result = 0
  flag = 1
  for char in a:
    if char == 'O':
      result += flag
      flag += 1
    elif char == 'X':
      flag = 1
  print(result)