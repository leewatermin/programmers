def solution(n):
    tmp = 0
    for i in range(1, n+1):
        if n%i == 0: tmp += i
    return tmp
