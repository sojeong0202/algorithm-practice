import sys
input = sys.stdin.readline

def solution(a, b, c):
    if a == "Fizz":
        if b != "Fizz" and b != "Buzz" and b != "FizzBuzz":
            b = int(b)
            if (b + 2) % 5 == 0:
                return "FizzBuzz"
        if c != "Fizz" and c != "Buzz" and c != "FizzBuzz":
            c = int(c)
            if (c + 1) % 5 == 0:
                return "FizzBuzz"
        return "Fizz"
    if a != "Fizz" and a != "Buzz" and a != "FizzBuzz":
        a = int(a)
        if (a + 3) % 5 == 0:
            return "Buzz"
        return a + 3
    if b != "Fizz" and b != "Buzz" and b != "FizzBuzz":
        b = int(b)
        if (b + 2) % 15 == 0:
            return "FizzBuzz"
        elif (b + 2) % 3 == 0:
            return "Fizz"
        elif (b + 2) % 5 == 0:
            return "Buzz"
        return b + 2
    if c != "Fizz" and c != "Buzz" and c != "FizzBuzz":
        c = int(c)
        if (c + 1) % 15 == 0:
            return "FizzBuzz"
        elif (c + 1) % 3 == 0:
            return "Fizz"
        elif (c + 1) % 5 == 0:
            return "Buzz"
        return c + 1
    return None


n1 = input().strip()
n2 = input().strip()
n3 = input().strip()
print(solution(n1, n2, n3))


