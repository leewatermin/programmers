def solution(n, lost, reserve):
    lost.sort()
    reserve.sort()

    cnt = n - len(lost)

    for l in range(len(lost)): #체육복을 도난당했지만 여벌의 체육복을 가져온 학생인 경우
        for r in range(len(reserve)):
            if lost[l] == reserve[r]:
                lost[l] = 0
                reserve[r] = 0
                cnt += 1
                break

    lost = list(filter(lambda x: x!= 0, lost))
    reserve = list(filter(lambda x: x!= 0, reserve))

    for l in range(len(lost)): #여벌의 체육복을 빌려야하는 학생인 경우
        for r in range(len(reserve)):
            if lost[l]-1 == reserve[r] or lost[l]+1 == reserve[r]:  
                reserve[r] = -1
                cnt += 1
                break

    return cnt
