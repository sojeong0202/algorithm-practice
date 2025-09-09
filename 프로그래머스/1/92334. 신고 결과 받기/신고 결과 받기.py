import numpy as np

def solution(id_list, report, k):
    answer = [0 for h in range(len(id_list))]

    complain_list = np.zeros([len(id_list), len(id_list)], dtype=int)
    
    for i in report:
        u1, u2 = map(id_list.index, i.split())
        if complain_list[u1][u2] == 0:
            complain_list[u1][u2] += 1
    
    report_user = complain_list.sum(axis=0)
    banned_user = [j for j in range(len(report_user)) if report_user[j] >= k]
    
    for k in banned_user:
        for l in range(len(id_list)):
            if complain_list[l][k] == 1:
                answer[l] += 1
    return answer