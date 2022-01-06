def solution(brown, yellow):
    for i in range(1, brown):
        for j in range(1, brown):
            if(i*j == brown+yellow and (i-2)*(j-2) == yellow):
                return [i, j] if (i>j) else [j, i]
