def solution(bandage, health, attacks):
    # 남은 체력 return
    answer = health
    attack_time = [row[0] for row in attacks]
    attacks_dict = dict(attacks)
    combo = 0
    for i in range(1, attacks[-1][0]+1):
        if i in attack_time:
            answer -= attacks_dict.get(i)
            combo = 0
            print(answer)
            continue
        # 회복 시간이라면 얼마나?
        answer += bandage[1]
        combo += 1
        # 콤보
        if combo == bandage[0]:
            answer += bandage[2]
            combo = 0
        if answer > health:
            answer = health
        
        if answer <= 0:
            return -1
        print(answer)
        
    if answer <= 0:
        return -1
    return answer