def solution(clothes):
    answer = 1
    clothes_dict = {}
    for cloth in clothes: #가진 의상의 종류별 개수 확인
        if cloth[1] in clothes_dict:
            clothes_dict[cloth[1]] += 1
        else:
            clothes_dict[cloth[1]] = 1
    for val in clothes_dict.values(): #(n+1)!-1 구현
        answer *= (val+1)
    return answer-1
