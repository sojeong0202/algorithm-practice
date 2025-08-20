import re

def solution(my_string):
    answer = []
    # num_check = re.compile('[0-9]')
    answer = list(map(int, re.findall('[0-9]', my_string)))
    answer.sort()
    return answer