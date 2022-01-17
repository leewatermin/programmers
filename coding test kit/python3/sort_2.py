def solution(numbers):
    answer = ''
    tmp = []
    
    for number in numbers:
        c = (str(number) * 4)[:4]
        length = len(str(number))
        tmp.append((c, length))
    tmp.sort(reverse = True)
    
    for i in range(len(tmp)): answer += tmp[i][0][:tmp[i][1]]

    return '0' if int(answer) == 0 else answer
