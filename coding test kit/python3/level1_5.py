def solution(new_id):
    answer = []
    new_id = list(new_id.lower())
    
    for i in new_id:
        if i == '-' or i == '_' or i == '.' or i.isdigit() or i.isalpha():
            answer += i
    new_id = ''.join(answer)
    
    while True:
        tmp = new_id.replace('..', '.')
        if tmp == tmp.replace('..', '.'): 
            new_id = tmp.replace('..', '.')
            break
        new_id = tmp
    
    answer = list(new_id)
    
    if (answer[0]) and answer[0] == '.': 
        dot_cnt = 0
        for i in range(0, len(answer)-1):
            if answer[i] == '.': 
                dot_cnt += 1
            else: break
        answer = answer[dot_cnt:] 
        
    if len(answer)>0: 
        dot_cnt = 0
        for i in range(len(answer), 1, -1):
            if answer[i-1] == '.': 
                dot_cnt += 1
            else: break
        answer = answer[0:len(answer)-dot_cnt]
        
    if len(answer) == 0: answer = 'a'
    if len(answer) >= 16: 
        dot_cnt = 0
        answer = answer[:15]
        for i in range(len(answer), 1, -1):
            if answer[i-1] == '.': 
                dot_cnt += 1
            else: break
        if dot_cnt == 0: answer = answer[:15]
        else: answer = answer[0:15-dot_cnt]
    
    if len(answer) == 1:
        if answer[0] == '.': return 'aaa'
        answer.append(answer[0])  
        answer.append(answer[0])  
    elif len(answer) == 2: 
        answer.append(answer[1])
    return ''.join(answer)
