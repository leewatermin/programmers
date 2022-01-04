def solution(progresses, speeds):
    answer = []
    for day in range(100):
        deploy = 0
        for i in range(len(progresses)): #배포
            if progresses[0] >= 100:
                deploy += 1
                del progresses[0]
                del speeds[0]
        if deploy != 0: 
            answer.append(deploy)
        for i in range(len(progresses)): #개발
            progresses[i] += speeds[i]
    return answer
