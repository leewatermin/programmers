def solution(n):
    cnt = 0
    answer = ""
    while True:
        answer += "수"
        cnt += 1
        if cnt == n: return answer
        answer += "박"
        cnt += 1
        if cnt == n: return answer
