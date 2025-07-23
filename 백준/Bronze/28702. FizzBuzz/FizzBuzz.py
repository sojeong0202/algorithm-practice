def solution(str_list):
    result = 0
    for i in range(0,3):
        if str_list[i].isdigit() :
            result = int(str_list[i]) + (3-i)
            break
    if result % 15 == 0:
        return "FizzBuzz"
    elif result % 3 == 0:
        return "Fizz"
    elif result % 5 == 0:
        return "Buzz"
    else:
        return result
    
    
input_list = []

for _ in range(3):
    input_list.append(input())
    
print(solution(input_list))