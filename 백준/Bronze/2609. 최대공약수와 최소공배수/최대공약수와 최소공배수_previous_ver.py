import sys
input = sys.stdin.readline

def gcd(a, b):
    if a % b == 0:
        return b
    return gcd(b, a%b)


def lcm(a, b, gcd_num):
    return (a * b) // gcd_num


n1, n2 = map(int, input().split())
gcd_result = gcd(n1, n2)
print(gcd_result)
print(lcm(n1, n2, gcd_result))
