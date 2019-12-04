import math

#==========Algoritmo inocente==========
def zigzag(S):
    p = zigzag_aux(S,0,1)
    n = zigzag_aux(S,0,-1)
    if n < p:
        return p
    else:
        return n

def zigzag_aux(S,i,k):
    if i<=len(S)-1:
        p = nextElement(S,i,k)
        a = zigzag_aux(S,i + 1,k)
        b = 1 + zigzag_aux(S,p,-k)
        if b < a:
            return a
        else:
            return b
    else:
        return 0

def nextElement(S,i,k):
    p = i+1
    while p <= len(S)-1 and (S[i]-S[p])*k >= 0:
        p = p+1
    return p
#==========Algoritmo memorizado==========

def zigzagMem(S):
    M = [ [ 0 for i in range( len(S) + 1 )] for k in range(-1,2,2) ]
    p = zigzag_auxMem(S,0,1, M)
    n = zigzag_auxMem(S,0,-1, M)
    if n < p:
        return p
    else:
        return n
    
def zigzag_auxMem(S,i,k, M):
    if(k == -1):
        x = 0
    else:
        x = 1
    if M[x][i] != - math.inf:
        if i<=len(S)-1:
            p = nextElement(S,i,k)
            a = zigzag_auxMem(S,i + 1, k, M)
            b = 1 + zigzag_auxMem(S,p, -k, M)
            if b < a:
                M[x][i] = a
            else:
                M[x][i] = b
        else:
            M[x][i] = 0
    return M[x][i]

#==========Algoritmo BU==========

def zigzagBU(S):
    M = [ [ 0 for i in range( len(S) + 1 )] for k in range(-1,2,2) ]
    for i in range (len(S)-1,-1,-1):
        for k in range(-1,2,2):
            p = i+1
            while p <= len(S)-1 and (S[i]-S[p])*k >= 0:
                p = p+1
            print(i, k, p)
            if k == -1:
                x = 0
            else:
                x = 1
            print(x, i+1)
            a = M[x][i+1]
            if -k == -1:
                y = 0
            else:
                y = 1
            b = 1 + M[y][p]
            if b < a:
                M[x][i] = a
            else:
                print(x, i+1)
                M[x][i] = b
            #end if
        #end for
    #end for
    for row in M:
        for elem in row:
            print(elem, end=' ')
        print()
    return max(M[0][0], M[1][0])
            
#==========Pruebas==========
S=[1,7,4,9,2,5]
#print(zigzag(S))
print(zigzagMem(S))
#print(zigzagBU(S))

