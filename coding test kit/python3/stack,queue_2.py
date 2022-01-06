def solution(priorities, location):
    cnt = 1
    while True:
        if max(priorities) == priorities[0]: #중요도가 가장 높은 문서가 맨 앞에 온 경우
            if location != 0: #내가 요청한 문서가 아닌 경우
                del priorities[0]
                cnt += 1
                location -= 1
            else: #내가 요청한 문서인 경우
                return cnt
        else: #중요도가 높지 않은 문서가 맨 앞에 온 경우
            priorities.append(priorities.pop(0)) 
            location = location - 1 if location !=0 else len(priorities) - 1
