import re

def solution(my_string):
    answer = []
    num_check = re.compile('[0-9]')
    answer = list(map(int, num_check.findall(my_string)))
    answer.sort()
    return answer