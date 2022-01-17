from itertools import permutations

def solution(numbers):
    permut = []
    dict_permut = {}
    cnt = 0
    
    for i in range(1, len(numbers)+1):
        for j in list(permutations(numbers, i)):
            permut.append(j)
            dict_permut[int("".join(permut.pop()))] = 0
    permut = list(dict_permut.keys())
    
    for num in permut:
        if (sosu(num)): cnt += 1
    return cnt

def sosu(number): # 소수이면 True, 소수가 아니면 False 반환
    if number <= 1: return False
    for i in range(2, number):
        if number % i == 0: return False
    return True
