def solution(absolutes, signs):
    answer = 0
    for i in range(len(absolutes)): answer += (lambda x: 1 if (x) else -1)(signs[i]) * absolutes[i]
    return answer
