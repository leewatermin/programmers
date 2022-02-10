import math
def solution(n):
    return (math.sqrt(n)+1)*(math.sqrt(n)+1) if math.sqrt(n) % 1 == 0 else -1
