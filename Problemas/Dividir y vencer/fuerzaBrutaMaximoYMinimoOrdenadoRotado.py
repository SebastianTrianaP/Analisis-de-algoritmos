import math

def findMaxMin(S):
    maximo = - math.inf
    minimo = math.inf
    for i in range(0,len(S)-1):
        if S[i] > maximo:
            maximo = S[i]
        if S[i] < minimo:
            minimo = S[i]
    return [maximo, minimo]

S =(67, 89, 90, 23, 25, 34, 50, 60)
print(findMaxMin(S))
