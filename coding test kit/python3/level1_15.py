def solution(a, b):
    answer = 0
    tmp = a
    if a > b: 
        a = b
        b = tmp
    for i in range(a, b+1): answer += i
    return answer
        
