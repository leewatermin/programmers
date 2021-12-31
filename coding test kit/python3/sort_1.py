def solution(array, commands):
    answer = []

    for c in commands:
        sub_array = array[c[0]-1:c[1]]
        sub_array.sort()
        answer.append(sub_array[c[2]-1])
        
    return answer
