def solution(video_len, pos, op_start, op_end, commands):
    answer = ''
    answer_pos = pos
    
    mm, ss = map(int, answer_pos.split(':'))
    op_start_mm, op_start_ss = map(int, op_start.split(':'))
    op_end_mm, op_end_ss = map(int, op_end.split(':'))
    total_mm, total_ss = map(int, video_len.split(':'))
    
    pos_ss = mm*60 + ss
    op_start_s = op_start_mm*60 + op_start_ss
    op_end_s = op_end_mm*60 + op_end_ss
    total = total_mm*60 + total_ss
    
    pos_ss = judge_op_jump(pos_ss, op_start_s, op_end_s)
    
    
    for i in commands:
        if i[0] == 'p':
            pos_ss -= 10
            if pos_ss < 0:
                pos_ss = 0
            pos_ss = judge_op_jump(pos_ss, op_start_s, op_end_s)
        else:
            pos_ss += 10
            if pos_ss > total:
                pos_ss = total
            pos_ss = judge_op_jump(pos_ss, op_start_s, op_end_s)
    
    mm = pos_ss // 60 
    ss = pos_ss % 60 
    answer_pos = f'{mm:02}:{ss:02}' 
    return answer_pos

def judge_op_jump(pos_ss, op_start_s, op_end_s):
    j_boolean = False
    
    if op_start_s <= pos_ss and pos_ss < op_end_s:
        j_boolean = True
    
    if j_boolean == True:
        pos_ss = op_end_s
    return pos_ss
