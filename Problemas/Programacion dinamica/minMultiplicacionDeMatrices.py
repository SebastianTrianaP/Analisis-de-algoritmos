import math #-----------------Recursivo--------------------
def ParenthesesMaxMult(D):
	return ParenthesesMaxMult_Aux(D, 1, len(D)-1)

def ParenthesesMaxMult_Aux(D, i, j):
    if i == j:
        return 0
    else:
        q = math.inf
        for k in range(i, j):
            print(i)
            print(k)
            v = ParenthesesMaxMult_Aux(D, i, k) + ParenthesesMaxMult_Aux(D, k+1, j)+ D[i-1]*D[k]*D[j]
            if v < q:
                q = v
            #end if
        #end for
    return q
    #end if
#end procedure
#-----------------Memorizacion--------------------
def ParenthesesMaxMult_Mem(D):
    M = [ [ math.inf for i in range( len(D) +1)] for j in range( len(D) + 1) ]
    return ParenthesesMaxMult_Mem_Aux(D,1, len(D)-1, M)
def ParenthesesMaxMult_Mem_Aux(D, i, j, M):
    if M[i][j] == math.inf:
        if i >= j:
            M[i][j] = 0
        else:
            q = math.inf
            for k in range(i, j):
                v = ParenthesesMaxMult_Mem_Aux(D, i, k, M) + ParenthesesMaxMult_Mem_Aux(D, k+1, j, M)+ D[i-1]*D[k]*D[j]
                if v < q:
                    q = v
                #end if
            #end for
            M[i][j] = q
        #end if
        for fila in M:
            print(fila)
    #end if
    return M[i][j]
#end procedure

#-----------------Forward--------------------
#Suprimir casos base  y agregar la matriz b almacenando el k
def ParenthesesMaxMult_forward(D):
    M = [ [ 0 for i in range( len(D) -1 )] for j in range( len(D) -1 ) ]
    B = [ [ -1 for i in range( len(D) -1 )] for j in range( len(D) -1 ) ]
    for i in range (len(D)-1,0,-1):
        print("i:", i)
        for j in range(i+1, len(D)):
            print("j:", j)
            q = math.inf
            w = -1
            for k in range(i, j):
                print(k-1, i-1, j)
                v = M[i-1][k-1] + M[k][j-1] + D[i-1]*D[k]*D[j]
                print(v)
                if v < q:
                    q = v
                    w = k
            #end if
            #end for
            M[i-1][j-1] = q
            B[i-1][j-1] = w
            print("despues",i-1, j-1, q)
            #end for
    #end for
    for fila in M:
        print(fila)    
    return M[0][len(D)-2]
#end procedure
#-----------------BACKTRAKING--------------------
def ParenthesesMaxMult_backtraking(D):
    M = [ [ 0 for i in range( len(D) -1 )] for j in range( len(D) -1 ) ]
    B = [ [ -1 for i in range( len(D) -1 )] for j in range( len(D) -1 ) ]
    for i in range (len(D)-1,0,-1):
        for j in range(i+1, len(D)):
            q = math.inf
            w = -1
            for k in range(i, j):
                v = M[i-1][k-1] + M[k][j-1] + D[i-1]*D[k]*D[j]
                if v < q:
                    q = v
                    w = k
            #end if
            #end for
            M[i-1][j-1] = q
            B[i-1][j-1] = w
            #end for
    #end for 
        

#end procedure

#---------------------Pruebas-------------------
D = [ 10, 100, 5 , 50]
print(ParenthesesMaxMult(D))
#print(ParenthesesMaxMult_Mem(D))
print("============")
print(ParenthesesMaxMult_forward(D))
#print(ParenthesesMaxMult_backtraking(D))
