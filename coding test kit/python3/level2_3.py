def solution(s):
    flag = True
    answer = ""
    for c in s:
        if flag == True: 
            flag = False
            answer += c.upper()
        else: answer += c.lower()
        if c == " ": flag = True
    return answer
