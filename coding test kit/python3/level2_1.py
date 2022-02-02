def solution(record):
    user = {}
    answer = []
    for i in range(len(record)):
        if record[i][0] == 'E': user[record[i].split(' ')[1]] = record[i].split(' ')[2]
        elif record[i][0] == 'C': user[record[i].split(' ')[1]] = record[i].split(' ')[2]
    for i in range(len(record)):
        if record[i][0] == 'C': continue
        else: 
            answer.append(user[record[i].split(' ')[1]] + "님이 " + (lambda i : "들어왔습니다." if (record[i].split(' ')[0][0] == 'E') else "나갔습니다.")(i))
    return answer
