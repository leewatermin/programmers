def solution(left, right):
    answer = 0
    for i in range(left, right+1, 1):
        if zaksuYaksu(i): answer += i
        else: answer -= i
    return answer

def zaksuYaksu(num):
    yaksu = 0
    for i in range(1, num+1):
        if num % i == 0: yaksu += 1
    return (yaksu%2 == 0)
