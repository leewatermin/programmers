def solution(n):
    answer = []
    n = list(str(n))
    for i in n: answer.insert(0, int(i))
    return answer
