import math
#-------------FUERZA BRUTA--------------
def LCS( x , y):
    return LCS_Aux( x, y, len(x)-1, len(y)-1)

def LCS_Aux( x , y , i , j):
    if i < 0 or j < 0:
         return  0;
    else:
        if x[i] == y[j]:
            return LCS_Aux(x , y, i-1, j-1) + 1
        else:
            q = - math.inf
            vl = LCS_Aux(x, y, i, j-1)
            vr = LCS_Aux(x, y ,i-1, j)
            if vl > q:
                q = vl
            if vr > q:
                q = vr     
            return q
        
#-------------MEMORIZACION--------------
def LCS_mem( x , y):
    M = [ [ -math.inf for i in range( len(x) + 1 )] for j in range( len(y) + 1) ]
    return LCS_Aux_mem( x, y, len(x)-1, len(y)-1, M)
    for fila in M:
        print(fila)

def LCS_Aux_mem( x , y , i , j , M):
    if M[i][j] == -math.inf:
        if i < 0 or j < 0:
            M[i][j]  = 0;
        else:
            if x[i] == y[j]:
                M[i][j] = LCS_Aux_mem(x , y, i-1, j-1, M) + 1
            else:
                q = - math.inf
                vl = LCS_Aux_mem(x, y, i, j-1, M)
                vr = LCS_Aux_mem(x, y ,i-1, j, M)
                if vl > q:
                    q = vl
                if vr > q:
                    q = vr     
                M[i][j] = q
    return M[i][j]

#-------------BOTTOM UP--------------
def LCS_BU(x, y):
    M = [[0 for i in range(len(y) + 1)] for j in range(len(x) + 1)]
    for i in range (1, len(x)+1):
        for j in range (1, len(y)+1):
            if x[i-1] == y[j-1]:
                M[i][j] = M[i - 1][j - 1] + 1
            else :
                vl = M[i][j - 1]
                vr = M[i - 1][j]
                if vl > vr:
                    M[i][j] = vl
                else:
                    M[i][j] = vr
    for fila in M:
        print(fila)
    return M[len(x)][len(y)]

#-------------BACKTRAKING--------------
def LCS_BT(x, y):
    M = [[0 for i in range(len(y) + 1)] for j in range(len(x) + 1)]
    B = [[0 for i in range(len(y) + 1)] for j in range(len(x) + 1)]
    for i in range (1, len(x)+1):
        for j in range (1, len(y)+1):
            if x[i-1] == y[j-1]:
                M[i][j] = M[i - 1][j - 1] + 1
                B[i][j] = "diag"
            else :
                vl = M[i][j - 1]
                vr = M[i - 1][j]
                if vl > vr:
                    M[i][j] = vl
                    B[i][j] = "izq"
                else:
                    M[i][j] = vr
                    B[i][j] = "arr"
    i = len(x)
    j = len(y)
    z = []
    while i!=0 or j!=0:
        if B[i][j]=="diag":
            z.append(x[i-1])
            i=i-1
            j=j-1
        elif B[i][j] == "arr":
            j=j-1
        else:
            i=i-1
    return [M[len(x)][len(y)], z]     
#-----------Pruebas-----------
X = [ "A","B","C","B","D","A","B" ]
Y = [ "B","D","C","A","B","A" ]
#print(LCS(X, Y))
print(LCS_mem(X, Y))
print(LCS_BU(X, Y))
#print(LCS_BT(X, Y))       
    
